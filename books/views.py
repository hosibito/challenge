from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import EmptyPage, Paginator

from . import models as books_models

def resolve_books(request):

    page = request.GET.get("page", 1)
    book_list = books_models.Book.objects.all()
    paginator = Paginator(book_list, 10, orphans=4)

    try:
        page_obj = paginator.page(int(page))
        return render(request, "books/books.html", {"page_obj" : page_obj})
    except EmptyPage:
        return redirect(reverse("core:home"))