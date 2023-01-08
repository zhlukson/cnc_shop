from django.db import models
from django.urls import reverse

class CncListMetall(models.Model):
    model = models.CharField(max_length=255, verbose_name='Модель')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    work_pole = models.CharField(max_length=255, verbose_name='Рабочая зона')
    emitter_type = models.CharField(max_length=255, verbose_name='Тип лазера')
    power_laser = models.CharField(max_length=255, verbose_name='Мощность лазера')
    dimensions = models.CharField(max_length=255, verbose_name='Габариты')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('cnc', kwargs={'cnc_slug': self.slug})

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
