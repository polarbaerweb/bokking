# Generated by Django 4.2.6 on 2023-10-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_usermodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_address',
            field=models.CharField(default='', max_length=40, verbose_name='User address'),
        ),
    ]