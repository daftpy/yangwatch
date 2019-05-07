from django.db import models
from django.core.validators import URLValidator


class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


class AuthorEmail(models.Model):
    author_email = models.EmailField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_email


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)

    url = models.TextField(unique=True, validators=[URLValidator()])

    text = models.TextField()

    website = models.CharField(max_length=200, blank=True, null=True)

    publish_date = models.DateTimeField(blank=True, null=True)

    # Removed due to new news api
    # discover_date = models.DateTimeField()

    # Removed due to news api but will keep in model for future use
    sentiment_score = models.FloatField(blank=True, null=True)

    authors = models.ManyToManyField(Author, blank=True, null=True)

    visible = models.BooleanField(default=False)

    reviewed = models.BooleanField(default=False)

    # Removed read_time due to new news api
    # read_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.website:
            return self.website + ' ' + self.title
        return self.title
