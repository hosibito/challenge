from django.urls import path

from . import views as books_views

app_name = "books"

urlpatterns = [   
    path('', books_views.resolve_books, name="books"),
]