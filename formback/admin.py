from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WardForm, WardFormTemp

# Register your models here.
"""
@admin.register(Form)
class ShopAdmin(OSMGeoAdmin):
	list_display = ('PalikaName','Province','District','location')
"""
	
@admin.register(WardForm)
class TryFormAdmin(OSMGeoAdmin):
	pass

@admin.register(WardFormTemp)
class FormTempAdmin(OSMGeoAdmin):
	pass

