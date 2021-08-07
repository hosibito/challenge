from django import template

from reviews import models as reviews_models
from books import models as books_models
from movies import models as movies_models
from users import models as users_models

register = template.Library()

@register.simple_tag
def is_reviews(user_pk, obj_pk, type):
    user = users_models.User.objects.get(pk=user_pk)   
    try:
        if type == "book":
            reviews_models.Review.objects.get(created_by = user, book__pk=obj_pk)
        elif type =="movie":  
            reviews_models.Review.objects.get(created_by = user, movie__pk=obj_pk)
        return True
    except reviews_models.Review.DoesNotExist:
        return False     
    
   

      