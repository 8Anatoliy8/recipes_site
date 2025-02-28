from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150,
                                    blank=True,
                                    help_text='Краткое описание категории')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    ingredients = models.TextField(help_text='Перечислите ингридиенты через запятую')
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text='Время в минутах')
    servings = models.PositiveIntegerField(default=1, help_text='Количество порций')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title