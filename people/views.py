from django.shortcuts import render

from . import models as people_models

def all_people(request):
    return render(request, "people/people_list.html")
