# Generated by Django 3.2.16 on 2022-10-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='phoneNumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]