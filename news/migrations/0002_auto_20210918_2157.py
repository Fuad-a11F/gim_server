# Generated by Django 3.2.7 on 2021-09-18 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_new_comment',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='like_new_comment', to='news.like_new_comment'),
        ),
        migrations.AlterField(
            model_name='new',
            name='like',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='news.like'),
        ),
    ]
