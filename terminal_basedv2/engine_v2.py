#!/usr/bin/python2
# Author is Moses Arocha


import os
import pwd
import re
import socket
import subprocess
import sys


score = 0
points = []


def program_check(program):
   pro = subprocess.Popen("dpkg -l | grep " +program, shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.stdout.close()
   pro.wait()
   if display:
       return True
   else:
       return False


def waf_check():
   global score
   if os.path.isfile("/etc/modsecurity/modsecurity.conf-recommended"):
       pro = subprocess.Popen("cat /etc/modsecurity/modsecurity.conf-recommended", shell=True, stdout=subprocess.PIPE)
       display = pro.stdout.read()
       pro.stdout.close()
       pro.wait()
       if "SecRequestBodyAccess Off" in display:
           score = score+1
           points.append("Added WAF Protection to Apache Server")


def update_programs(topic,respository):
   global score
   pro = subprocess.Popen("cat /etc/apt/sources.list", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.stdout.close()
   pro.wait()
   if respository in display:
      score = score+1
      points.append(topic+" Respository Added To Debian Package Lists")


def user_passwd(user,hash):
   global score
   pro = subprocess.Popen("cat /etc/shadow | grep "+user, shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.stdout.close()
   pro.wait()
   if hash not in display:
      score = score+1
      points.append('Changed '+user+' Password')


def firewall_check():
   global score
   pro = subprocess.Popen("ufw status", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.stdout.close()
   pro.wait()
   if ' active' in display:
      score = score+1
      points.append('Enabled The Firewall')


def group_check(user):
   global score
   pro = subprocess.Popen("cat /etc/group | grep sudo", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if user in display:
      score = score+1
      points.append('Added '+user+' To The Sudo Group')


def password_complexity():
   global score
   pro = subprocess.Popen("cat /etc/pam.d/common-password", shell=True, stdout=subprocess.PIPE)
   display=pro.stdout.read()
   pro.wait()
   if "remember=5" in display:
     score = score+1
     points.append('Added Password History')
   if "minlen=8" in display:
     score = score+1
     points.append('Enforced Password Length')
   if "ucredit" and "lcredit" and "dcredit" and "ocredit" in display:
     score = score+1
     points.append('Added Password Complexity Standards')


def password_history():
   global score
   pro = subprocess.Popen("cat /etc/login.defs", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if "PASS_MAX_DAYS " and "PASS_MIN_DAYS " and "PASS_WARN_AGE " in display:
     score = score+1
     points.append('Added Password History Standards')


def account_policy():
   global score
   pro = subprocess.Popen("cat /etc/pam.d/common-auth", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if "deny=" and "unlock_time=" in display:
      score = score+1
      points.append('Set Account Policy Standards') 


def guest_account(file_path):
   global score
   if os.path.isfile(file_path):
     pro = subprocess.Popen("cat "+file_path, shell=True, stdout=subprocess.PIPE)
     display = pro.stdout.read()
     pro.wait()
     if "allow-guest=false" in display:
        score = score+1
        points.append('Disabled Guest Account')


def apache_security(file):
   global score
   if os.path.isfile(file):
      pro = subprocess.Popen("cat /etc/apache2/conf-available/security.conf" +file, shell=True, stdout=subprocess.PIPE)
      display = pro.stdout.read()
      pro.wait()
      if "ServerSignature" and "ServerTokens" in display:
          score = score+1
          points.append('Secured Apache Web Server')


def ssh_security():
   global score
   pro = subprocess.Popen("cat /etc/ssh/sshd_config | grep PermitRootLogin", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if "no" in display:
      score = score+1
      points.append('Disabled Root Login for SSH')
   subpro = subprocess.Popen("cat /etc/ssh/sshd_config", shell=True, stdout=subprocess.PIPE)
   subdisplay = subpro.stdout.read()
   subpro.wait()
   if "AllowUsers" in subdisplay:
      score = score+1
      points.append('Secured SSH User Login')

def advance_ssh(port):
   global score
   pro = subprocess.Popen("cat /etc/ssh/sshd_config | grep Port", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if port not in display:
     score = score+1
     points.append('Secured SSH Server Port')

def samba_security():
   global score
   pro = subprocess.Popen("cat /etc/samba/smb.conf", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if "guest ok = no" in display:
      score = score+1
      points.append('Secured Samba Server')

def php_security():
   global score
   pro = subprocess.Popen("cat /etc/php/7.0/apache2/php.ini | grep expose_php", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if "Off" in display:
     score = score+1
     points.append('Secured PHP Version')


def mysql_security(hash):
   global score
   pro = subprocess.Popen("cat /etc/mysql/debian.cnf | grep password", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if hash not in display:
      score = score+1
      points.append('Changed MySQL Root Password')
    


def malware_check(file_path):
   global score
   if not os.path.isfile(file_path):
      score = score+1
      points.append('Removed Harmful File')


def user_check(user):
   global score
   jenny = 0
   for line in open('/etc/passwd'):
       if user in line:
           jenny = 1
   if jenny == 0:
       score = score+1
       points.append('Removed The User '+user)


def main():
   global score
   global points
   if not program_check('nmap'):
      score = score+1
      points.append('Removed The Tool Nmap')
   if not program_check('medusa'):
      score = score+1
      points.append('Removed The Tool Medusa')
   if not program_check('wireshark'):
      score = score+1
      points.append('Removed The Tool Wireshark')
   user_check('kurt')
   user_check('moses')
   group_check('juan')
   user_passwd('cyber', '$1$tsJ$')
   user_passwd('delgado', '$6$iPs56')
   user_passwd('krist', '$6$tfF8') 
   malware_check('/home/cyber/Desktop/all_apologies.mp3')
   malware_check('/home/cyber/Music/smells_like_teen_spirit.mp3')
   firewall_check()
   update_programs('General','http://us.archive.ubuntu.com/ubuntu')
   update_programs('Security','http://security.ubuntu.com/ubuntu')
   password_complexity()
   password_history()
   account_policy()
   guest_account('/usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf')
   apache_security('/etc/apache2/conf-available/myconf.conf')
   ssh_security()
   php_security()
   samba_security()
   waf_check()
   mysql_security('R4NatSMf1zNK148p')
   advance_ssh('22')
   for point in points:
       print point
   print str(score),"/28 Total Points"


if __name__ == '__main__':
    main()
