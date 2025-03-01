from django import forms
from django.contrib.auth.models import User
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Категория'
    )
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'servings', 'ingredients', 'steps', 'cooking_time', 'image', 'category']
        labels = {
            'title': 'Название',
            'description': 'Краткое описание',
            'servings': 'Количество порций',
            'ingredients': 'Ингридиенты',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (мин)',
            'image': 'Изображение',
            'category': 'Категория'
        }


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'password': 'Пароль'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        return cleaned_data