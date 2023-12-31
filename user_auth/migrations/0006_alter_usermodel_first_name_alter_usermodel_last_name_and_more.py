# Generated by Django 4.2.3 on 2023-11-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_usermodel_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(null=True, upload_to='user_images/'),
        ),
    ]
