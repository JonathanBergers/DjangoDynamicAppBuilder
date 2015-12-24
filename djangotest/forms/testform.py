from django import forms
from material import LayoutMixin, Inline
from djangotest.models import FormField


class TestForm(forms.Form):
    textField = forms.CharField(100)
    emailField = forms.EmailField()


class ItemInLine(Inline):
    model = FormField


class FormForm(LayoutMixin):
    Inline("Joo", ItemInLine)

