#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Creates 3 column layout on A4 paper and save it under 3columnA4.sla filename"""

import sys

try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

margins = (50, 50, 50, 50)
size = (612, 792)

def main():
    if newDoc(PAPER_A4, margins, LANDSCAPE, 1, UNIT_POINTS, NOFACINGPAGES, FIRSTPAGELEFT):
        a = createText(50, 50, 230, 512)
        setTextAlignment(1,a)
        setText("Column A", a)
        setFontSize(12, a)
        b = createText(280, 50, 230, 512)
        setTextAlignment(1,b)
        setText("Column B", b)
        setFontSize(12, b)
        c = createText(510, 50, 230, 512)
        setTextAlignment(1,b)
        setText("Column C", c)
        setFontSize(12, c)
        saveDocAs("3columnA4.sla")
        closeDoc()

if __name__ == '__main__':
    main()
