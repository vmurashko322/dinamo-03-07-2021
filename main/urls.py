from django.contrib import admin
from django.urls import path, include
from .views import product, product_detail, product2_detail, ProductNew, UserView, CityView, CountryView, ShowMaterial

app_name = 'main'
urlpatterns = [
    path('product/', product, name='product'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('product2/<int:pk>/', product2_detail, name='product2_detail'),
    path('product_class/', ProductNew.as_view(), name='ProductNew'),
    path('user_class/', UserView.as_view(), name='UserView'),
    path('city/', CityView.as_view(), name='CityView'),
    path('country/', CountryView.as_view(), name='CountryView'),
    path('material/', ShowMaterial.as_view(), name='MaterialView'),
]
