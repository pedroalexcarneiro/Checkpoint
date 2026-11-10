"""Importação Logiqx DAT; checksum gera candidatos, nunca associa sem revisão."""
import re
import xml.etree.ElementTree as ET
from pathlib import Path

class RomCatalog:
    def __init__(self,library): self.library=library
    def import_dat(self,path,platform):
        path=Path(path)
        if not platform.strip(): raise ValueError('Plataforma obrigatória.')
        if path.stat().st_size>150_000_000: raise ValueError('DAT excede 150 MB.')
        content=path.read_bytes()
        # Aceita DOCTYPE externo habitual do Logiqx, sem buscar DTD. Rejeita entidades internas.
        doctype = re.search(br'<!DOCTYPE[^>]*>',content,re.I)
        if b'<!ENTITY' in content.upper() or doctype and b'[' in doctype.group(0):
            raise ValueError('Entidades XML não são aceitas.')
        root=ET.fromstring(content); source=path.name; rows=[]
        for game in list(root.findall('game'))+list(root.findall('machine')):
            title=game.findtext('description') or game.get('name')
            if not title: continue
            for rom in game.findall('rom'):
                hashes={key:(rom.get(key) or '').lower() for key in ['md5','sha1','crc']}
                for key,length in [('md5',32),('sha1',40),('crc',8)]:
                    if hashes[key] and not re.fullmatch('[0-9a-f]{'+str(length)+'}',hashes[key]): raise ValueError('Hash inválido no DAT.')
                rows.append((source,platform,title,rom.get('name',''),int(rom.get('size')) if rom.get('size') else None,hashes['md5'] or None,hashes['sha1'] or None,hashes['crc'] or None))
        with self.library.sql:
            self.library.sql.execute('DELETE FROM rom_catalog WHERE source=? AND platform=?',(source,platform))
            self.library.sql.executemany('INSERT INTO rom_catalog(source,platform,title,rom_name,size,md5,sha1,crc32) VALUES(?,?,?,?,?,?,?,?)',rows)
        return len(rows)

    def candidates(self,file):
        if not file.get('md5'): return []
        return [dict(row) for row in self.library.sql.execute('SELECT DISTINCT title,platform,source FROM rom_catalog WHERE md5=? AND (size IS NULL OR size=?) AND platform=?',
                   (file['md5'].lower(),file['size'],file['platform']))]
