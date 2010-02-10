from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from core import views

urlpatterns = patterns('',
    url(r'',
        views.index,
    name="search"),
)