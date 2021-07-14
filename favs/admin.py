from django.contrib import admin
from . import models

@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):

    """FavList Admin Definition"""
    pass

