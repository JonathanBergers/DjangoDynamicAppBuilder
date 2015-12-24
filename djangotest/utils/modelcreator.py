import os
from django.contrib import admin
from django import forms
from django.shortcuts import render
from material import Layout, Row
import xmltodict

__author__ = 'jonathan'






msql_mapping_dict = {}

form_mapping_dict = {
    "int": forms.IntegerField,
    "varchar": forms.CharField,
    "date": forms.DateField,
    "datetime": forms.DateTimeField,
    "textinput": forms.TextInput,
    "textarea": forms.Textarea,
    "time": forms.TimeField,
    "decimal": forms.DecimalField,
    "email": forms.EmailField
}


page = 'main'


def create_form(page):
    location = os.getcwd() + '/djangotest/pages/' + page + '/table.xml'
    with open(location, 'r') as menu_file:
        parsed = xmltodict.parse(menu_file.read())

    form_dict = parsed["form"]
    input_dict = form_dict["input"]

    database_dict = form_dict["database"]


    table_name = database_dict["table"]

    form_attrs = {}
    for i in input_dict:
        var_name = i["label"]
        var_type = i["type"]
        mapped_type = form_mapping_dict[var_type]
        form_attrs[var_name] = mapped_type()


    attr_names = [i for i in form_attrs]


    layout = Layout(Row(*[i for i in form_attrs]))
    form_attrs["layout"] = layout
    form_attrs["form_names"] = attr_names
    print(layout)
    # print(model_attr)

    tabel_form = type("DynamicForm", (forms.Form,), form_attrs)
    return tabel_form





