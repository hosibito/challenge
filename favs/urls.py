from django.urls import path

from . import views as favs_view

app_name="favs"

urlpatterns = [  
  path('<int:pk>/', favs_view.favs_list_view , name="list"),  
  path('add/<int:pk>/', favs_view.favs_add_view , name="add"),
]
