from .models import Post
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "scale", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "scale": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Масштаб'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
User = get_user_model()



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")