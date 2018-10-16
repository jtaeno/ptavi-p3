#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

if __name__ == "__main__":
    try:
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(sys.argv[1]))
        listafinal = cHandler.get_tags()
        p = ''
        for frase in listafinal:
            for clave, valor in frase.items():
                if clave == 'etiqueta':
                    p = valor
                if valor != "" and clave != 'etiqueta':
                    p += '\t' + clave + "=" + "'" + valor + "'"
            print(p)
    except FileNotFoundError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
