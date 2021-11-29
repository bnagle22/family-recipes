from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Recipe
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

recipes = [
  Recipe('Eggs', ['eggs', 'oil'], ['add oil to pan', 'cook eggs'])
]

class Home(LoginView):
  template_name = 'home.html'

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'ingredients', 'steps']
  success_url = '/recipes/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def home(request):
  return render(request, 'home.html')

@login_required
def recipes_index(request):
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', { 'recipes': recipes })

@login_required
def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  return render(request, 'recipes/detail.html', {'recipe': recipe })

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('recipes_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


# class Recipe:
#   def __init__(self, name, ingredients, steps):
#     self.name = name
#     self.ingredients = ingredients
#     self.steps = steps
