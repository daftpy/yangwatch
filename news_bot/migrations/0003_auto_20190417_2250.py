# Generated by Django 2.1.7 on 2019-04-18 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_bot', '0002_auto_20190407_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='discover_date',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='read_time',
        ),
    ]