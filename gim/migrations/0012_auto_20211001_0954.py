# Generated by Django 3.2.7 on 2021-10-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0011_remove_programtraining_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programtrainingitem',
            name='date',
        ),
        migrations.AlterField(
            model_name='programtraining',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]