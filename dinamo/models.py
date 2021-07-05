from django.db import models


# Create your models here.

class Stadium(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    description = models.TextField()
    team = models.OneToOneField('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Team(models.Model):
    title = models.CharField(max_length=100)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Players(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # team = models.ManyToManyField('Team')

    def __str__(self):
        return self.name

class Sponcor(models.Model):
    title = models.CharField(max_length=100)
    teams = models.ManyToManyField('Team')

    def __str__(self):
        return self.title