from django import template

from favs import models as favlist_models
from books import models as books_models
from movies import models as movies_models
from users import models as users_models

register = template.Library()

@register.simple_tag
def is_favs(user_pk, t_pk, type):
    user = users_models.User.objects.get(pk=user_pk)   
    try:
        my_fav = favlist_models.FavList.objects.get(created_by = user)
    except:
        my_fav = favlist_models.FavList.objects.create(created_by = user)      

    if type == "book":
        try:
            reselt = books_models.Book.objects.get(pk=t_pk)  
            if reselt in my_fav.books.all():
                return True             
        except:
            return False

    elif type == "movie":
        try:
            reselt = movies_models.Movie.objects.get(pk=t_pk)            
            if reselt in my_fav.movies.all():
                return True  
        except:          
            return False
    
    return False

      