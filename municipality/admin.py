from django.contrib import admin
from .models import All,All_Temp
# Register your models here.

@admin.register(All)
class MunicipalityVerified(admin.ModelAdmin):
    pass

@admin.register(All_Temp)
class MunicipalityUnVerified(admin.ModelAdmin):
    pass