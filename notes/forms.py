from django import forms
from django.forms.widgets import SelectDateWidget
from djrichtextfield.widgets import RichTextWidget
from datetime import date


class NoteForm(forms.Form):
    date = forms.DateField(initial=date.today(), widget=SelectDateWidget())
    body = forms.CharField(widget=RichTextWidget())
