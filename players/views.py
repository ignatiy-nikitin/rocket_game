from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bets.serializers import BetSerializer
from bets.views import BetViewSet
from players.models import Player
from players.serializers import PlayerSerializer

from rest_framework.decorators import action


from rest_framework import mixins

from bets.models import Bet


# Create your views here.
class PlayerViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        Создать игрока

        Создает игрока с данными от провайдера


    retrieve:
        Получить информацию о игроке

        -

    bets:
        Получить список ставок пользователя (история ставок)

        -

    bets_active:
        Получить список активных ставок пользователя

        -

    '''
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


    @action(detail=True, methods=['get'])
    def bets(self, request, pk=None):
        bets = Bet.objects.filter(player_id=pk).order_by('-id')
        response = [BetSerializer(bet).data for bet in bets]
        return Response(response)

    @action(detail=True, methods=['get'])
    def bets_active(self, request, pk=None):
        bets = Bet.objects.filter(player_id=pk, status='active').order_by('-id')
        response = [BetSerializer(bet).data for bet in bets]
        return Response(response)

    # @action(detail=True, methods=['get'])
    # def betss(self, request, pk=None):
    #     bets = Bet.objects.filter(user=self.kwargs['id'])
    #     return Response(self.get_serializer(bets).data)


# class PlayerBetsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
#     '''
#     list:
#         Получить историю ставок игрока

#         -

#     read:
#         Получить ставку игрока

#         -
#     '''
#     def get_queryset(self):
#         return Bet.objects.filter(user=self.kwargs['pk'])