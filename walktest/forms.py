from django import forms
from .models import WalkTest

class TestForm(forms.ModelForm):
    class Meta:
        model = WalkTest
        fields = ('device_list', 'test_history', 'site_name', 'panel')
