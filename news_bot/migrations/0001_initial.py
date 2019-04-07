# Generated by Django 2.1.7 on 2019-04-07 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('text', models.TextField()),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('discover_date', models.DateTimeField()),
                ('sentiment_score', models.FloatField(blank=True, null=True)),
                ('visible', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
                ('read_time', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
