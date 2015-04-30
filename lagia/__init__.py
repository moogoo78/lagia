#!/usr/bin/env python
# -.- coding: utf-8 -.-

"""
# Lagia

easy spider

depends on requests, bs4


# ChangeLog

## [0.1] new born - 2015-04-30


"""
import requests
from bs4 import BeautifulSoup

class Lagia(object):

    is_file = True
    src = ''
    soup = None

    def __init__(self, url_or_file):

        self._debug('init')
        
        self.src = url_or_file
        self._debug('source: ' + self.src)
        
        if 'http://' in self.src:
            is_file = False

        html = None
        if self.is_file:
            f = open(self.src, 'r')
            html = f.read()
        else:
            r = requests.get(self.src)
            html = r.text
            
        self.soup = BeautifulSoup(html, 'lxml')            


    def _debug(self, s):
        print ('[lagia] %s' % s)

    def download(self, src, tgt):
        r = requests.get(src)        
        out = open(tgt, 'wb')
        out.write(r.content)
        out.close()
        self._debug('download... %s to %s' % (src, tgt))
