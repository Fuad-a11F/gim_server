# Generated by Django 3.2.7 on 2021-09-26 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210926_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.playlistitem'),
        ),
    ]
