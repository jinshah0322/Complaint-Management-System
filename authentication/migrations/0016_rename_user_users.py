# Generated by Django 3.2.16 on 2022-10-31 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_user_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
