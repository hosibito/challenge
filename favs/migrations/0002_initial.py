# Generated by Django 3.2.5 on 2021-07-19 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favlist',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favlist',
            name='movies',
            field=models.ManyToManyField(related_name='fav_lists', to='movies.Movie'),
        ),
    ]
