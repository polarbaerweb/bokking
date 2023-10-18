# Generated by Django 4.2.6 on 2023-10-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_data', '0005_remove_movie_name_movie_name_original_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='undecided', max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
