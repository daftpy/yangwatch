import graphene

import news_bot.schema

class Query(news_bot.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
