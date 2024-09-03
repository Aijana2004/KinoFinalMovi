# Generated by Django 5.0.7 on 2024-07-28 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_description_en_product_description_ky_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ky',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_tr',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
