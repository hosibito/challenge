from django.shortcuts import render

from . import models as movies_models

def all_movies(request):
    return render(request, "movies/movie_list.html")
