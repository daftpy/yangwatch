from django.core.management.base import BaseCommand, CommandError
from news_bot.models import NewsArticle, Author, AuthorEmail
from django.db import IntegrityError
from eventregistry import EventRegistry, QueryArticlesIter
import os

apikey = os.getenv('NEWS_KEY')

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
        er = EventRegistry(apiKey=apikey)
        q = QueryArticlesIter(
            keywords='Andrew Yang',
            keywordsLoc='body, title',
        )

        for article in q.execQuery(er, sortBy='date', maxItems=10):
            try:
                existing_article, new_article = NewsArticle.objects.get_or_create(
                    title=article['title'],
                    url=article['url'],
                    text=article['body'],
                    website=safeget(article, 'source', 'uri'),
                    publish_date=article.get('dateTime'),
                )
                for author in article['authors']:
                    existing_author, new_author = Author.objects.get_or_create(
                        author_name = author.get('name')
                    )
                    existing_email, new_email = AuthorEmail.objects.get_or_create(
                        author_email = author.get('uri'),
                        author = existing_author
                    )
                    if new_article:
                        existing_article.authors.add(existing_author)
                        existing_article.save()
                        print(existing_author, ' added to ', existing_article)
                    if existing_article:
                        print('exists')
            except IntegrityError as e:
                print('Integrity Error:', e)

