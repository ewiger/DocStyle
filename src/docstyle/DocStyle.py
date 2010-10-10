#!/usr/bin/env python2.6
# encoding: utf-8
'''
DocStyle module requires antlr3 runtime. It can be downloaded at
http://www.antlr.org/download/Python

'''
from antlr3 import *
from antlr3.tree import CommonTree
from DocStyleLexer import DocStyleLexer
from DocStyleParser import DocStyleParser


class DocStyle:

    def __init__(self, doc_string):
        self.doc_string = doc_string

    def parse(self):
        '''
        Parse doc string using generated lexer and parser.
        
        @return: None
        '''
        char_stream = ANTLRStringStream(self.doc_string)
        lexer = DocStyleLexer(char_stream)
        tokens = CommonTokenStream(lexer)
        parser = DocStyleParser(tokens)
        rule = parser.docString()

if __name__ == '__main__':
    doc_string = DocStyle.parse.__doc__
    #doc_string = '@taggy: bunny'
    doc_string = unicode(doc_string)
    print doc_string
    DocStyle(doc_string).parse()
