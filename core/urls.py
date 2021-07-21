from django.urls import path

from core import views as core_views

app_name = "core"

urlpatterns = [   
    path('', core_views.all_movies_and_books, name="home"),    
    path("search/", core_views.search, name="search"),
]