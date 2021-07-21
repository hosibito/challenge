from django.shortcuts import render

from . import models as categories_models

def all_categorie(request):
    return render(request, "categories/categorie_list.html")
