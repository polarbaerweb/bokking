# Generated by Django 4.2.3 on 2023-11-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_data', '0008_rename_name_original_movie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='title',
            new_name='name',
        ),
    ]
