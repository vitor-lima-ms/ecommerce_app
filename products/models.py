from django.db import models

# Create your models here.

modelsChoices = [
    ('Bellafral', 'Bellafral'),
    ('Big Confort', 'Big Confort'),
    ('Basic/Mille', 'Basic/Mille'),
]

sizesChoices = [
    ('XG', 'XG'),
    ('G', 'G'),
    ('M', 'M'),
]

class Products(models.Model):
    model = models.CharField(max_length=200, choices=modelsChoices, default='Bellafral')
    size = models.CharField(max_length=200, choices=sizesChoices, default='XG')
    description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    stock = models.IntegerField(default=0, blank=True, null=True)
    purchase_qtd = models.PositiveIntegerField(verbose_name='Quantidade à comprar', default=0, blank=True, null=True)
    image = models.ImageField(upload_to='media/', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.model} - {self.size}'
