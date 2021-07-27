from django.urls import path

from . import views as books_views

app_name = "books"

urlpatterns = [   
    path('', books_views.BooksView.as_view() , name="books"),
    path('<int:pk>/', books_views.BooksDetail.as_view() , name="detail"),
    path('create/', books_views.BooksCreate.as_view() , name="create"),
    path('update/<int:pk>/', books_views.BooksUpdate.as_view() , name="update"),
]