"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView

from djangotest.forms import testform
from djangotest.utils import classcontract
from djangotest.views import testView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', testView.get),
    url(r'^test2/', testView.MenuView.as_view()),
    url(r'^test3/', testView.TableView.as_view()),
    # url(r'^test4/', testView.anotherView()),


]
