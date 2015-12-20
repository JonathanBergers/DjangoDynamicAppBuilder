import django.forms
from django import forms
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Manager
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.forms import Form
import os

from django.template.loader_tags import register
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




def anotherView():
    cursor = connection.cursor()
    # cursor.execute("CREATE TABLE test(id int, name VARCHAR(50) PRIMARY KEY (id))")
    cursor.execute("INSERT INTO test VALUES (10, 'joo')")
    data = cursor.execute("SELECT * FROM test").fetchall()
    print(data)
    return data
    # print(data)




def show_table(tableName):
    queryString = "SELECT * FROM " + (tableName)
    print(queryString)
    cursor = connection.cursor()

    cursor.execute(queryString)
    result = dictfetchall(cursor)
    return result

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@register.inclusion_tag('table.html', name='show_table')
class TableView(ListView):
    context_object_name = 'rows'
    queryset = show_table('test')
    paginate_by = 10
    template_name = 'table.html'


class MenuView(ListView):
    template_name = 'menuTemplate.html'
    paginate_by = 25
    context_object_name = 'menuItems'

    templateView = TableView()
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, '../config/../pages/main/menu.xml')
    queryset = classcontract.getMenu(file_path)




# queryset = {"jo", "jo"}


