# Generated by Django 2.2.14 on 2021-08-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210827_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ProImage',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics', verbose_name='Profile Image'),
        ),
    ]
