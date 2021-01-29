# Generated by Django 3.1.3 on 2021-01-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
                ('screen_shot', models.ImageField(upload_to='screenshot/')),
                ('movie_length', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('movie_rate', models.CharField(max_length=100)),
                ('imdb_rating', models.CharField(max_length=100)),
                ('movie_director', models.CharField(max_length=200)),
                ('movie_actor', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=500)),
                ('movie_language', models.CharField(max_length=1000)),
                ('movie_quality', models.CharField(max_length=100)),
                ('movie_link', models.TextField(max_length=10000)),
                ('movie_size', models.CharField(max_length=100)),
            ],
        ),
    ]