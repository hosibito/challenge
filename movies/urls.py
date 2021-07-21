from django.urls import path

from . import views as movies_views

app_name = "movies"

urlpatterns = [   
    path('', movies_views.all_movies, name="movie_list"),
]