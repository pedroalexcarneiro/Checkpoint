import pytest
from gamevault.game_import import save_import
from gamevault.integrations import MetadataResult
from gamevault.trash_import import removed_match,save_decision


def previous(library):
    result=MetadataResult('steam','42','Game')
    identity=save_import(library,{'title':'Game','platform':'PC','notes':'Minha história','cover':'manual.png'},result=result)
    library.add_diary(identity,'Memória preservada');library.delete(identity)
    return identity,result


def test_restore_retains_history_and_art(library):
    old,result=previous(library)
    match=removed_match(library,{'title':'Game','platform':'PC'},result=result)
    assert match['id']==old
    restored=save_decision(library,{'title':'Game','platform':'PC'},result=result,removed_id=old,decision='restore')
    assert restored==old and library.get(old)['notes']=='Minha história'
    assert library.get(old)['cover']=='manual.png' and len(library.diary(old))==1
    assert len(library.games())==1


def test_new_entry_preserves_trash_and_does_not_steal_identity_on_restore(library):
    old,result=previous(library)
    fresh=save_decision(library,{'title':'Game','platform':'PC'},result=result,removed_id=old,decision='new')
    assert fresh!=old and library.get(old) is None
    assert library.sql.execute('SELECT notes FROM games WHERE id=?',(old,)).fetchone()[0]=='Minha história'
    library.restore(old)
    assert len(library.games())==2
    assert library.sql.execute("SELECT game_id FROM external_identifiers WHERE provider='steam' AND external_id='42'").fetchone()[0]==fresh


def test_cancel_and_failed_new_leave_trash_unchanged(library):
    old,result=previous(library)
    assert save_decision(library,{'title':'Game'},result=result,removed_id=old,decision='cancel') is None
    with pytest.raises(ValueError):save_decision(library,{'title':'Game'},999,result,removed_id=old,decision='new')
    assert library.get(old) is None and library.games()==[]
    assert library.sql.execute('SELECT game_id FROM external_identifiers').fetchone()[0]==old
    assert library.setting(f'trash.identities.{old}') is None


def test_title_matching_is_exact_and_platform_specific(library):
    old,_=previous(library)
    assert removed_match(library,{'title':' game ','platform':'pc'})['id']==old
    assert removed_match(library,{'title':'Game 2','platform':'PC'}) is None
    assert removed_match(library,{'title':'Game','platform':'Nintendo DS'}) is None


def test_explicit_new_does_not_repeat_late_catalog_prompt(library):
    old,_=previous(library)
    fresh=save_decision(library,{'title':'Game','platform':'PC'},removed_id=old,decision='new')
    match=MetadataResult('rawg','999','Game')
    assert removed_match(library,library.get(fresh),result=match) is None
