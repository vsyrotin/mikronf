import re

def genconfig(iploop,iplan,subnetlan):
    file = open('rb450', 'r')
    text = file.read()
    file.close()
    file = open('rb450', 'w')

    file.write(text.replace("iploop", iploop).replace("iplan", iplan).replace("subnetlan", subnetlan))
    file.close


genconfig(iploop="127.0.0.1",iplan="192.168.0.1",subnetlan="24")