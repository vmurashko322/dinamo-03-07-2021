from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dinamo.views import ShowPlayer, ShowPlayers, PlayerView

app_name = 'dinamo'
urlpatterns = [
    path('all_players/', ShowPlayers.as_view(), name='show_players'),
    path('player/', ShowPlayer.as_view(), name='ShowPlayers'),
    path('create_player/', PlayerView.as_view(), name='PlayerView'),
    path('create_player/<int:pk>/', PlayerView.as_view(), name='UpdatePlayer'),
]
urlpatterns=format_suffix_patterns(urlpatterns)