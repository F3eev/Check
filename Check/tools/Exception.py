#!/usr/bin/python
#_*_coding:utf-8_*_


class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message 