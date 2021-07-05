from rest_framework import serializers

from dinamo.models import Players


class PlayersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Players.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.pop('name')
        instance.surname = validated_data.pop('surname')
        instance.save()
        return instance


class TeamSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    player = PlayersSerializer()


class StadiumSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)
    description = serializers.CharField()
    team = TeamSerializer()


class SponcorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    teams = TeamSerializer(many=True)
