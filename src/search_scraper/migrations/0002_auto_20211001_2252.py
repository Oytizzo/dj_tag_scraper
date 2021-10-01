# Generated by Django 3.2.7 on 2021-10-01 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search_scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchitem',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 16, 52, 12, 93098, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='searchitem',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
