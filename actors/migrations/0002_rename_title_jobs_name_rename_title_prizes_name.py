# Generated by Django 4.2.3 on 2023-11-03 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='prizes',
            old_name='title',
            new_name='name',
        ),
    ]
