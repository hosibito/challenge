# Generated by Django 3.2.5 on 2021-07-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('kind', models.CharField(choices=[('book', 'book'), ('movie', 'movie'), ('both', 'both')], default='both', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
