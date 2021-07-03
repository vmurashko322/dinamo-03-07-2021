import json
import io
import requests
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from main.models import ProductModel, Car, User, City, Country, Material
from main.serializers import ProductSerializerModel, ProductSerializer, CarSerializer, UserSerializer, CitySerializer, \
    CountrySerializer, MaterialSerializer


class A:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def get_name(self):
        return self.name


user = requests.get('https://jsonplaceholder.typicode.com/users/1')
a1 = user.json()
a = A(a1['name'], a1['username'], a1['email'])

res = json.dumps(a.__dict__)
content = JSONRenderer().render(a.__dict__)

d = {'id': 1, 'name': 'Johan'}
_json = json.dumps(d)


@api_view(['GET', 'POST'])
def product(request):
    confeti = ProductModel.objects.all()
    data = ProductSerializer(confeti, many=True)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(data.data)
    # if request.method == 'POST':
    #     serializer = ProductSerializerModel(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    # confeti = ProductModel.objects.all()
    # serializer = ProductSerializerModel(confeti, many=True)
    # return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def product_detail(request, pk):
    prod = get_object_or_404(ProductModel, pk=pk)
    if request.method == "GET":
        serializer = ProductSerializerModel(prod)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializerModel(instance=prod, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=201)


@api_view(['GET', 'POST', 'PUT'])
def product2_detail(request, pk):
    prod = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(prod)
    print(serializer.data)
    if request.method == 'PUT':
        serializer = CarSerializer(instance=prod, partial=True, data=request.data)
        ######
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response(serializer.data)


def get_object(request):
    try:
        return ProductModel.objects.all()
    except:
        return Http404


class ProductNew(APIView):

    def get(self, request, format=None):
        obj = get_object(request)
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('main:product'))
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class UserView(APIView):
    def get(self, request, format=None):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('main:product'))
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CityView(APIView):
    def get(self, request):
        obj = City.objects.all()
        serializer = CitySerializer(obj, many=True)
        return Response(serializer.data)


class CountryView(APIView):
    def get(self, request):
        obj = Country.objects.all()
        serializer = CountrySerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ShowMaterial(APIView):
    def get(self, request):
        obj = Material.objects.all()
        serializer = MaterialSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print(serializer.validated_data, ' из вью ')
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors)
