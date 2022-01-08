from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    text = forms.CharField(max_length=2000, required=True, label="Text",
                           widget=widgets.Textarea(attrs={"rows":5 , "cols":50}))