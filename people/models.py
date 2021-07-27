from django.db import models
from django.urls import reverse
from core.models import CoreModel

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