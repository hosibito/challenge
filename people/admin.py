from django.contrib import admin
from . import models

@admin.register(models.Person_Actor, models.Person_Director, models.Person_Writer)
class PersonAdmin(admin.ModelAdmin):

    """Person Admin Definition"""
    plist_display = ("name", "create", "update")
    

