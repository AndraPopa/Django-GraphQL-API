import graphene

import events.api.schema


class Query(events.api.schema.Query, graphene.ObjectType):
    pass


class Mutation(events.api.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
