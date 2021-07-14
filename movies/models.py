from django.db import models

from core import models as core_models

# Create your models here.
"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""

class Movie(core_models.TimeStampedModel):
      
  """Movie Model Definition"""

  title = models.CharField(max_length=120)
  year = models.DateField()  
  cover_image = models.ImageField( blank=True)
  rating = models.IntegerField()
  category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
  director = models.ForeignKey("people.Person_Director", on_delete=models.CASCADE)
  cast = models.ManyToManyField("people.Person_Actor", blank=True)

  def __str__(self):
    return self.title