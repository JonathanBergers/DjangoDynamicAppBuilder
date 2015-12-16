from django import forms

class TestForm(forms.Form):
    textField = forms.CharField(100)
    emailField = forms.EmailField()




