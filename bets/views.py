from django.shortcuts import render
from rest_framework import viewsets
from bets.serializers import BetSerializer

from rest_framework.response import Response

from bets.models import Bet

from rest_framework.decorators import action
from rest_framework import status

from decimal import Decimal

# from rest_framework.generics import GenericAPIView
from rest_framework import mixins 

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class BetViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    list:
        Получить список ставок

        -

    create:
        Сделать ставку

        Метод сздает ставку, привязанную к определенному игроку. Параметр amount отправляется строкой в формате "100.00"


    retrieve:
        Получить информацию о ставке

        -

    win:
        Присвоить ставке статус выигрышной

        Пользователь получает выигрыш исходя из размера ставки и ее коэффициента

    loose:
        Присвоить ставке статус проигранной 

        -


    '''
    # serializer_class = BetSerializer
    queryset = Bet.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['player__id']

    def get_serializer_class(self):
        if action in ('win', 'loose'):
            return None
        return BetSerializer


    @action(detail=True, methods=['post'])
    def win(self, request, pk=None):
        bet = self.get_object()
        if bet.status != Bet.StatusChoices.ACTIVE:
            return Response({'warn': 'bet already closed'})
        bet.status = Bet.StatusChoices.WIN
        bet.save()
        total_win = bet.amount * bet.factor
        bet.player.balance += total_win
        bet.player.active_bets -= 1
        bet.player.save()
        return Response(self.get_serializer(bet).data)

    @action(detail=True, methods=['post'])
    def loose(self, request, pk=None):
        bet = self.get_object()
        if bet.status != Bet.StatusChoices.ACTIVE:
            return Response({'warn': 'bet already closed'})
        bet.status = Bet.StatusChoices.LOOSE
        bet.save()
        bet.player.active_bets -= 1
        bet.player.save()
        return Response(self.get_serializer(bet).data)