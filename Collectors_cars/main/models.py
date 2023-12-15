from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.contrib.auth.models import User


My_choices = (
    ("1/64", "1/64"),
    ("1/48", "1/48"),
    ("1/32", "1/32"),
    ("1/18", "1/18"),
)
class User(AbstractUser):
    pass

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    scale = models.CharField(max_length=20, choices=My_choices, default='1')
    photo = models.ImageField('Фото', upload_to=user_directory_path)
    text = models.TextField('Описание')
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

