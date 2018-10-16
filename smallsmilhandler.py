#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.etiq = []
        self.atrib = {}

    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background-color', "")
            self.atrib = {'etiqueta': name, 'width': self.width,
                          'height': self.height,
                          'background-color': self.background_color}
            self.etiq.append(self.atrib)
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.atrib = {'etiqueta': name, 'id': self.id,
                          'top': self.top, 'bottom': self.bottom,
                          'left': self.left, 'right': self.right}
            self.etiq.append(self.atrib)
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.atrib = {'etiqueta': name, 'src': self.src,
                          'region': self.region, 'begin': self.begin,
                          'dur': self.dur}
            self.etiq.append(self.atrib)
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.atrib = {'etiqueta': name, 'src': self.src,
                          'begin': self.begin, 'dur': self.dur}
            self.etiq.append(self.atrib)
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.atrib = {'etiqueta': name, 'src': self.src,
                          'region': self.region}
            self.etiq.append(self.atrib)

    def get_tags(self):

        return self.etiq


if __name__ == "__main__":
    try:
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(sys.argv[1]))
        listafinal = cHandler.get_tags()
        print(listafinal)
    except FileNotFoundError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
