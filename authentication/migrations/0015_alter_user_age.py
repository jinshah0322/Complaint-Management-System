# Generated by Django 3.2.16 on 2022-10-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
    ]
