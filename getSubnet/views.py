from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from getSubnet.parce import genconfig
import os, tempfile, zipfile
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
import mimetypes


@csrf_exempt
def getSubnet(request):
    errors = []
    form = {}
    if request.POST:

        form['subnet'] = request.POST.get('subnet')
        form['mask'] = request.POST.get('mask')
        form['loopback'] = request.POST.get('loopbask')
        form['location'] = request.POST.get('location')
        iploopback = str(request.POST.get('loopback'))
        ipsubnet = str(request.POST.get('subnet'))
        location = str(request.POST.get('location'))
        type = str(request.POST.get('type'))
        iface = str(request.POST.get('iface'))
        typesecond = str(request.POST.get('typesecond'))
        ifacesecond = str(request.POST.get('ifacesecond'))
        args = str(request.POST.get('args'))
        args2 = str(request.POST.get('args2'))
        argssecond = str(request.POST.get('argssecond'))
        args2second = str(request.POST.get('args2second'))

        tunuser1 = str(request.POST.get('tunuser1'))
        tunpass1 = str(request.POST.get('tunpass1'))
        tungw1 = str(request.POST.get('tungw1'))
        tuncert1 = str(request.POST.get('tuncert1'))

        tunuser2 = str(request.POST.get('tunuser2'))
        tunpass2 = str(request.POST.get('tunpass2'))
        tungw2 = str(request.POST.get('tungw2'))
        tuncert2 = str(request.POST.get('tuncert2'))


        genconfig(iploopback, ipsubnet, location, type, iface, typesecond, ifacesecond, args, args2, argssecond,
                  args2second, tunuser1,tunpass1,tuncert1,tungw1,tunuser2,tunpass2,tuncert2,tungw2)




    return render(request,'getSubnet/base.html', {'errors': errors, 'form':form})


