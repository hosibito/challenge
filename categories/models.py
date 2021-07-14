from django.db import models

# Create your models here.
"""
Here are the models you have to create:
- Category
  name
  kind (book/movie/both)
"""

KIND_BOOK = "book"
KIND_MOVIE = "movie"
KIND_BOTH = "both"

KIND_CHOICES = (
  (KIND_BOOK, "book"),
  (KIND_MOVIE, "movie"),
  (KIND_BOTH, "both"),
)

class Category(models.Model):
      
  """Person Model Definition"""

  name = models.CharField(max_length=80)
  kind = models.CharField(choices=KIND_CHOICES, max_length=10, default=KIND_BOTH) 

  def __str__(self):
    return f"{self.name}  - {self.kind}"