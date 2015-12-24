from django import forms
from django.db import models

# Create your models here.

FIELD_CHOICES = (("forms.charfield", "varchar"), (forms.IntegerField, "int"))





class FormClass(models.Model):
    table_name = models.CharField(max_length=50)
    fields = models.ManyToOneRel

    operation_create = models.BooleanField()
    operation_update = models.BooleanField()
    operation_delete = models.BooleanField()



class FormField(models.Model):
    form = models.OneToOneField(FormClass)
    type = models.CharField(choices=FIELD_CHOICES, max_length=50)

