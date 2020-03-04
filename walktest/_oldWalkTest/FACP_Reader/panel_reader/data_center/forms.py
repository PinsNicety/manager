from django import forms
from .models import Test


class TestModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['site_name', 'panel_type', 'device_list', 'alarm_history']
