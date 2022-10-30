# Generated by Django 3.2.16 on 2022-10-30 12:20

from django.db import migrations, models
import snapzapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('snapzapp', '0003_alter_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=snapzapp.models.idGenerator, max_length=200, unique=True),
        ),
    ]