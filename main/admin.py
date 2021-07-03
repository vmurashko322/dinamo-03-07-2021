from django.contrib import admin

# Register your models here.
from main.models import ProductModel, Car, User, Material

admin.site.register(ProductModel)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Material)