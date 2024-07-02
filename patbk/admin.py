from django.contrib import admin
from patbk.models import patient,docter,hospital
# Register your models here.
admin.site.register(patient)
admin.site.register(docter)
admin.site.register(hospital)