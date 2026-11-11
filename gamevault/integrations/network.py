"""Diagnósticos por tipos de exceção, nunca por mensagens que contêm URLs privadas."""
import http.client
import errno
import socket
import ssl
import requests
from urllib3 import exceptions as urllib_errors


def error_chain(error):
    pending, seen = [error], set()
    while pending:
        current = pending.pop()
        if id(current) in seen:
            continue
        seen.add(id(current))
        yield current
        for child in [current.__cause__, current.__context__, getattr(current, 'reason', None), *current.args]:
            if isinstance(child, BaseException):
                pending.append(child)


def connection_diagnosis(error):
    chain = list(error_chain(error))
    if any(isinstance(e, (requests.exceptions.ProxyError, urllib_errors.ProxyError)) for e in chain):
        return 'proxy', 'Falha ao conectar pelo proxy. Confira o proxy configurado no Windows ou no ambiente.'
    if any(isinstance(e, (requests.exceptions.SSLError, ssl.SSLError, urllib_errors.SSLError)) for e in chain):
        return 'tls', 'Falha na validação HTTPS. Confira a data do Windows e os certificados da rede. A validação de segurança permanece ativa.'
    if any(isinstance(e, (socket.gaierror, urllib_errors.NameResolutionError)) for e in chain):
        return 'dns', 'Não foi possível resolver o endereço do Google (DNS).'
    if any(isinstance(e, (requests.exceptions.Timeout, TimeoutError, urllib_errors.TimeoutError)) for e in chain):
        return 'timeout', 'O Google não respondeu dentro do prazo. Tente novamente quando a conexão estiver disponível.'
    for e in chain:
        if isinstance(e, OSError):
            number = getattr(e, 'winerror', None) or e.errno
            if number in (10013, errno.EACCES, errno.EPERM):
                return 'access_denied', 'O sistema recusou a abertura da conexão (permissão de rede). Verifique as regras para o executável com o administrador da rede.'
            if number in (10061, errno.ECONNREFUSED):
                return 'refused', 'A conexão foi recusada pela rede ou pelo destino.'
            if number in (10054, errno.ECONNRESET):
                return 'reset', 'A conexão foi interrompida pela rede ou pelo destino.'
    if any(isinstance(e, http.client.RemoteDisconnected) for e in chain):
        return 'remote_closed', 'O destino ou um intermediário encerrou a conexão sem enviar uma resposta HTTP.'
    if any(isinstance(e, (requests.exceptions.ConnectionError, urllib_errors.HTTPError)) for e in chain):
        return 'connection', 'Não foi possível estabelecer conexão com o Google. A causa específica não foi informada pela rede.'
    return 'unknown', ''


def safe_transport_details(error):
    # Somente nomes de classes e códigos numéricos, nunca str(error), URL ou args.
    parts = []
    for item in error_chain(error):
        label = type(item).__name__
        codes = []
        for key in ('errno', 'winerror', 'verify_code'):
            value = getattr(item, key, None)
            if isinstance(value, int) and not isinstance(value, bool):
                codes.append(f'{key}={value}')
        trace = item.__traceback__
        if trace:
            while trace.tb_next:
                trace = trace.tb_next
            from pathlib import Path
            label += '@' + Path(trace.tb_frame.f_code.co_filename).name + ':' + str(trace.tb_lineno) + ':' + trace.tb_frame.f_code.co_name
        parts.append(label + ('(' + ','.join(codes) + ')' if codes else ''))
    return ' > '.join(parts[:12])


def probe_google_connection():
    # Sem código OAuth, token ou JSON. GET é apenas teste de transporte.
    try:
        with requests.get('https://oauth2.googleapis.com/token', timeout=(10, 20),
                          allow_redirects=False, stream=True) as response:
            status = response.status_code
            if status in (200, 400, 404, 405):
                return f'HTTPS ao endpoint de token respondeu (HTTP {status}). Isso confirma alcance de rede, não autenticação. Tente autenticar para validar a troca do token.'
            return f'O endpoint respondeu HTTP {status}. A rede respondeu, mas o acesso esperado não foi confirmado.'
    except requests.RequestException as error:
        code, message = connection_diagnosis(error)
        return f'Teste de conexão [{code}]: {message or "Falha de transporte."} Detalhes técnicos: {safe_transport_details(error)}'
