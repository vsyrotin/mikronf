import re

import os
import datetime

def genconfig(iploopback,ipsubnet,mask,location):
    file = open('templateconf', 'r')
    text = file.read()
    file.close()
    name = location+"conf-" + str(datetime.datetime.now().date().year) + "-" + str(datetime.datetime.now().date().month) \
           + "-" + str(datetime.datetime.now().date().day)
    file = open(os.path.join(os.path.expanduser('E:\python\mikronf\generic'), name),'w')

    file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
               .replace("location", location))
    file.close


genconfig("127.0.0.1","192.168.0.1","24","test")
