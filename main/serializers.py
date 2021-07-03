from rest_framework import serializers

from main.models import ProductModel, User, City, Country, Material


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15, read_only=True)
    product = ProductSerializer()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    product = ProductSerializer()

    def create(self, validated_data):
        product = ProductModel(**dict(validated_data['product']))
        test = ProductModel.objects.filter(title=product.title, price=product.price)
        if test:
            validated_data['product'] = test[0]
        else:
            validated_data['product'] = product
            product.save()
        return User.objects.create(**validated_data)

        # product=ProductModel.objects.get_or_create(**dict(validated_data['product']))
        # validated_data['product']=product[0]
        # return User.objects.create(**validated_data)


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    population = serializers.IntegerField()


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    city = CitySerializer()

    def create(self, validated_data):
        city = City.objects.create(**dict(validated_data['city']))
        base = City.objects.filter(name=city.name, population=city.population)
        print(base)
        print(base.values())
        print(base[0])
        if base:
            validated_data['city'] = base[0]
        else:
            validated_data['city'] = city
            city.save()
        return Country.objects.create(**validated_data)


class MaterialSerializer(serializers.Serializer):
    title = ProductSerializer(many=True)
    model = serializers.CharField(max_length=150)
    user = UserSerializer()

    def create(self, validated_data):
        product_list = []
        if validated_data.get('title'):
            for i in validated_data['title']:
                prod = ProductModel.objects.get_or_create(**i)
                product_list.append(prod[0])
        if validated_data.get('user'):
            prod_user = ProductModel.objects.get_or_create(**validated_data['user']['product'])[0]
            user = User.objects.create(name=validated_data["user"]['name'], product=prod_user)
        if validated_data.get('model'):
            material = Material.objects.create(model=validated_data['model'], user=user)
            material.title.set(product_list)
            return material
