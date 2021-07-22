from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import EmptyPage, Paginator

from . import models as movies_models

def resolve_movies(request):

    page = request.GET.get("page", 1)
    movie_list = movies_models.Movie.objects.all()
    paginator = Paginator(movie_list, 10, orphans=4)

    try:
        page_obj = paginator.page(int(page))
        return render(request, "movies/movies.html", {"page_obj" : page_obj})
    except EmptyPage:
        return redirect(reverse("core:home"))