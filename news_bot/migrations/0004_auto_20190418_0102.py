# Generated by Django 2.1.7 on 2019-04-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_bot', '0003_auto_20190417_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='author_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
