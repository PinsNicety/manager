from django import forms
from django.forms.widgets import SelectDateWidget
from djrichtextfield.widgets import RichTextWidget
from datetime import date


class NoteForm(forms.Form):
    new_date = date.today()
    date = forms.DateField(initial=new_date, widget=SelectDateWidget())
    body = forms.CharField(widget=RichTextWidget())