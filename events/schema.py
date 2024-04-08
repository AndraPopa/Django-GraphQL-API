import graphene
import events.api.schema


class Query(events.api.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
