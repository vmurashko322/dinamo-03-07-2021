from django.db import models


# Create your models here.

class Stadium(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    description = models.TextField()
    team=models.OneToOneField('Team', on_delete=models.CASCADE)


class Team(models.Model):
    title = models.CharField(max_length=100)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)


class Players(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # team = models.ManyToManyField('Team')
