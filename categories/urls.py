from django.urls import path

from . import views as categories_views

app_name = "category"

urlpatterns = [   
    path('', categories_views.CategoriesView.as_view(), name="categories"),
    path('<int:pk>/', categories_views.CategoriesDetail.as_view() , name="detail"),
]