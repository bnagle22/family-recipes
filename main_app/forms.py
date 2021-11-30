from django.forms import ModelForm, fields
from .models import Recipe

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = ["date"]