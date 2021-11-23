from django.db import models

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=100)
  steps = models.CharField(max_length=100)

  def __str__(self):
    return self.name