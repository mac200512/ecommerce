# Generated by Django 4.1.2 on 2022-10-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]