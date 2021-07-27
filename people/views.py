from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models as people_models


class PeopleView(ListView):

    """ PeopleView Definition """

    model = people_models.Person
    paginate_by = 10
    paginate_orphans = 4
    
class PeopleDetail(DetailView):
    
    """ BookDetail Deginition """

    model = people_models.Person

class PeopleCreate(CreateView):

    """ BookCreate Deginition """

    model = people_models.Person
    fields = ['name',"kind" ]


class PeopleUpdate(UpdateView):

    """ BookUpdate Deginition """

    model = people_models.Person
    fields = ['name',"kind" ]
    template_name_suffix = '_update_form'
