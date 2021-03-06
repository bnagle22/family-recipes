from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  ingredients = models.TextField(max_length=1000)
  steps = models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(default=timezone.now)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('recipes_detail', kwargs={'recipe_id': self.id})