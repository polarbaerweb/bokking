# Generated by Django 4.2.3 on 2023-11-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_profile', '0003_alter_session_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]