from django.urls import path

from . import views as people_views

app_name = "people"

urlpatterns = [   
    path('', people_views.resolve_people, name="people"),
]