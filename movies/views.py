from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models as movies_models

class MoviesView(ListView):

    """ MoviesView Definition """

    model = movies_models.Movie
    paginate_by = 10
    paginate_orphans = 4


class MoviesDetail(DetailView):

    """ MoviesDetail Deginition """   

    model = movies_models.Movie
  
    

class MoviesCreate(CreateView):
    
    """ MoviesCreate Deginition """

    model = movies_models.Movie
    fields = ['title',"year",'rating','category','director' , 'cast']


class MoviesUpdate(UpdateView):

    """ MoviesUpdate Deginition """

    model = movies_models.Movie
    fields = ['title',"year",'rating','category','director' , 'cast']
    template_name_suffix = '_update_form'
    