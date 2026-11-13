import pytest
from checkpoint.save_profiles import SaveProfiles

def test_profiles_persist_and_reject_states(library,folder):
    game=library.save_game({'title':'Save profile'})
    profiles=SaveProfiles(library)
    profiles.configure(game,folder,['*.sav'])
    assert profiles.latest(game)['game_id']==game
    for pattern in ['*','*.*','*.state','../*.sav']:
        with pytest.raises(ValueError): profiles.configure(game,folder,[pattern])
    assert profiles.latest(game)['patterns_json']=='["*.sav"]'
