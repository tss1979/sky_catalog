# Generated by Django 5.1 on 2024-09-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
