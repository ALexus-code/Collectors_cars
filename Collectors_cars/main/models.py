from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Task(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    scale = models.CharField('Масштаб', max_length=50)
    task = models.TextField('Описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    members = models.ManyToManyField(User, related_name="members", blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'