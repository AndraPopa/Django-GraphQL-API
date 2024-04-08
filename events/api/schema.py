import graphene
from graphene_django.types import DjangoObjectType
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()