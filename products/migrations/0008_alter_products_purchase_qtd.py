# Generated by Django 5.2 on 2025-04-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_purchase_qtd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='purchase_qtd',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Quantidade à comprar'),
        ),
    ]
