from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import EmptyPage, Paginator

from . import models as people_models

def resolve_people(request):
    page = request.GET.get("page", 1)
    people_list = people_models.Person.objects.all()
    paginator = Paginator(people_list, 10, orphans=4)

    try:
        page_obj = paginator.page(int(page))
        return render(request, "people/people.html", {"page_obj" : page_obj})
    except EmptyPage:
        return redirect(reverse("core:home"))
    
