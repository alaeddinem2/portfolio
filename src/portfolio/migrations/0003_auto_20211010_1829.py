# Generated by Django 2.1.4 on 2021-10-10 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_maxnumpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maxnumpost',
            old_name='user',
            new_name='user_num',
        ),
    ]
