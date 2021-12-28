from django.contrib import admin
from . models import Person, Desc, Offence, Report

admin.site.register(Person)
admin.site.register(Desc)
admin.site.register(Offence)
admin.site.register(Report)
