# Generated by Django 3.2.7 on 2021-10-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_name_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=757858765),
            preserve_default=False,
        ),
    ]
