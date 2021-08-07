from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
    path("create/<int:obj_pk>:<str:type>", views.review_create_view, name="create"),
    path("delete/<int:pk>:<str:type>", views.review_delete_view , name="delete"),
]