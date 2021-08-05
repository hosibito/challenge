
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from . import models as favlist_models
from users import models as users_models
from books import models as books_models
from movies import models as movies_models


@login_required(login_url=reverse_lazy('users:login'))
def favs_list_view(request, pk):
    if not request.user.pk == pk:
        raise Http404("접근방식이 잘못되었습니다.")

    user = users_models.User.objects.get(pk=pk)
    user = users_models.User.objects.get(pk=pk)
    try:
        h_fav = favlist_models.FavList.objects.get(created_by = user)
    except:
        h_fav = favlist_models.FavList.objects.create(created_by = user)    
        
    b_list = h_fav.books.all()
    b_paginator = Paginator(b_list, 5, orphans=2) 
    b_page = int(request.GET.get("b_page", 1))
    if b_page > b_paginator.num_pages:
        b_page = b_paginator.num_pages 
    page_fav_book = b_paginator.page(int(b_page))

    m_list = h_fav.movies.all()
    m_paginator = Paginator(m_list, 5, orphans=2) 
    m_page = int(request.GET.get("m_page", 1))
    if m_page > m_paginator.num_pages:
        m_page = m_paginator.num_pages     
    page_fav_movie = m_paginator.page(int(m_page))
    
    return render(request, "favs/fav_list.html" ,{
        "page_fav_book" : page_fav_book,
        "page_fav_movie" : page_fav_movie,
    })


@login_required(login_url=reverse_lazy('users:login'))
def favs_add_view(request, pk):
    if not request.user.pk == pk:
        raise Http404("접근방식이 잘못되었습니다.1")
    
    user = users_models.User.objects.get(pk=pk)
    try:
        my_fav = favlist_models.FavList.objects.get(created_by = user)
    except:
        my_fav = favlist_models.FavList.objects.create(created_by = user)
        

    t_pk = request.GET.get("tpk")
    type = request.GET.get("type")

    if type == "book":
        try:
            reselt = books_models.Book.objects.get(pk=t_pk)
            my_fav.books.add(reselt)
            return redirect(reverse('books:detail', kwargs={'pk':t_pk }))
        except:
            raise Http404("접근방식이 잘못되었습니다.2")
    elif type == "movie":
        try:
            reselt = movies_models.Movie.objects.get(pk=t_pk)
            my_fav.movies.add(reselt)
            return redirect(reverse('movies:detail', kwargs={'pk':t_pk }))
        except:
            raise Http404("접근방식이 잘못되었습니다.3")
    else:
        raise Http404("접근방식이 잘못되었습니다.4")
    
  
    

  
    


    # 북과 영화 fav list에 추가한다. 이미 있는거면?..그래서..믹스인...
    

    

    

