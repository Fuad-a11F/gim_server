# Generated by Django 3.2.7 on 2021-10-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_new_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='Comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.new'),
        ),
        migrations.AlterModelTable(
            name='new',
            table=None,
        ),
    ]
