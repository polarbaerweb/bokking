# Generated by Django 4.2.3 on 2023-11-14 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_data', '0009_rename_title_genre_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='title',
            new_name='name',
        ),
    ]
