# Generated by Django 3.2.7 on 2021-09-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210918_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
