# Generated by Django 3.2.16 on 2022-10-31 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_complaint_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='phoneNumber',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='date_of_register',
        ),
    ]
