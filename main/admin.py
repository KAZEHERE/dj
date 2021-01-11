#from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


admin.site.register(Abonent)
admin.site.register(Street)
admin.site.register(Disrepair)
admin.site.register(Pricing)
admin.site.register(Request)
admin.site.register(PaySum)