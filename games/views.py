from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bets.serializers import BetSerializer
from bets.views import BetViewSet
from games.models import Game
from games.serializers import GameSerializer
from merchants.serializers import MerchantSerializer
from players.models import Player
from players.serializers import PlayerSerializer

from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated


from rest_framework import mixins

from bets.models import Bet


class GameViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
