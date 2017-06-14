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

def user_check():
   for line in open('/etc/passwd'):
       if 'jennylewis' in line:
           jennylewis = True
       if not jennylewis:
           score = score +1
           points.append('Removed The User Jenny Lewis')


def main(score,points):
   if not program_check('nmap'):
      score = score+1
      points.append('Removed The Tool Nmap')
   user_check()
   for point in points:
       print point
   print str(score),"/20 Total Points"


if __name__ == '__main__':
   main(score,points)

