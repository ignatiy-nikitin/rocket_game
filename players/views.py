from django.shortcuts import redirect, render
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from players.serializers import BetSerializer
from bets.views import BetViewSet
from players.models import Player
from players.serializers import GetBalanceSerializer, PlayerSerializer, WithdrawSerializer

from rest_framework.decorators import action


from rest_framework import mixins

from bets.models import Bet

from rest_framework import generics, status


class PlayerViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        Получить информацию о игроках (для админа - статистика всех игроков)

        -

    read:
        Получить информацию о игроке по id (для админа - статистика всех игроков)

        -
    """
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Player.objects.all()
        return Player.objects.filter(merchant=self.request.user)
