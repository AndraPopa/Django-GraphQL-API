import graphene
from graphene_django.types import DjangoObjectType
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    event = graphene.Field(EventType, id=graphene.Int(), title=graphene.String())

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Event.objects.get(pk=id)

        if title is not None:
            return Event.objects.get(title=title)

        return None