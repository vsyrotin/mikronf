from django.conf.urls import url
from getSubnet.views import getSubnet

urlpatterns = [
    url(r'^$', getSubnet, name='getSubnet'),

]
