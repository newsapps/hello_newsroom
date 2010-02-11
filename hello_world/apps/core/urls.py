from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from core import views

urlpatterns = patterns('',
    url(r'^community_area/(\d+).kml',
        views.comm_area_kml,
    name="comm_area_kml"),
    url(r'',
        views.index,
    name="search"),
)