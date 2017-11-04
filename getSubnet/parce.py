import re

import os
import datetime
import getSubnet

# call like this genconfig("127.0.0.1","192.168.0.1","24","test")
def genconfig(iploopback,ipsubnet,location,type,iface,typesecond,ifacesecond,args,args2,argssecond,args2second):
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
    file = open(os.path.join(os.path.expanduser('E:\python\mikronf\generic'), name),'w')

    if type == "dhcp" and typesecond == "dhcp":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("dhcpiface", iface).replace("dhcpiface2",ifacesecond)
                   .replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "dhcp" and typesecond == "static":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("dhcpiface", iface).replace("ifacesecond", ifacesecond).replace("ipaddrpr2",argssecond)
                   .replace("gataweypr2", args2second).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "dhcp" and typesecond == "pppoe":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("dhcpiface", iface).replace("pppoeiface2", ifacesecond).replace("pppoeusernamepr2",argssecond)
                   .replace("pppoepasswordpr2", args2second).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))
    ####################################################################################################################

    if type == "static" and typesecond == "dhcp":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
               .replace("location", location).replace("iface", iface).replace("dhcpiface2",ifacesecond).replace("ipaddrpr1",args)
                   .replace("gataweypr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "static" and typesecond == "static":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("iface", iface)
                   .replace("typesecond", typesecond).replace("ipaddrpr2",argssecond)
                   .replace("gataweypr2", args2second).replace("ipaddrpr1",args)
                   .replace("gataweypr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "static" and typesecond == "pppoe":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("iface", iface)
                   .replace("pppoeiface2", ifacesecond).replace("pppoeusernamepr2",argssecond)
                   .replace("pppoepasswordpr2", args2second).replace("ipaddrpr1",args)
                   .replace("gataweypr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))
    #####################################################################################################################

    if type == "pppoe" and typesecond == "dhcp":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
               .replace("location", location).replace("pppoeiface1", iface)
                   .replace("dhcpiface",ifacesecond).replace("pppoeusernamepr1",args)
                   .replace("pppoepasswordpr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "pppoe" and typesecond == "static":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("pppoeiface1", iface)
                   .replace("iface", ifacesecond).replace("ipaddrpr2",argssecond)
                   .replace("gataweypr2", args2second).replace("pppoeusernamepr1",args)
                   .replace("pppoepasswordpr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))

    if type == "pppoe" and typesecond == "pppoe":
        file.write(text.replace("iploopback", iploopback).replace("ipsubnet", ipsubnet).replace("mask", mask)
                   .replace("location", location).replace("pppoeiface1", iface)
                   .replace("pppoeiface2", ifacesecond).replace("pppoeusernamepr2",argssecond)
                   .replace("pppoepasswordpr2", args2second).replace("pppoeusernamepr1",args)
                   .replace("pppoepasswordpr1", args2).replace("ipgw",gw).replace("ipStart",startrange).replace("ipEnd",endrange))


    file.close

    link = open("base.html", 'r')
    linkbuild = link.read()
    link.close()

    link = open("base.html", 'w')

    link.write(linkbuild.replace("link",name))

    link.close()

