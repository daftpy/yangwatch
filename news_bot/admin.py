from django.contrib import admin
from .models import NewsArticle, Author, AuthorEmail
# Register your models here.


def apply_reviewed(modeladmin, request, queryset):
    for article in queryset:
        article.reviewed = True
        article.save()


apply_reviewed.short_description = 'Mark as Reviewed'


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'reviewed', 'visible')
    list_filter = ('reviewed', 'visible')
    actions = [apply_reviewed, ]


class EmailInline(admin.TabularInline):
    model = AuthorEmail


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('author_name',)
    inlines = [
        EmailInline,
    ]


admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorEmail)
