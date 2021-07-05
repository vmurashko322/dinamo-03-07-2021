from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from dinamo.models import Team, Players, Stadium, Sponcor
from dinamo.serializers import PlayersSerializer, StadiumSerializer, TeamSerializer, SponcorSerializer


class ShowPlayers(generic.ListView):
    model = Team
    template_name = 'dinamo/all_players.html'

    def post(self, request):
        player = Players.objects.filter(name=request.POST['name_players'])
        try:
            t = player.values('id')
            print(player[0].__dict__)
            print(t)
            result = []
            for i in t:
                teams = Team.objects.get(pk=i['id'])
                print(teams)
                result.append(teams)
            context = {"teams": result}
            print(result)
            return render(request, 'dinamo/all_players.html', context)
        except:
            return render(request, 'dinamo/all_players.html')


class ShowPlayer(APIView):
    def get(self, request):
        stadium = Stadium.objects.all()
        players = Players.objects.all()
        team = Team.objects.all()
        sponcor = Sponcor.objects.all()
        serializer_player = PlayersSerializer(players, many=True)
        serializer_stadium = StadiumSerializer(stadium, many=True)
        serializer_team = TeamSerializer(team, many=True)
        serializer_sponcor = SponcorSerializer(sponcor, many=True)

        res = {"players": serializer_player.data, 'stadium': serializer_stadium.data, 'team': serializer_team.data,
               "sponcor": serializer_sponcor.data}
        return Response(res)


class PlayerView(APIView):
    def get(self, request, pk=None):
        if not pk:
            player = Players.objects.all()
            serializer = PlayersSerializer(player, many=True)
        else:
            player = Players.objects.get(pk=pk)
            serializer = PlayersSerializer(player)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = PlayersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        player = Players.objects.get(pk=pk)
        serializer = PlayersSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
