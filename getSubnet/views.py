from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from getSubnet.parce import genconfig


@csrf_exempt
def getSubnet(request):
    errors = []
    form = {}
    if request.POST:

        form['subnet'] = request.POST.get('subnet')
        form['mask'] = request.POST.get('mask')
        form['loopback'] = request.POST.get('loopbask')
        form['location'] = request.POST.get('location')
        iploopback = request.POST.get('loopback')
        ipsubnet = request.POST.get('subnet')
        location = request.POST.get('location')
        type = request.POST.get('type')
        iface = request.POST.get('iface')
        typesecond = request.POST.get('typesecond')
        ifacesecond = request.POST.get('ifacesecond')
        args = request.POST.get('args')
        args2 = request.POST.get('args2')
        argssecond = request.POST.get('argssecond')
        args2second = request.POST.get('args2second')

        genconfig(iploopback, ipsubnet, location, type, iface, typesecond, ifacesecond, args, args2, argssecond, args2second)




    return render(request,'getSubnet/base.html', {'errors': errors, 'form':form})