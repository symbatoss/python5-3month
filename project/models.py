from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=100,
                            verbose_name='Название')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    title = models.CharField(max_length=100,
                             verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    text = models.TextField(verbose_name='Текст')
    product = models.ForeignKey(Product, null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Продукт')

    def __str__(self):
        return self.text
