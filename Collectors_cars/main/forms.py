from .models import Post
from django.forms import ModelForm, TextInput, Textarea, Select, ImageField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

My_choices = (
    ("1/64", "1/64"),
    ("1/48", "1/48"),
    ("1/32", "1/32"),
    ("1/18", "1/18"),
)

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        fields = ["title", "scale", "photo", "text", "author"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "scale": Select(choices=My_choices),
            #"photo": ImageField(),
            "text": Textarea(attrs={
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