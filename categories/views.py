from django.shortcuts import render

from django.views.generic import ListView, DetailView

from . import models as categories_models
from movies import models as movie_models
from books import models as book_models

class CategoriesView(ListView):
    
    """ CategoriesView Definition """

    model = categories_models.Category
    paginate_by = 10
    paginate_orphans = 4


class CategoriesDetail(DetailView):
    
    """ MoviesDetail Deginition """   

    model = categories_models.Category    

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['movie_reselt']=movie_models.Movie.objects.filter(category=self.kwargs.get('pk'))
        context['book_reselt']=book_models.Book.objects.filter(category=self.kwargs.get('pk'))        
        return context