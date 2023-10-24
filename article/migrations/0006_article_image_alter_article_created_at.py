# Generated by Django 4.2.5 on 2023-10-04 18:02

import article.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=article.models.upload_to_path),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 23, 32, 51, 472737)),
        ),
    ]
