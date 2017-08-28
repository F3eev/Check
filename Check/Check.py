#!/usr/bin/python
#_*_coding:utf-8_*_
import os,sys
from tools.CheckHttp import *
from tools.CheckSsh import *
from tools.libs import *
from tools.Exception import *

class Check:
    """
    class check 
    """

    sshobj=None

    def __init__(self,
                 awdname,
                 host,
                 httpport=22,
                 filelogpath=os.getcwd()+"\\log.txt"):

        self.host = host
        self.awdname = awdname
        self.httpport = httpport
        self.filelogpath = filelogpath
        self.logfile = open(self.filelogpath, "a+")
        self.result_list=[]

    def CheckHttp(self, httpport, htmlDict, cookie=''):
        """
            input three values  httpport(int) htmlDict(dict) cookie(int default )
            return a tuple like (True,None)/(False,"error {msg}")
        """
        res = CheckHttp(self.host, httpport).Checker(
            htmlDict, cookie='')
        self.__log(res)
        self.__appres(res)
        return res
    def Login(self, sshport, username, password):
        """ 
            input three values sshport(str) username(str) password(str) 
            return a tuple (True,None)/(False,"error {msg}")
        """
        flag=True,None
        self.sshport=int(sshport)
        self.sshusername=username
        self.sshpassword=password
        sshobj= CheckSsh(self.host,self.sshusername,self.sshpassword,self.sshport)
        res=sshobj.Login()
        if res[0]:
            self.sshobj=sshobj
        else:
            self.__log(res)
            flag=res
        self.__appres(res)
        return flag
    def CheckCmd(self,CmdDict):
        """ 
            input three values sshport(str) username(str) password(str)  CmdDict(dict)
            return a tuple (True,None)/(False,"error {msg}")
        """
        self.__islogin()
        result=self.sshobj.Checker(CmdDict)
        self.__log(result) 
        self.__appres(result)
        return result
        
    def exe(self,cmd):
        """
            input a values cmd(str)
            return a tuple (True,res)/(False,None)
        """
        self.__islogin()
        result=self.sshobj.Cmd(cmd)
        return result
        
    def __islogin(self):
        """
            if not login  raise "you must be login"
            else pass
        """
        if not self.sshobj:
            raise Exception("you must be login")
    
    def __log(self, context):
        "input one values context tuple  (True,None)/(False, {error msg})"
        self.logfile.write("%s %s %s  %s  %s \n"%(GetTime(),self.host,self.awdname,str(context[0]),str(context[1])))

    def __appres(self,res):
        
        self.result_list.append(res)

    def get_status(self):
        """return str True,self.host/False,error"""
        status=True,self.host
        for res in self.result_list:
            if False in res:
                status=res
                break
        return status
if __name__ == '__main__':

    awkname = "dayday"
    host = "192.168.6.131"
    httpport = "8082"
    HtmlDict = {
        '/': ['DayDay', '添加日志', '登录'],
        '/index/login/': ['value="登录"', 'username', 'password'],
        '/index/register/': ['返回登陆', 'Username', 'Password', '注册'],
    }
    CmdDict = {
        'ls':[u'11\n'],
    }
    sshport='22'
    cc = Check(awkname, host)
    res = cc.CheckHttp(httpport, HtmlDict)
    cc.Login(sshport,"root",'123456') 
    # cc.CheckCmd(CmdDict)
    print cc.exe("whoami")