"""Empacota somente a variante asInvoker, sem criar tag ou release."""
import hashlib
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET
import zipfile
import pefile
from PyInstaller.archive.readers import CArchiveReader
from checkpoint import __version__
from checkpoint.update_installer import extract_package
from native_startup_check import native_startup
from package_windows_release import smoke,save_smoke


def main():
    if sys.platform!='win32':raise RuntimeError('Build exige Windows.')
    root=Path(__file__).resolve().parents[1];portable=root/'dist'/'Checkpoint'
    executable=portable/'Checkpoint.exe'
    archive=CArchiveReader(str(executable))
    assert 'run_checkpoint_user' in archive.toc and 'run_checkpoint' not in archive.toc
    pe=pefile.PE(str(executable));manifests=[]
    for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries:
        if entry.id!=24:continue
        for name in entry.directory.entries:
            for language in name.directory.entries:
                resource=language.data.struct
                manifests.append(ET.fromstring(pe.get_data(resource.OffsetToData,resource.Size)))
    levels=[element.attrib.get('level') for manifest in manifests for element in manifest.iter() if element.tag.rsplit('}',1)[-1]=='requestedExecutionLevel']
    assert levels==['asInvoker'],levels
    (portable/'LEIA-ME-SEM-ADMIN.txt').write_text('Checkpoint '+__version__+' — variante sem elevação\n\nExtraia o ZIP inteiro e abra Checkpoint.exe.\nO aplicativo usa os privilégios atuais do usuário e não solicita administrador ao iniciar.\nDados continuam no diretório Checkpoint do usuário.\nProgramas externos que exigem administrador continuam sujeitos às permissões do Windows.\n',encoding='utf-8',newline='\n')
    output=root/'user-variant-assets';output.mkdir(exist_ok=True)
    path=output/f'Checkpoint-{__version__}-sem-admin-windows-x64.zip'
    with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as bundle:
        for file in sorted(portable.rglob('*')):
            assert not file.is_symlink()
            if file.is_file():bundle.write(file,file.relative_to(portable.parent).as_posix())
    with zipfile.ZipFile(path) as bundle:assert bundle.testzip() is None
    with TemporaryDirectory(prefix='checkpoint-user-') as temporary:
        temporary=Path(temporary);extracted=extract_package(path,temporary/'extracted')
        command=[str(extracted/'Checkpoint.exe')]
        smoke(command,temporary/'smoke')
        save_smoke(command,temporary/'save')
        native=native_startup(command,temporary/'native')
    with path.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
    (output/(path.name+'.sha256')).write_text(digest+'  '+path.name+'\n',encoding='utf-8')
    record={'version':__version__,'variant':'sem-admin','manifest':'asInvoker','entrypoint':'run_checkpoint_user','native_startup':native,'sha256':digest,'bytes':path.stat().st_size,'windows_standard_account_interactive_test':False}
    (output/'validacao-sem-admin.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
