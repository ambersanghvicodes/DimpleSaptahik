# Generated by Django 4.2.5 on 2023-10-04 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_image_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 23, 34, 33, 507272)),
        ),
    ]