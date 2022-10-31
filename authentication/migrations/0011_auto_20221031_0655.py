# Generated by Django 3.2.16 on 2022-10-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20221031_0523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_description',
            new_name='cdescription',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_name',
            new_name='cname',
        ),
        migrations.AddField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
