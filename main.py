#!/usr/bin/env python
# -.- coding: utf-8 -.-

import os
import sys
from lagia import Lagia

def main(url_or_file):

    src = os.path.join(os.getcwd(), url_or_file)
    lagia = Lagia(src)
    
    dirname = url_or_file[:-5]
    try:
        path = os.mkdir(dirname)
    except OSError:
        print 'err mkdir'

    a = 0    
    for i in lagia.soup.select('.a img'):
        a = a + 1
        tgt = os.path.join(dirname, '%02d.jpg'%a)
        lagia.download(i['src'], tgt)
        

if __name__ == '__main__':

    main(sys.argv[1])
