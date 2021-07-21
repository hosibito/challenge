from django.urls import path

from . import views as categories_views

app_name = "genres"

urlpatterns = [   
    path('', categories_views.all_categorie, name="categorie_list"),
]