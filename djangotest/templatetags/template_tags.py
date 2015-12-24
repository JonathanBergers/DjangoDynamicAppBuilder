from django import template
from django.db import connection
from django.template.loader import render_to_string
from django.views.generic import ListView
from djangotest.model import dao
from djangotest.utils import xmlparser

__author__ = 'jonathan'

register = template.Library()


@register.inclusion_tag('table.html', name="render_table")
def get_table_view(table_name):
    return dao.select_all(table_name)


# @register.inclusion_tag('menu.html', name="render_table")
def get_menu_view(page):
    return xmlparser.parse_menu(page)





#
# class TableView(ListView):
#     table_name = None
#     queryset = dao.select_all(table_name)
#     paginate_by = 10
#     template_name = 'table.html'
#
#
# def get_table(table_name):
#     return dao.select_all(table_name)
