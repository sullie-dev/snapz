# Generated by Django 3.2.16 on 2022-11-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapzapp', '0006_auto_20221101_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='eMtYxgAuzr', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='eMtYxgAuzr', max_length=200, unique=True),
        ),
    ]