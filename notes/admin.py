from django.contrib import admin
from .models import Note, Organization, Site

# Register your models here.
admin.site.register(Note)
admin.site.register(Site)
admin.site.register(Organization)
