from django.shortcuts import render

from . import models as books_models

def all_books(request):
    return render(request, "books/book_list.html")
