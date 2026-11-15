import pytest
@pytest.mark.parametrize('appid,title',[('620','Portal 2'),('400','Portal')])
def test_discover_steam_multiple_libraries(folder,appid,title):
 from checkpoint.steam_installations import find_executables
 root=folder/'Steam';other=folder/'Outra unidade';(root/'steamapps').mkdir(parents=True);(other/'steamapps').mkdir(parents=True)
 (root/'steamapps/libraryfolders.vdf').write_text('"libraryfolders" { "0" { "path" "'+str(root)+'" } "1" { "path" "'+str(other)+'" } }',encoding='utf-8')
 install=other/'steamapps/common'/title;install.mkdir(parents=True)
 executable=install/'game.exe';executable.write_bytes(b'fixture')
 (install/'uninstall.exe').write_bytes(b'fixture')
 (other/f'steamapps/appmanifest_{appid}.acf').write_text('"AppState" { "appid" "'+appid+'" "installdir" "'+title+'" }',encoding='utf-8')
 assert find_executables(appid,[root])==[executable.resolve()]
 assert find_executables('999',[root])==[]
