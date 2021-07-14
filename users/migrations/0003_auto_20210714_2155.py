# Generated by Django 3.2.5 on 2021-07-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('users', '0002_auto_20210714_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourite_book_genre',
        ),
        migrations.AddField(
            model_name='user',
            name='favourite_book_genre',
            field=models.ManyToManyField(blank=True, related_name='Category_book', to='categories.Category'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='favourite_movie_genre',
        ),
        migrations.AddField(
            model_name='user',
            name='favourite_movie_genre',
            field=models.ManyToManyField(blank=True, related_name='Category_movie', to='categories.Category'),
        ),
    ]