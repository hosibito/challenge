from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models as books_models


class BooksView(ListView):

    """ BooksView Definition """

    model = books_models.Book
    paginate_by = 10
    paginate_orphans = 4
    

class BooksDetail(DetailView):

    """ BookDetail Deginition """

    model = books_models.Book

class BooksCreate(CreateView):

    """ BookCreate Deginition """

    model = books_models.Book
    fields = ['title',"year",'rating','category','writer' ]


class BooksUpdate(UpdateView):

    """ BookUpdate Deginition """

    model = books_models.Book
    fields = ['title',"year",'rating','category','writer' ]
    template_name_suffix = '_update_form'
