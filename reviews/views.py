from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404

from . import models as reviews_models
from . import froms as reviews_forms

from books import models as books_models
from movies import models as movies_models

# Create your views here.

@login_required(login_url=reverse_lazy('users:login'))
def review_create_view(request, obj_pk, type):
    if request.method == "POST":
        form = reviews_forms.CreateReviewForm(request.POST)       

        try:
            # 이미 작성된 리뷰가 있다. 처리
            if type == "book":              
                review = reviews_models.Review.objects.get(created_by=request.user, book__pk=obj_pk)
                return redirect(reverse("books:detail", kwargs={"pk": obj_pk}))
            elif type =="movie":   
                review = reviews_models.Review.objects.get(created_by=request.user, movie__pk=obj_pk)
                return redirect(reverse("movies:detail", kwargs={"pk": obj_pk}))            
            return redirect(reverse("core:home"))

        except reviews_models.Review.DoesNotExist:          
            # print(type)     
            # print(obj_pk)     
            # print(request.user)
            if form.is_valid():
                review_f = form.save()
                review_f.created_by = request.user

                if type == "book":
                    review_f.book = books_models.Book.objects.get(pk=obj_pk)
                    review_f.save()
                    return redirect(reverse("books:detail", kwargs={"pk": obj_pk}))

                elif type =="movie":
                    review_f.movie = movies_models.Movie.objects.get(pk=obj_pk)
                    review_f.save()
                    return redirect(reverse("movies:detail", kwargs={"pk": obj_pk}))               
               
                
@login_required(login_url=reverse_lazy('users:login'))
def review_delete_view(request, pk, type):
    try:
        review = reviews_models.Review.objects.get(pk=pk)        
    except reviews_models.Review.DoesNotExist:
        raise Http404("접근방식이 잘못되었습니다.")    

    # print(request.user.pk, review.created_by.pk)   
    if not request.user.pk == review.created_by.pk:
        raise Http404("접근방식이 잘못되었습니다.")    

    if type == "book":              
        return_pk = review.book.pk  
        review.delete()
        return redirect(reverse("books:detail", kwargs={"pk": return_pk}))   
    elif type =="movie":   
        return_pk = review.movie.pk  
        review.delete()  
        return redirect(reverse("movies:detail", kwargs={"pk": return_pk}))   
       
    
    



    
    
