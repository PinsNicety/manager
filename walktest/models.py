from django.db import models
from notes.models import Site

def set_choices(sites):
    choices = []
    for site in sites:
        choices.append((site.name, site.name))
    return choices

# Create your models here.
class WalkTest(models.Model):
    PANEL_TYPES = (
        ('320', '320'),
        ('640', '640'),
        ('3030', '3030')
    )
    device_list = models.FileField(upload_to='walktest/')
    test_history = models.FileField(upload_to='walktest/')
    site = models.CharField(max_length=200, choices=set_choices(Site.objects.all()))
    panel = models.CharField(max_length=200, choices=PANEL_TYPES)
