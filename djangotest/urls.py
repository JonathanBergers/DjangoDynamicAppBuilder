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
from djangotest import forms
from djangotest.utils import modelcreator

from djangotest.views import testView
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(frontend_urls)),
    # url(r'^test/', testView.get_information_scheme()),
    url(r'^test2/', testView.MenuView.as_view()),
    url(r'^test3/', testView.TableView.as_view()),
    url(r'^test4/', modelcreator.create_form),
    url(r'^test5/', testView.MaterialFormView.as_view()),
     url(r'^test6/', testView.PageView.as_view(table_name="persons")),


]
