# Generated by Django 5.0.6 on 2024-07-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='網址別名'),
        ),
    ]