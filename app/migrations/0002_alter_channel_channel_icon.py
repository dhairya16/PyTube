# Generated by Django 3.2 on 2021-05-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_icon',
            field=models.ImageField(default='default_icon.png', upload_to='profile/'),
        ),
    ]
