from django.db import models

# Create your models here.
"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""

class FavList(models.Model):
  created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)    
  books = models.ManyToManyField("books.Book", blank= True)
  movies = models.ManyToManyField("movies.Movie",  blank=True )  

  def __str__(self):
    return self.created_by.username