#!/usr/bin/python
#_*_coding:utf-8_*_

from Check.Check import *

 
obj={
    'awdname':"chinaz",
    'host':'192.168.6.133',
    'httpport':'80',
    'sshport':'22',
    'sshuser':'root',
    'sshpass':'8181ppx',
    'htmlDict':{
        '/index.php': ['MD5', '2decodebeauty',],
        '/index.php?page=phpcom': ['phpcom', 'decodebeauty', 'basiccompress']
    },
    'CmdDict':{
        'ls -l  /var/www/html/logs':[u'total 4\n', u'-rwxr-xr-x 1 www-data www-data 40 Aug 28 15:28 logfile.php\n'],
        'ls /var/www/html/':[u'action.php\n', u'config.php\n', u'error.php\n', u'favicon.ico\n', u'index.php\n', u'library\n', u'logs\n', u'md5.php\n', u'normaliz.php\n', u'phpcom.php\n', u'static\n', u'uploadfile\n', u'views\n']
    },

}

CC=Check(obj['awdname'], obj['host'])
CC.CheckHttp(obj['httpport'], obj['htmlDict'])
CC.Login(obj['sshport'],obj['sshuser'],obj['sshpass'])
CC.CheckCmd(obj['CmdDict'])
print CC.exe("sss")