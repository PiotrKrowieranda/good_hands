# Generated by Django 4.2.2 on 2023-11-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]