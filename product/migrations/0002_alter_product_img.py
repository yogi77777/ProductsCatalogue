# Generated by Django 3.2.6 on 2021-08-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media/products'),
        ),
    ]
