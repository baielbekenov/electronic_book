from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображения')

    def __int__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', verbose_name='Категории')
    file = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.name



