import django.forms
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.forms import Form
import os

from django.views import generic
from django.views.generic import ListView
from django.views.generic.list import BaseListView

from djangotest.utils import classcontract


def get(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, '../config/form.xml')
    form = classcontract.getForms(file_path)

    if(request.method == 'GET'):

        form = form
    else:
        form = form(request.POST)
        if form.is_valid():
            return HttpResponse("YEAH")
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    return render(request, 'formtemplate.html', {'form': form, })



class MenuView(ListView):
    template_name = 'menuTemplate.html'
    paginate_by = 25
    context_object_name = 'menuItems'

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, '../config/menu.xml')
    queryset = classcontract.getMenu(file_path)



    # queryset = {"jo", "jo"}


