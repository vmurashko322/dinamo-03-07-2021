from django.db import models


# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Car(models.Model):
    name = models.CharField(max_length=10)
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=150)
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    A = (
        ('железо', 'железо'),
        ('ртуть', 'ртуть'),
        ('что-то', 'что-то')

    )
    title = models.ManyToManyField('ProductModel')
    model = models.CharField(max_length=150, choices=A, default='железо')
    user = models.OneToOneField('User', on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=150)
    population = models.PositiveIntegerField()


class Country(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
