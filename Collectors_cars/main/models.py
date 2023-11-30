from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class User(AbstractUser):
    pass
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    scale = models.CharField('Масштаб', max_length=50)
    text = models.TextField('Описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

