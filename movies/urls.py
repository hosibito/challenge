from django.urls import path

from . import views as movies_view

app_name="movies"

urlpatterns = [
  path("", movies_view.MoviesView.as_view() , name="movies"),
  path('<int:pk>/', movies_view.MoviesDetail.as_view() , name="detail"),
  path('create/', movies_view.MoviesCreate.as_view() , name="create"),
  path('update/<int:pk>/', movies_view.MoviesUpdate.as_view() , name="update"),
]
