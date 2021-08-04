from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

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

class SearchView(View):    
    def get(self, request):
        search = request.GET.get("search")     
        if search:
            movie_reselt = movie_models.Movie.objects.filter(title__startswith=search)
            book_reselt = book_models.Book.objects.filter(title__startswith=search)
            people_reselt = people_models.Person.objects.filter(name__startswith=search)
        else:
            return redirect(reverse("core:home"))

        return render(request, "core/search.html" ,{"movie_reselt":movie_reselt, "book_reselt":book_reselt, "people_reselt":people_reselt})
