from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Tool)
class CustomToolAdmin(admin.ModelAdmin):
    pass
