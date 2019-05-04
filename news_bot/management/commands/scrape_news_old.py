from django.core.management.base import BaseCommand, CommandError
from news_bot.models import NewsArticle as NewsArticle
from django.db import IntegrityError
import requests
import json
import os

api_key = os.getenv('NEWS_KEY')

def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

class Command(BaseCommand):
    help = 'Scrape the current news for yang gang' 
    

    def handle(self, *args, **options):
        try:
            response = requests.get("https://api.newsriver.io/v2/search?query=text%3A%20%22Andrew%20Yang%22&sortBy=discoverDate&sortOrder=DESC&limit=100", headers={"Authorization": api_key})
            json_data = json.loads(response.text)
            
        except:
            raise CommandError('Error')

        for article in json_data:
            try:
                NewsArticle.objects.get_or_create(
                    title=article['title'],
                    url=article['url'],
                    text=article['text'],
                    website=safeget(article, 'website', 'name'),
                    publish_date=article.get('publishDate'),
                    discover_date=article['discoverDate'],
                    sentiment_score=safeget(article, 'metadata', 'finSentiment', 'sentiment'),
                    read_time=safeget(article, 'metadata', 'readTime', 'seconds')
                    #sentiment_score=article.get('metadata').get('finSentiment').get('sentiment')
                )
            except IntegrityError as e:
                print('Integrity Error')
