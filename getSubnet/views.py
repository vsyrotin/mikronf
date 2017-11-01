from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getSubnet(request):
    errors = []
    form = {}
    if request.POST:

        form['subnet'] = request.POST.get('subnet')
        form['mask'] = request.POST.get('mask')
        form['loopback'] = request.POST.get('loopbask')
        form['location'] = request.POST.get('location')
        if not form['subnet']:
            errors.append('Enter subnet')
        if '@' not in form['mask']:
            errors.append('Enter mask')
        if not form['loopback']:
            errors.append('Enter loopback')
        if not form['location']:
            errors.append('Enter location')

        if not errors:
            # ... сохранение данных в базу
            return HttpResponse('Done!')
        m = request.POST.get('location')
        print(m)

    return render(request,'getSubnet/base.html', {'errors': errors, 'form':form})