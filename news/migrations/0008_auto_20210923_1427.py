# Generated by Django 3.2.7 on 2021-09-23 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like_new_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='like_new_comment',
            field=models.ManyToManyField(default='0', related_name='like_new_comment', to='news.Like_new_comment'),
        ),
        migrations.AlterField(
            model_name='like_new_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comments', to='news.comment'),
        ),
    ]