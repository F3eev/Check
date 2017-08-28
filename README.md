
<!-- TOC -->

- [checkv1.0介绍](#checkv10介绍)
- [安装](#安装)
- [引用](#引用)
- [开始使用](#开始使用)
    - [CheckHttp() check web页面，以及功能](#checkhttp-check-web页面以及功能)
    - [Login() ssh远程登陆](#login-ssh远程登陆)
    - [CheckCmd() check linux目录，命令，数据库等](#checkcmd-check-linux目录命令数据库等)
    - [辅助函数](#辅助函数)
    - [get_status() check 结果](#get_status-check-结果)
- [案例](#案例)

<!-- /TOC -->

<a id="markdown-checkv10介绍" name="checkv10介绍"></a>
# checkv1.0介绍

为什么要写这个check第三方库，请往下看

<a id="markdown-安装" name="安装"></a>
# 安装
在项目目录下执行
git clone https://github.com/F3eev/Check.git 
<a id="markdown-引用" name="引用"></a>
# 引用
把你的代码加入到main_check.py 即可

`from Check.Check import *`
<a id="markdown-开始使用" name="开始使用"></a>
# 开始使用
```python

CC=Check(awkname,host) //实例化Check类
```
<a id="markdown-checkhttp-check-web页面以及功能" name="checkhttp-check-web页面以及功能"></a>
## CheckHttp() check web页面，以及功能

```python

httpport=80
htmlDict:{
        '/index.php': ['MD5', '2decodebeauty',],
        '/index.php?page=phpcom': ['phpcom', 'decodebeauty', 'basiccompress']
    },
CC.CheckHttp(httpport, Dicthtml)
//return  a tuple like True,None/False,error message

```
<a id="markdown-login-ssh远程登陆" name="login-ssh远程登陆"></a>
## Login() ssh远程登陆
```python
sshport=22
sshuser='root'
sshpass='******'
CC.Login(sshport,sshuser,sshpass)
//return  a tuple like True,None/False,error message
```

<a id="markdown-checkcmd-check-linux目录命令数据库等" name="checkcmd-check-linux目录命令数据库等"></a>
## CheckCmd() check linux目录，命令，数据库等

```python
CmdDict:{
        'ls -l  /var/www/html/logs':[u'total 4\n', u'-rwxr-xr-x 1 www-data www-data 40 Aug 28 15:28 logfile.php\n'],
        'ls /var/www/html/':[u'action.php\n', u'config.php\n', u'error.php\n', u'favicon.ico\n', u'index.php\n', u'library\n', u'logs\n', u'md5.php\n', u'normaliz.php\n', u'phpcom.php\n', u'static\n', u'uploadfile\n', u'views\n']
    }

CC.CheckCmd(CmdDict)

//return  a tuple like True,None/False,error message
```
<a id="markdown-辅助函数" name="辅助函数"></a>
## 辅助函数
1.CC.exe()这个函数主要帮助你去定义CmdDict变量，以至于准确得使用

```
cmd='whoami'
CC.exe(cmd)
// return a list like (True, [u'root\n'])/(True, [])

```
<a id="markdown-get_status-check-结果" name="get_status-check-结果"></a>
## get_status() check 结果

```
CC.get_status()
// return True,IP
// return False,error message
// 这符合平台得接口规范
```
<a id="markdown-案例" name="案例"></a>
# 案例

```python
#!/usr/bin/python
#_*_coding:utf-8_*_

from Check.Check import *

 
obj={
    'awdname':"***",
    'host':'192.168.6.*',
    'httpport':'80',
    'sshport':'22',
    'sshuser':'root',
    'sshpass':'**',
    'htmlDict':{
        '/index.php': ['**', '***'],
        '/index.php?page=phpcom': ['***']
    },
    'CmdDict':{
        'ls -l  /var/www/html/logs':[u'total 4\n', u'-rwxr-xr-x 1 www-data www-data 40 Aug 28 15:28 test.php\n'],
        
    },

}

CC=Check(obj['awdname'], obj['host'])
CC.CheckHttp(obj['httpport'], obj['htmlDict'])
CC.Login(obj['sshport'],obj['sshuser'],obj['sshpass'])
CC.CheckCmd(obj['CmdDict'])
print CC.get_status()
```


tips:当然因为爱情了，因为今天情人节啊