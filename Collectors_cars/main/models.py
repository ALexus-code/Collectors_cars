from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.contrib.auth.models import User

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    scale = models.CharField('Масштаб', max_length=50)
    text = models.TextField('Описание')
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

