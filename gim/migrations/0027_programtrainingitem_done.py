# Generated by Django 3.2.7 on 2021-10-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0026_auto_20211009_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='programtrainingitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
