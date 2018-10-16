import sys
import smallsmilhandler
import json
import urllib.request
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

        archivojson = sys.argv[1].replace('.smil', '.json')
        with open(archivojson, 'w') as jsonfile:
            json.dump(listafinal, jsonfile, indent=1)

        for frase in listafinal:
            for clave, valor in frase.items():
                if clave == 'src':
                    url = valor
                    if url.startswith('http'):
                        archivo = url.split('/')[-1]
                        urllib.request.urlretrieve(url, archivo)
                        valor = archivo
                if clave == 'etiqueta':
                    p = valor
                if valor != "" and clave != 'etiqueta':
                    p += '\t' + clave + "=" + "'" + valor + "'"
            print(p)
    except FileNotFoundError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
