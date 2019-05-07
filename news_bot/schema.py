import graphene
from graphene_django.types import DjangoObjectType
from .models import NewsArticle, Author


class NewsArticleType(DjangoObjectType):
    class Meta:
        model = NewsArticle


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query(object):
    newsarticle = graphene.List(
        NewsArticleType,
        id=graphene.Int(),
        keyword=graphene.String()
    )

    all_newsarticles = graphene.List(NewsArticleType)

    def resolve_all_newsarticles(self, info, **kwargs):
        print('success')
        return NewsArticle.objects.filter(visible=True)

    def resolve_newsarticle(self, info, **kwargs):
        id = kwargs.get('id')
        keyword = kwargs.get('keyword')

        if keyword is not None:
            print('keyword found')
            return NewsArticle.objects.filter(text__icontains=keyword) \
                .filter(visible=True)

        if id is not None:
            print(id)
            return NewsArticle.objects.filter(pk=id)

        return None
