from django.urls import path

from . import views as books_views

app_name = "books"

urlpatterns = [   
    path('', books_views.all_books, name="book_list"),
]