from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField(validators=[URLValidator()])
    text = models.TextField()
    website = models.CharField(max_length=200, blank=True, null=True)
    # Not all articles have explicit publish dates
    publish_date = models.DateTimeField(blank=True, null=True)
    discover_date = models.DateTimeField()
    sentiment_score = models.FloatField(blank=True, null=True)
    visible = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    # Anticipating that readtime might not be calculated
    read_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.website:
            return self.website + ' ' + self.title
        return self.title
