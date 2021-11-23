from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'about.html')

def recipes_index(request):
  return render(request, 'recipes/index.html', { 'recipes': recipes })

def about(request):
  return render(request, 'about.html')

class Recipe:
  def __init__(self, name, ingredients, steps):
    self.name = name
    self.ingredients = ingredients
    self.steps = steps

recipes = [
  Recipe('Eggs', ['eggs', 'oil'], ['add oil to pan', 'cook eggs'])
]