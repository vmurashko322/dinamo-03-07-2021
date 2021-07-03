from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from dinamo.models import Team, Players


class ShowPlayers(generic.ListView):
    model = Team
    template_name = 'dinamo/all_players.html'

    def post(self, request):
        print(request.POST)
        player = Players.objects.filter(name=request.POST['name_players'])
        teams = Team.objects.filter(pk=player.team_id)
        context = {"teams": teams}
        return render('dinamo/all_players.html', context)


