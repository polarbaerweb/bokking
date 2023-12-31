# Generated by Django 4.2.6 on 2023-10-16 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_usermodel_managers_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
