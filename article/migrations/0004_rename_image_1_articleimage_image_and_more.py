# Generated by Django 4.2.5 on 2023-10-04 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleimage',
            old_name='image_1',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 23, 14, 41, 306813)),
        ),
    ]
