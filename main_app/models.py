from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=100)
  steps = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('recipes_detail', kwargs={'recipe_id': self.id})