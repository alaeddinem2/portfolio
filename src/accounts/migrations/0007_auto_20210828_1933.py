# Generated by Django 2.2.14 on 2021-08-28 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210828_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='slug',
            new_name='ProSlug',
        ),
    ]