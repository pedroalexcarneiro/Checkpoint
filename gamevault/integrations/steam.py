"""Steam Web API somente leitura; sem acesso a senha, inventário ou compras."""
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import urlencode

from . import IntegrationError
from .http import HttpClient


def steam_id(value):
    value = str(value).strip()
    if len(value) != 17 or not value.isascii() or not value.isdigit():
        raise ValueError('Informe o SteamID64 numérico de 17 dígitos, não o apelido ou URL do perfil.')
    return value


def app_id(value):
    value = str(value)
    if not value.isascii() or not value.isdigit() or not 0 < int(value) < 2**32:
        raise ValueError('AppID Steam inválido.')
    return str(int(value))


def nonnegative(value):
    if type(value) is not int or value < 0:
        raise IntegrationError('A Steam retornou dados numéricos inválidos. Nenhum dado foi importado.')
    return value


@dataclass(frozen=True)
class SteamGame:
    app_id: str
    title: str
    minutes: int | None


@dataclass(frozen=True)
class SteamAchievement:
    api_name: str
    title: str
    unlocked_at: str | None


class SteamProvider:
    def __init__(self, key, http=None):
        if not key or not key.strip():
            raise IntegrationError('Configure uma chave Steam Web API no cofre do Windows.')
        self.key = key.strip()
        self.http = http or HttpClient()

    def request(self, resource, params):
        url = 'https://api.steampowered.com/' + resource + '/?' + urlencode({'key': self.key, **params})
        try:
            payload = self.http.json(url)
        except IntegrationError:
            raise IntegrationError('Não foi possível consultar a Steam. Confira a chave, a conexão e a privacidade da conta.') from None
        if not isinstance(payload, dict):
            raise IntegrationError('Resposta Steam inválida. Nenhum dado foi alterado.')
        return payload

    def owned_games(self, account):
        account = steam_id(account)
        payload = self.request('IPlayerService/GetOwnedGames/v0001', {
            'steamid': account, 'include_appinfo': 1, 'include_played_free_games': 1,
        })
        response = payload.get('response')
        if not isinstance(response, dict) or 'game_count' not in response:
            raise IntegrationError('Biblioteca Steam indisponível. Confira o SteamID64 e a privacidade de “Detalhes dos jogos”. A biblioteca local foi preservada.')
        count = nonnegative(response['game_count'])
        rows = response.get('games', [])
        if not isinstance(rows, list) or len(rows) != count:
            raise IntegrationError('A lista Steam está incompleta. Consulte novamente antes de importar.')
        games, seen = [], set()
        for row in rows:
            if not isinstance(row, dict):
                raise IntegrationError('A Steam retornou um jogo inválido.')
            try:
                identity = app_id(row.get('appid', ''))
            except ValueError:
                raise IntegrationError('A Steam retornou um AppID inválido.') from None
            title = row.get('name')
            if identity in seen or not isinstance(title, str) or not title.strip():
                raise IntegrationError('A Steam retornou jogos duplicados ou sem título. Consulte novamente.')
            seen.add(identity)
            minutes = row.get('playtime_forever')
            games.append(SteamGame(identity, title.strip(), None if minutes is None else nonnegative(minutes)))
        return sorted(games, key=lambda game: game.title.casefold())

    def achievements(self, account, identity):
        payload = self.request('ISteamUserStats/GetPlayerAchievements/v0001', {
            'steamid': steam_id(account), 'appid': app_id(identity), 'l': 'brazilian',
        })
        stats = payload.get('playerstats')
        if not isinstance(stats, dict) or stats.get('success') is not True:
            raise IntegrationError('Conquistas indisponíveis: confira a privacidade e se este jogo oferece conquistas Steam. Os registros anteriores foram preservados.')
        rows = stats.get('achievements')
        if not isinstance(rows, list):
            raise IntegrationError('A Steam não retornou a lista de conquistas. Os registros anteriores foram preservados.')
        result, seen = [], set()
        for row in rows:
            if not isinstance(row, dict):
                raise IntegrationError('Resposta de conquistas inválida.')
            name = row.get('apiname')
            if not isinstance(name, str) or not name or name in seen or type(row.get('achieved')) is not int or row['achieved'] not in (0, 1):
                raise IntegrationError('Resposta de conquistas inválida.')
            seen.add(name)
            unlocked = None
            if row['achieved']:
                timestamp = nonnegative(row.get('unlocktime', 0))
                try:
                    unlocked = datetime.fromtimestamp(timestamp, timezone.utc).isoformat() if timestamp else ''
                except (OverflowError, OSError, ValueError):
                    raise IntegrationError('Data de conquista Steam inválida.') from None
            title = row.get('name') or name
            if not isinstance(title, str):
                raise IntegrationError('Título de conquista Steam inválido.')
            result.append(SteamAchievement(name, title, unlocked))
        return result
