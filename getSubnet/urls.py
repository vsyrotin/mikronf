from django.conf.urls import url
from getSubnet.views import getSubnet, send_file

urlpatterns = [
    url(r'^$', getSubnet, name='getSubnet'),
    url(r'^/opt/mikronf/getSubnet/generic/example.txt', send_file)
]


