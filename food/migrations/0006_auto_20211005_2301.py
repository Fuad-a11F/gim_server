# Generated by Django 3.2.7 on 2021-10-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_food_pryce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='pryce',
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
    ]
