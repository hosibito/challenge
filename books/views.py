from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models as books_models

from reviews import models as reviews_models
from reviews import froms as reviews_forms


class BooksView(ListView):

    """ BooksView Definition """

    model = books_models.Book
    paginate_by = 10
    paginate_orphans = 4
    

class BooksDetail(DetailView):

    """ BookDetail Deginition """

    model = books_models.Book

    form_class = reviews_forms.CreateReviewForm

    def get_context_data(self, **kwargs):	#template에보낼 context설정
        context = super(BooksDetail, self).get_context_data(**kwargs)
        context['form'] = self.form_class       
        #context['user'] = self.request.user	# 유저이름표시용
        # print(self.get_object())
        # print(reviews_models.Review.objects.filter(book=self.get_object()))
        context['reviews'] = reviews_models.Review.objects.filter(book=self.get_object())
        return context

class BooksCreate(CreateView):

    """ BookCreate Deginition """

    model = books_models.Book
    fields = ['title',"year",'rating','category','writer' ]

   


class BooksUpdate(UpdateView):

    """ BookUpdate Deginition """

    model = books_models.Book
    fields = ['title',"year",'rating','category','writer' ]
    template_name_suffix = '_update_form'
