#!/usr/bin/python
#_*_coding:utf-8_*_

import paramiko
from libs import CheckPort


class CheckSsh():
    """ CheckSsh """
    def __init__(self,host,username,passsowrd,port=22):
        """ 
            (host str,username str,passsowrd str ,port=22 int)  
        """
        self.host=host
        self.username=username
        self.passsowrd=passsowrd
        self.port=port
        self.Status=True,None
    
    def Login(self):
        """
            return a tuple like (True,None)/(False,"{host} {port} {error}")
        """
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host,self.port,self.username,self.passsowrd,timeout=2)
            return (True,None)
        except Exception,e:
            
            return (False,"%s %s %s"%(self.host,self.username,e))
            
    def Cmd(self,cmd):
        """ 
            input one values cmd(str)
            return a tuple like (True,result)/(False,"{cmd} error")
        """
        is_login=self.Login()
        if not is_login[0]:
            return is_login
        else:
            try:
                stdin, stdout, stderr = self.ssh.exec_command(cmd)
                out = stdout.readlines()
                # print out
                return (True,out)
            except Exception,e:
                return False,"%s cmd error"%(cmd)

    def Checker(self,cmdDict):
        """
            input one values cmdDict(dict)
            return a tuple like (True,out)/(False," {cmd} cmd result not find {cmdDict}"
        """
        for (cmd,content) in cmdDict.items():
            out=self.Cmd(cmd)
            if out[0] == 0:return out
            else:
                for c in content:
                    if c not in out[1]:
                        return (False,'%s cmd result not find %s'%(cmd,c))
        return True,None


if __name__ =='__main__':
    CmdDict = {
        'ls':[u'11\n'],
    }
    sscmd=CheckSsh('192.168.6.131','root','123456')
    print sscmd.Checker(CmdDict)


