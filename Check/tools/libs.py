#!/usr/bin/python
#_*_coding:utf-8_*_

import socket
import sys
import datetime


def CheckPort(host, port, timeout=2):
    '''
    input three values host(str) port(str or int) timout(int),return a tuple like (False, 'ip localhost CheckPort 22  is Error')
    '''
    port = int(port)
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True, None
    except:
        return False, '%s CheckPort %d  is Error' % (host, port)

def GetTime():
    """ return now time %Y-%m-%d %H:%M:%S """
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')  



if __name__ == '__main__':
    print GetTime()
    print CheckPort('192.168.75.180', 8081)
    help(GetTime)