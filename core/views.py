from django.shortcuts import render


def all_movies_and_books(request):
    return render(request, "core/home.html")


def search(request):
    return render(request, "core/search.html")
