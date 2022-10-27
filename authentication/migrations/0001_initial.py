# Generated by Django 4.1.2 on 2022-10-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_name', models.CharField(max_length=100)),
                ('complaint_description', models.TextField()),
                ('priority', models.CharField(choices=[('High', 'High'), ('Moderate', 'Moderate'), ('Low', 'Low')], max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]