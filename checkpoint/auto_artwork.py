from .locale import count_text
"""Artes por identidade confirmada, com cache e preservação de escolhas locais."""
import hashlib
import time
from pathlib import Path
from .library import now
from .integrations import IntegrationError
from .integrations.images import ImageCache
from .integrations.metadata import SteamGridDbProvider

KINDS=('cover','banner','logo')


class AutoArtwork:
    def __init__(self,library,provider=None,cache=None,clock=time.time):
        self.library=library;self.provider=provider;self.cache=cache or ImageCache(library.db.path.parent/'images');self.clock=clock
    def confirm_identity(self,game_id,external_id,canonical_title=None):
        if not self.library.get(game_id): raise ValueError('Jogo não encontrado.')
        if not str(external_id).isdigit() or int(external_id)<=0: raise ValueError('Identificador inválido.')
        used=self.library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',('steamgriddb',str(external_id))).fetchone()
        if used and used[0]!=game_id: raise ValueError('Este jogo do provedor já está associado a outro cadastro. Associe a ROM ao jogo existente.')
        with self.library.sql:
            self.library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?) ON CONFLICT(game_id,provider) DO UPDATE SET external_id=excluded.external_id', (game_id,'steamgriddb',str(external_id)))
            self.library.sql.execute('DELETE FROM settings WHERE key=?',(f'artwork.checked.{game_id}',))
            if canonical_title and canonical_title.strip():
                self.library.sql.execute('UPDATE games SET title=?,updated_at=? WHERE id=?',(canonical_title.strip(),now(),game_id))
    def identity(self,game_id):
        return self.library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,'steamgriddb')).fetchone()
    def obtain(self,game_id,force=False):
        game=self.library.get(game_id)
        if not game: return 'Jogo não encontrado; nenhuma arte alterada.'
        if not force and not self.library.setting('artwork.auto',True): return 'Artes automáticas desativadas.'
        missing=[kind for kind in KINDS if not game[kind]]
        if not missing: return 'Capa, banner e logo já definidos; escolhas preservadas.'
        checked=self.library.setting(f'artwork.checked.{game_id}',0)
        if not force and self.clock()-checked<3600: return 'Artes pendentes: consulta recente; tente Obter artes faltantes para consultar novamente.'
        identity=self.identity(game_id)
        steam=self.library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,'steam')).fetchone()
        if not identity and not steam: return 'Artes aguardando identificação: abra Artes e confirme o jogo correto no SteamGridDB.'
        provider=self.provider
        if provider is None:
            from .credentials import CredentialVault
            key=CredentialVault().get('steamgriddb')
            if not key: return 'Configure a chave SteamGridDB para obter capa, banner e logo automaticamente.'
            provider=SteamGridDbProvider(key)
        self.library.set_setting(f'artwork.checked.{game_id}',self.clock())
        if identity is None:
            try:
                resolved=provider.game_from_steam(steam[0]);self.confirm_identity(game_id,resolved.external_id)
                identity=self.identity(game_id)
            except (IntegrationError,ValueError): return 'Não foi possível resolver o AppID Steam no provedor de artes.'
        external_id=identity[0];saved=[];unavailable=[]
        for kind in missing:
            try:
                urls=provider.artworks(external_id,kind)
                if not urls: unavailable.append(kind);continue
                # Até três alternativas por tipo; não reenvia credenciais ao CDN.
                path=None;url=None
                for candidate in urls[:3]:
                    try: path=self.cache.download(candidate);url=candidate;break
                    except (IntegrationError,OSError): continue
                if not path: unavailable.append(kind);continue
                with self.library.sql:
                    current=self.identity(game_id)
                    if not current or current[0]!=external_id: continue
                    cursor=self.library.sql.execute(f"UPDATE games SET {kind}=?,updated_at=? WHERE id=? AND {kind}='' AND deleted_at IS NULL",(path,now(),game_id))
                    if cursor.rowcount:
                        digest=hashlib.sha256(Path(path).read_bytes()).hexdigest()
                        self.library.sql.execute('INSERT INTO artwork_assets VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(game_id,kind) DO UPDATE SET provider=excluded.provider,external_id=excluded.external_id,source_url=excluded.source_url,local_path=excluded.local_path,sha256=excluded.sha256,fetched_at=excluded.fetched_at',
                            (game_id,kind,'steamgriddb',external_id,url,path,digest,now()))
                        saved.append(kind)
            except (IntegrationError,OSError,ValueError): unavailable.append(kind)
        self.library.set_setting(f'artwork.checked.{game_id}',self.clock())
        return count_text(len(saved),'imagem salva','imagens salvas')+'; '+count_text(len(unavailable),'tipo indisponível','tipos indisponíveis')+'. Imagens existentes preservadas.'


def obtain_artwork(library,game_id,force=False):
    # Falha de arte nunca desfaz cadastro, associação ou download de ROM.
    if not force and not library.setting('artwork.auto',True):
        return 'Ficha e artes automáticas desativadas.'
    from .enrichment import complete_game
    has_art_identity=library.sql.execute("SELECT 1 FROM external_identifiers WHERE game_id=? AND provider='steamgriddb'",(game_id,)).fetchone()
    def art():
        try:return AutoArtwork(library).obtain(game_id,force)
        except Exception:return 'Arte pendente: não foi possível consultar o provedor ou o cofre. Jogo e arquivos preservados.'
    # Arte vertical do SteamGridDB tem preferência sobre a imagem de fundo RAWG.
    if has_art_identity:
        artwork=art();metadata=complete_game(library,game_id)
    else:
        metadata=complete_game(library,game_id);artwork=art()
    return metadata+' '+artwork
