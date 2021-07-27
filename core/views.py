from django.shortcuts import render

from movies import models as movie_models
from books import models as book_models
from people import models as people_models



def home(request):
    movies_list = movie_models.Movie.objects.all().order_by('-created_at')[0:10]
    books_list = book_models.Book.objects.all().order_by('-created_at')[0:10]
    people_list = people_models.Person.objects.all().order_by('-created_at')[0:10]
    
    return render(request, "core/home.html" , {
        "movies_list": movies_list,
        "books_list": books_list,
        "people_list": people_list,
        })

def search(request):
    return render(request, "core/search.html")
