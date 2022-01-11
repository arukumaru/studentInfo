from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<Roll_no>[0-9]+)$', views.detail, name='detail'),
]

