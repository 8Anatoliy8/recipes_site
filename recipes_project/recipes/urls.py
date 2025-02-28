from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import recipe_details, add_recipe, home, register, edit_recipe, delete_recipe

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:recipe_id>/', recipe_details, name='recipe_details'),
    path('recipe/<int:recipe_id>/edit/', edit_recipe, name='edit_recipe'),
    path('recipe/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),
    path('add/', add_recipe, name='add_recipe'),
    path('login/', LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]