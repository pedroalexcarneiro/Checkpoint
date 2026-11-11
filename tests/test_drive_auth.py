import logging
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from gamevault.integrations.drive import GoogleDriveClient
from gamevault.integrations import IntegrationError


def test_token_exchange_failure_reports_stage_without_secrets(monkeypatch, caplog):
    from google_auth_oauthlib.flow import InstalledAppFlow
    flow = Mock()
    flow.run_local_server.side_effect = RuntimeError('private-token-secret')
    monkeypatch.setattr(InstalledAppFlow, 'from_client_secrets_file', lambda *a: flow)
    vault = Mock()
    vault.get.return_value = None
    with caplog.at_level(logging.WARNING), pytest.raises(IntegrationError) as result:
        GoogleDriveClient.authenticate('client.json', vault, True)
    assert 'trocar autorização por token' in str(result.value)
    assert 'private-token-secret' not in str(result.value) + caplog.text
    vault.set.assert_not_called()
    assert flow.run_local_server.call_args.kwargs['authorization_prompt_message'] is None


def test_vault_failure_is_distinct_from_oauth_failure(monkeypatch):
    from google_auth_oauthlib.flow import InstalledAppFlow
    flow = Mock()
    flow.run_local_server.return_value = SimpleNamespace(to_json=lambda: 'private-token')
    monkeypatch.setattr(InstalledAppFlow, 'from_client_secrets_file', lambda *a: flow)
    vault = Mock()
    vault.get.return_value = None
    vault.set.side_effect = OSError('private-token')
    with pytest.raises(IntegrationError, match='salvar token no cofre') as result:
        GoogleDriveClient.authenticate('client.json', vault, True)
    assert 'private-token' not in str(result.value)


def test_success_initializes_drive_after_persisting_token(monkeypatch):
    from google_auth_oauthlib.flow import InstalledAppFlow
    import googleapiclient.discovery
    import google_auth_httplib2
    flow = Mock()
    flow.run_local_server.return_value = SimpleNamespace(to_json=lambda: 'private-token')
    monkeypatch.setattr(InstalledAppFlow, 'from_client_secrets_file', lambda *a: flow)
    monkeypatch.setattr(google_auth_httplib2, 'AuthorizedHttp', lambda *a, **kw: object())
    service = object()
    monkeypatch.setattr(googleapiclient.discovery, 'build', lambda *a, **kw: service)
    vault = Mock()
    vault.get.return_value = None
    assert GoogleDriveClient.authenticate('client.json', vault, True).service is service
    vault.set.assert_called_once_with('drive-readonly', 'private-token')


def test_initial_token_exchange_has_network_timeout(monkeypatch):
    from google_auth_oauthlib.flow import InstalledAppFlow
    captured = []
    flow = Mock()
    flow.run_local_server.side_effect = RuntimeError('stop before network')
    def make_flow(cls, *args):
        captured.append(cls)
        return flow
    monkeypatch.setattr(InstalledAppFlow, 'from_client_secrets_file', classmethod(make_flow))
    parent_fetch = Mock(return_value='test-token')
    monkeypatch.setattr(InstalledAppFlow, 'fetch_token', parent_fetch)
    vault = Mock()
    vault.get.return_value = None
    with pytest.raises(IntegrationError):
        GoogleDriveClient.authenticate('test.json', vault, True)
    instance = object.__new__(captured[0])
    assert instance.fetch_token(authorization_response='private-code') == 'test-token'
    assert parent_fetch.call_args.kwargs['timeout'] == (10, 30)
