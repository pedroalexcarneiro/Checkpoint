"""Gera ICO multirresolução a partir da mesma identidade vetorial da interface."""
import argparse
from pathlib import Path
import struct
from PySide6.QtCore import QBuffer,QIODevice
from PySide6.QtGui import QGuiApplication
from checkpoint.branding import app_icon
from checkpoint.theme import get_theme


def main():
    parser=argparse.ArgumentParser();parser.add_argument('output',type=Path);args=parser.parse_args()
    app=QGuiApplication.instance() or QGuiApplication([])
    icon=app_icon(get_theme('green'));payloads=[]
    sizes=(16,24,32,48,64,128,256)
    for size in sizes:
        buffer=QBuffer();buffer.open(QIODevice.WriteOnly)
        if not icon.pixmap(size,size).save(buffer,'PNG'):raise RuntimeError('Falha ao gerar ícone.')
        payloads.append(bytes(buffer.data()))
    offset=6+16*len(sizes);entries=[]
    for size,data in zip(sizes,payloads):
        entries.append(struct.pack('<BBBBHHII',size%256,size%256,0,0,1,32,len(data),offset));offset+=len(data)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(struct.pack('<HHH',0,1,len(sizes))+b''.join(entries)+b''.join(payloads))


if __name__=='__main__':main()
