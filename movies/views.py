from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models as movies_models

from reviews import models as reviews_models
from reviews import froms as reviews_forms

class MoviesView(ListView):

    """ MoviesView Definition """

    model = movies_models.Movie
    paginate_by = 10
    paginate_orphans = 4


class MoviesDetail(DetailView):

    """ MoviesDetail Deginition """   

    model = movies_models.Movie

    form_class = reviews_forms.CreateReviewForm

    def get_context_data(self, **kwargs):	#template에보낼 context설정
        context = super(MoviesDetail, self).get_context_data(**kwargs)
        context['form'] = self.form_class       
        #context['user'] = self.request.user	# 유저이름표시용
        # print(self.get_object())
        # print(reviews_models.Review.objects.filter(book=self.get_object()))
        context['reviews'] = reviews_models.Review.objects.filter(movie=self.get_object())
        return context
  
    

class MoviesCreate(CreateView):
    
    """ MoviesCreate Deginition """

    model = movies_models.Movie
    fields = ['title',"year",'rating','category','director' , 'cast']


class MoviesUpdate(UpdateView):

    """ MoviesUpdate Deginition """

    model = movies_models.Movie
    fields = ['title',"year",'rating','category','director' , 'cast']
    template_name_suffix = '_update_form'
    