from django.db import models

# Create your models here.
"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""

class Review(models.Model):
  created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
  text = models.TextField()
  movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, null=True, blank=True )
  book = models.ForeignKey("books.Book", on_delete=models.CASCADE, null=True,blank= True)
  rating = models.IntegerField()

  def __str__(self):
    return f"{self.created_by.username} / {self.movie} / {self.book}"