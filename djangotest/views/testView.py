import django.forms
from django import forms
from django.core.paginator import Paginator
from django.db import connection, connections
from django.db.models import Manager
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.forms import Form
import os

from django.template.loader_tags import register
from django.views import generic
from django.views.generic import ListView, FormView, CreateView, TemplateView
from django.views.generic.list import BaseListView
from djangotest.model import dao

from djangotest.utils import classcontract, modelcreator


def get(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, '../config/form.xml')
    form = modelcreator.create_form('main')

    if (request.method == 'GET'):
        form = form
    else:
        form = form(request.POST)
        if form.is_valid():
            return HttpResponse("YEAH")

        else:
            print(form.errors)
            return HttpResponse(form.errors)
    return render(request, 'formtemplate.html', {'form': form})









def sql_server_view():
    cursor = connections['sqlserver'].cursor()
    print(cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES").fetchall())
    return "JO"



def anotherView():
    cursor = connection.cursor()
    # cursor.execute("CREATE TABLE test(id int, name VARCHAR(50) PRIMARY KEY (id))")
    cursor.execute("INSERT INTO test VALUES (10, 'joo')")
    data = cursor.execute("SELECT * FROM test").fetchall()
    print(data)
    return data
    # print(data)



def get_information_scheme():
    import pymssql
    conn = pymssql.connect(server='192.168.0.114', user='admin', password='admin',
    database='jonathan', as_dict=True)


    cursor = conn.cursor()
    cursor.execute("SELECT COLUMN_NAME , DATA_TYPE  FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'persons'")
    # print(conn)

    for row in cursor.fetchall():
        print(row)
    return render("jo")


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
    template_name = 'menu.html'
    paginate_by = 25
    context_object_name = 'menuItems'

    templateView = TableView()
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, '../config/../pages/main/menu.xml')
    queryset = classcontract.getMenu(file_path)


class MaterialFormView(FormView):
    form_class = modelcreator.create_form('main')
    template_name = 'form.html'

    form_names = form_class.form_names
    print(form_names)

    def form_valid(self, form):
        querystring = 'INSERT INTO testname('
        for i in form.cleaned_data:
            querystring += (" " + i)

        querystring += (") WHERE VALUES(")

        for i in form.cleaned_data:
            querystring +=  str(form.cleaned_data[i]) + ","

        querystring += ")"
        print(querystring)
        return querystring

# queryset = {"jo", "jo"}

class PageView(MaterialFormView):
    template_name = 'page.html'
    table_name = 'test'

    jo = "jooooooo"

    result = dao.select_all('persons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"result" :dao.select_all("persons")})
        return context




