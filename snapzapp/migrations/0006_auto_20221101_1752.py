# Generated by Django 3.2.16 on 2022-11-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapzapp', '0005_auto_20221101_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='JA9FsWo0Xm', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='JA9FsWo0Xm', max_length=200, unique=True),
        ),
    ]
