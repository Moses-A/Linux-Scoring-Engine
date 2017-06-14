#!/usr/bin/python2


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

def user_check(user,score):
   jenny = 0
   for line in open('/etc/passwd'):
       if user in line:
           jenny = 1 
   if jenny == 0:
       score = score +1
       points.append('Removed The User '+user)


def main(score,points):
   if not program_check('nmap'):
      score = score+1
      points.append('Removed The Tool Nmap')
   if not program_check('medusa'):
      score = score+1
      points.append('Removed The Tool Medusa')
   user_check('jennylewis',score)
   for point in points:
       print point
   print str(score),"/20 Total Points"


if __name__ == '__main__':
   main(score,points)
