from django.contrib import admin
from .models import NewsArticle
# Register your models here.

def apply_reviewed(modeladmin, request, queryset):
    for article in queryset:
        article.reviewed = True
        article.save()

apply_reviewed.short_description = 'Mark as Reviewed'


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'discover_date', 'reviewed', 'visible')
    list_filter = ('reviewed', 'visible')
    actions = [apply_reviewed,]

admin.site.register(NewsArticle, NewsArticleAdmin)