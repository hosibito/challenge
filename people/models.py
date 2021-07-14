from django.db import models

# Create your models here.

"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""

KIND_ACTOR = "Actor"
KIND_DIRECTOR = "Director"
KIND_WRITER = "Writer"

KIND_CHOICES = (
  (KIND_ACTOR, "Actor"),
  (KIND_DIRECTOR, "Director"),
  (KIND_WRITER, "Writer"),
)

class Person(models.Model):
      
  """Person Model Definition"""

  name = models.CharField(max_length=80)  
  photo = models.ImageField( blank=True )

  class Meta:
    abstract = True
  
class Person_Actor(Person):
      
  """Person_Actor Model Definition"""

  def __str__(self):
    return self.name

class Person_Director(Person):
      
  """Person_Director Model Definition"""

  def __str__(self):
    return self.name

class Person_Writer(Person):
      
  """Person_Writer Model Definition"""

  def __str__(self):
    return self.name