#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import smallsmilhandler
import json
import urllib.request
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal:

    def __init__(self, teclado):
            parser = make_parser()
            cHandler = smallsmilhandler.SmallSMILHandler()
            parser.setContentHandler(cHandler)
            parser.parse(open(teclado))
            self.listafinal = cHandler.get_tags()

    def __str__(self):
        for frase in self.listafinal:
            for clave, valor in frase.items():
                if clave == 'etiqueta':
                    p = valor
                if clave == 'src':
                    valor = valor.split('/')[-1]
                if valor != "" and clave != 'etiqueta':
                    p += '\t' + clave + "=" + "'" + valor + "'"
            print(p)

    def to_json(self, teclado, archivojson=''):
        if archivojson == '':
            archivojson = teclado.replace('.smil', '.json')
        with open(archivojson, 'w') as jsonfile:
            json.dump(self.listafinal, jsonfile, indent=4)

    def do_local(self):
        for frase in self.listafinal:
            for clave, valor in frase.items():
                if clave == 'src':
                    url = valor
                    if url.startswith('http'):
                        archivo = url.split('/')[-1]
                        urllib.request.urlretrieve(url, archivo)

if __name__ == "__main__":
    try:
        teclado = sys.argv[1]
        karaoke = KaraokeLocal(teclado)
    except FileNotFoundError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    karaoke.to_json(teclado)
    karaoke.do_local()
    karaoke.to_json(teclado, 'local.json')
    karaoke.__str__()
