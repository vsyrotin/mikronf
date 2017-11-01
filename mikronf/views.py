from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def index(request):
    return render_to_response('index.html')

