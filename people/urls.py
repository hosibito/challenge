from django.urls import path

from . import views as people_views

app_name = "people"

urlpatterns = [   
    path('', people_views.PeopleView.as_view() , name="people"),
    path('<int:pk>/', people_views.PeopleDetail.as_view() , name="detail"),
    path('create/', people_views.PeopleCreate.as_view() , name="create"),
    path('update/<int:pk>/', people_views.PeopleUpdate.as_view() , name="update"),
]