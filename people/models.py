from django.db import models
from django.urls import reverse
from core.models import CoreModel
from movies.models import Movie as models_Movie
from books.models import Book as models_Book
class Person(CoreModel):

  """ Person Model """

  KIND_ACTOR = "actor"
  KIND_DIRECTOR = "director"
  KIND_WRITER = "writer"

  KIND_CHOICES = (
    (KIND_ACTOR, "Actor"),
    (KIND_DIRECTOR, "Director"),
    (KIND_WRITER, "Writer")
  )

  name = models.CharField(max_length=120)
  photo = models.ImageField()
  kind = models.CharField(max_length=15, choices=KIND_CHOICES)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('people:detail', kwargs={'pk': self.pk})

  def get_activate_list(self):
    g_kind = self.kind   
    if g_kind == self.KIND_ACTOR:
      g_list = models_Movie.objects.filter(cast=self.pk)
    elif g_kind == self.KIND_DIRECTOR:
      g_list = models_Movie.objects.filter(director=self.pk)
    elif g_kind == self.KIND_WRITER:
      g_list = models_Book.objects.filter(writer=self.pk)
      
    return g_list