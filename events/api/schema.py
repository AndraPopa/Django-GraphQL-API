from datetime import datetime

import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Presenter


class EventType(DjangoObjectType):
    class Meta:
        model = Event

    days_until = graphene.String()

    def resolve_days_until(self, info):
        current_date = datetime.now().date()
        delta = self.date - current_date
        days_until_event = delta.days
        if days_until_event <= 3:
            return "A little bit"
        elif days_until_event < 0:
            return "Already passed"
        else:
            return "A little bit more"


class PresenterType(DjangoObjectType):
    class Meta:
        model = Presenter


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    event = graphene.Field(EventType, id=graphene.Int(), title=graphene.String())

    all_presenters = graphene.List(PresenterType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_all_presenters(self, info, **kwargs):
        return Presenter.objects.all()

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Event.objects.get(pk=id)

        if title is not None:
            return Event.objects.get(title=title)

        return None


class EventCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        date = graphene.Date(required=True)
        mandatory = graphene.Boolean(required=True)

    event = graphene.Field(EventType)

    def mutate(self, info, title, date, mandatory):
        event = Event.objects.create(title=title, date=date, mandatory=mandatory)

        return EventCreateMutation(event=event)

class Mutation:
    create_event = EventCreateMutation.Field()