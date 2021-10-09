# Generated by Django 2.2.14 on 2021-08-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210827_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ProSlug',
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
