from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'имя: {self.title}, стоимость: {self.price}'

    class Meta:
        verbose_name = 'cash_machine_item'
        ordering = ['title']
