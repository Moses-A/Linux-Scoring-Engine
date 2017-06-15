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
      pro = subprocess.Popen("cat " +file, shell=True, stdout=subprocess.PIPE)
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
   user_check('jennylewis')
   user_check('moses')
   group_check('juan')
   user_passwd('cyber', '$6$FicC')
   user_passwd('jimmy', '$6$QMoj')
   user_passwd('ben',   '$6$SkT') 
   malware_check('/home/cyber/.virus.py')
   malware_check('/root/Firewall/setup.py')
   firewall_check()
   update_programs('General','http://us.archive.ubuntu.com/ubuntu')
   update_programs('Security','http://security.ubuntu.com/ubuntu')
   password_complexity()
   password_history()
   account_policy()
   guest_account('/etc/lightdm/lightdm.conf')
   apache_security('/etc/apache2/conf-available/myconf.conf')
   ssh_security()
   for point in points:
       print point
   print str(score),"/20 Total Points"


if __name__ == '__main__':
   main()


