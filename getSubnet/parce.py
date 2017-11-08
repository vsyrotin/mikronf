import re

import os
import datetime
import getSubnet

# call like this genconfig("127.0.0.1","192.168.0.1","24","test")
def genconfig(iploopback,ipsubnet,location,type,iface,typesecond,ifacesecond,args,args2,argssecond,args2second,
              tunuser1,tunpass1,tuncert1,tungw1,tunuser2,tunpass2,tuncert2,tungw2):
    # static
    addAddress = "/ip address add address=%s interface=%s" % (args, iface)
    addAddress2 = "/ip address add address=%s interface=%s" % (args2, ifacesecond)
    addGw = "/ip route add dst-address=0.0.0.0/0 gateway=%s" % args2
    addGW2 = "/ip route add dst-address=0.0.0.0/0 gateway=%s" % args2second

    #dhcp
    addDhcp1 = "/ip dhcp-client add interface=%s add-default-route=yes use-peer-dns=no use-peer-ntp=no" % iface
    addDhcp2 = "/ip dhcp-client add interface=%s add-default-route=yes use-peer-dns=no use-peer-ntp=no" % ifacesecond

    #pppoe
    addpppoe1 = "/interface pppoe-client add interface=%s disabled=yes user=%s " \
                "password=%s profile=default-encryption add-default-route=yes " \
                "dial-on-demand=no use-peer-dns=no" % (iface, args, args2)
    addpppoe2 = "/interface pppoe-client add interface=%s disabled=yes user=%s " \
                "password=%s profile=default-encryption add-default-route=yes " \
                "dial-on-demand=no use-peer-dns=no" % (ifacesecond,argssecond,args2second)
    addGwPPPOE = "/ip route add dst-address=0.0.0.0/0 gateway=%s" % iface
    addGW2PPPOE = "/ip route add dst-address=0.0.0.0/0 gateway=%s" % ifacesecond


    mask = "26"
    print(ipsubnet)
    firstoct = (str(ipsubnet).split('.')[0])
    twooct = (str(ipsubnet).split('.')[1])
    threeoct = (str(ipsubnet).split('.')[-2])
    lastoct = (str(ipsubnet).split('.')[-1])

    gw = (firstoct + "." + twooct + '.' + threeoct + "." + str(int(lastoct) + 1))

    startrange = (firstoct + "." + twooct + '.' + threeoct + "." + str(int(lastoct) + 2))
    endrange = (firstoct + "." + twooct + '.' + threeoct + "." + str(int(lastoct) + 62))

    file = open("templateconf", 'r')
    text = file.read()
    file.close()
    name = location+"conf-" + str(datetime.datetime.now().date().year) + "-" + str(datetime.datetime.now().date().month) \
           + "-" + str(datetime.datetime.now().date().day)
    file = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name),'w')

    file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("ipStart",startrange).replace("ipEnd",endrange)
               .replace("tunuser1", tunuser1).replace("tunuser2", tunuser2).replace("tunpass1",tunpass1)
               .replace("tunpass2", tunpass2).replace("tungw1", tungw1).replace("tungw2", tungw2)
               .replace("tuncert1", tuncert1).replace("tuncert2", tuncert2))

    file.close

    if type == "static" and typesecond == "static":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addAddress + '\n' + addAddress2 + '\n' + addGw + '\n' + addGW2)
        prov.close()

    if type == "static" and typesecond == "dhcp":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addAddress + '\n' + addGw + '\n' + addDhcp2)
        prov.close()

    if type == "static" and typesecond == "pppoe":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addAddress + '\n' + addGw + '\n' + addpppoe2 + '\n' + addGW2PPPOE)
        prov.close()

    if type == "dhcp" and typesecond == "static":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addAddress2 + '\n' + addGW2 + '\n' + addDhcp1)
        prov.close()

    if type == "dhcp" and typesecond == "pppoe":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addDhcp1 + '\n' + addpppoe2 + '\n' + addGW2PPPOE)
        prov.close()

    if type == "dhcp" and typesecond == "dhcp":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addDhcp1 + '\n' + addDhcp2)
        prov.close()

    if type == "pppoe" and typesecond == "static":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addpppoe1 + '\n' + addGwPPPOE + '\n' + addAddress2 + '\n' + addGW2)
        prov.close()

    if type == "pppoe" and typesecond == "pppoe":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addpppoe1 + '\n' + addGwPPPOE + '\n' + addpppoe2 + '\n' + addGW2PPPOE)
        prov.close()

    if type == "pppoe" and typesecond == "dhcp":
        prov = open(os.path.join(os.path.expanduser('/opt/mikronf/getSubnet/generic'), name), 'a')
        prov.write('\n' + addpppoe1 + '\n' + addGwPPPOE + '\n' + addDhcp2)
        prov.close()

    path = "/opt/mikronf/getSubnet/generic/" + name
    os.system("cp %s /opt/mikronf/mkconf" % path)