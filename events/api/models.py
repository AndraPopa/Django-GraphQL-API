from django.db import models


class Presenter(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.surname


class Event(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField()
    mandatory = models.BooleanField(default=False)
    presenter = models.ForeignKey(
        Presenter, on_delete=models.PROTECT, blank=True, null=True
    )

    def __str__(self):
        return self.title
