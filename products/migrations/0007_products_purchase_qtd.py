# Generated by Django 5.2 on 2025-04-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='purchase_qtd',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
