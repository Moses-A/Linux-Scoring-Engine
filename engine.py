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


def group_check(user):
   pro = subprocess.Popen("cat /etc/group | grep sudo", shell=True, stdout=subprocess.PIPE)
   display = pro.stdout.read()
   pro.wait()
   if user in display:
      global score
      score = score+1
      points.append('Added '+user+' To The Sudo Group')


def user_check(user):
   jenny = 0
   for line in open('/etc/passwd'):
       if user in line:
           jenny = 1
   if jenny == 0:
       global score
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
   for point in points:
       print point
   print str(score),"/20 Total Points"


if __name__ == '__main__':
   main()


