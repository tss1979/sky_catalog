from random import choice
from tabnanny import verbose

from django.core.files.images import ImageFile
from django.db import models
from django.db.models import ForeignKey, BooleanField
from django.forms import CharField, FloatField

from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=500, **NULLABLE, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    description = models.CharField(max_length=500, **NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='img/', **NULLABLE, verbose_name='превью')
    price = models.FloatField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='время создания')
    updated_at =models.DateTimeField(auto_now_add=True, verbose_name='время последнего изменениязшз')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('update_published_status', 'Can cancel publish product'),
            ('update_description', 'Can update product description'),
            ('change_category', 'Can change product category')
        ]

    def __str__(self):
        return f'{self.name}({self.category})'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер')
    name = models.CharField(max_length=255, verbose_name='название', **NULLABLE)
    is_current = models.BooleanField(default=True, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'Версия {self.number} - {self.name}'










