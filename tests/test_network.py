import socket
import ssl
from unittest.mock import Mock
import pytest
import requests
from urllib3 import exceptions as ue
from gamevault.integrations.network import connection_diagnosis, probe_google_connection

@pytest.mark.parametrize('error,category', [
 (requests.exceptions.ProxyError('secret'), 'proxy'),
 (requests.exceptions.SSLError('secret'), 'tls'),
 (requests.exceptions.ConnectionError(ue.MaxRetryError(None, '/private', socket.gaierror(11001, 'secret'))), 'dns'),
 (requests.exceptions.ConnectionError(ue.ReadTimeoutError(None, '/private', 'secret')), 'timeout'),
 (requests.exceptions.ConnectionError(ConnectionResetError(10054, 'secret')), 'reset'),
 (requests.exceptions.ConnectionError(ConnectionRefusedError(10061, 'secret')), 'refused'),
 (requests.exceptions.ConnectionError('secret'), 'connection'),
 (ValueError('secret'), 'unknown'),
])
def test_safe_nested_diagnosis(error,category):
 code,message = connection_diagnosis(error)
 assert code == category
 assert 'secret' not in message and '/private' not in message


def test_chain_handles_cycles():
 error = requests.exceptions.ConnectionError('secret')
 error.__cause__ = error
 assert connection_diagnosis(error)[0] == 'connection'


def test_probe_does_not_send_oauth_data(monkeypatch):
 response = Mock(status_code=405)
 response.__enter__ = Mock(return_value=response)
 response.__exit__ = Mock(return_value=False)
 get = Mock(return_value=response)
 monkeypatch.setattr(requests, 'get', get)
 assert 'não autenticação' in probe_google_connection()
 args,kwargs = get.call_args
 assert args == ('https://oauth2.googleapis.com/token',)
 assert kwargs == dict(timeout=(10,20), allow_redirects=False, stream=True)


def test_probe_reports_tls_without_error_contents(monkeypatch):
 monkeypatch.setattr(requests,'get',Mock(side_effect=requests.exceptions.SSLError('private-token')))
 result = probe_google_connection()
 assert '[tls]' in result and 'private-token' not in result


def test_safe_details_exclude_exception_messages():
 from gamevault.integrations.network import safe_transport_details
 error = requests.exceptions.ConnectionError(OSError(10013, 'private-token URL code=secret'))
 result = safe_transport_details(error)
 assert '10013' in result and 'OSError' in result
 assert 'private-token' not in result and 'secret' not in result
 assert connection_diagnosis(error)[0] == 'access_denied'


def test_remote_disconnect_is_recognized():
 import http.client
 assert connection_diagnosis(requests.exceptions.ConnectionError(http.client.RemoteDisconnected('private')))[0] == 'remote_closed'
