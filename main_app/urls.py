from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.Home.as_view(), name="home"),
  # localhost:8000/about
  path('about/', views.about, name='about'),
  # localhost:8000/recipes
  path('recipes/', views.recipes_index, name='recipes_index'),
  # localhost:8000/recipes/:recipe_id
  path('recipes/<int:recipe_id>/', views.recipes_detail, name='recipes_detail'),
  # localhost:8000/recipes/create
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('accounts/signup/', views.signup, name='signup')
]