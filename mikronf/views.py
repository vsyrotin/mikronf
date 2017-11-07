from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.conf import settings
import mimetypes



def index(request):
    return render_to_response('index.html')

def send_file(request):


  filename     = "/opt/mikronf/mkconf" # Select your file here.
  download_name ="mkconf"
  wrapper      = FileWrapper(open(filename))
  content_type = mimetypes.guess_type(filename)[0]
  response     = HttpResponse(wrapper,content_type=content_type)
  response['Content-Length']      = os.path.getsize(filename)
  response['Content-Disposition'] = "attachment; filename=%s"%download_name
  return response


