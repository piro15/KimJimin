from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Idea)
class CustomIdeaAdmin(admin.ModelAdmin):
    pass
