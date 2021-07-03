from django.contrib import admin
from django.urls import path

from dinamo.views import ShowPlayers

app_name = 'dinamo'
urlpatterns = [
    path('all_players/', ShowPlayers.as_view(), name='show_players'),

]
