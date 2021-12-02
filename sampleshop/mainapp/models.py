from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Category(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    objects = CurrentSiteManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Good(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_created=True,
        auto_now_add=True
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    receipt_date = models.DateField(
        verbose_name='Дата поступления'
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0
    )

    unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=8,
        default='шт'
    )

    vendor = models.CharField(
        verbose_name='Поставщик',
        max_length=255
    )

    category = models.ManyToManyField(Category)

    site = models.ManyToManyField(Site)

    objects = CurrentSiteManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
