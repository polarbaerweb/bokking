# Generated by Django 4.2.3 on 2023-11-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_rename_title_jobs_name_rename_title_prizes_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actors',
            old_name='first_name',
            new_name='name',
        ),
    ]
