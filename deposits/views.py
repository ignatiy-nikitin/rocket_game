import re
from django.shortcuts import redirect, render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bets.serializers import BetSerializer
from bets.views import BetViewSet
from deposits.serializers import DepositCreateSerializer
from merchants.models import Merchant
from merchants.serializers import MerchantAuthSerializer, MerchantSerializer
from merchants.services import get_merchant_by_auth_token
from players.models import Player
from players.serializers import PlayerSerializer

from deposits.serializers import DepositSerializer

from rest_framework.decorators import action, api_view

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import permissions


from rest_framework import mixins

from bets.models import Bet

from rest_framework.views import APIView

from rest_framework import generics, status

from players.services import get_player_by_private_token

from deposits.models import Deposit


class DepositViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        Получить информацию о депозитах игроков партнера (для админа - статистика всех игроков)

        -

    read:
        Получить информацию о депозите игрока партнера по id (для админа - статистика всех игроков)

        -
    """
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Deposit.objects.all()
        return Deposit.objects.filter(player__merchant=self.request.user)


class DepositCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = DepositCreateSerializer(data=request.data)
        if serializer.is_valid():

            player = get_player_by_private_token(serializer.data['player_private_token']) # + merchant_id

            deposit = DepositSerializer(data={
                'amount': serializer.data['amount'],
                'player': player.id,
                'currency': serializer.data['currency'],
            })
            if deposit.is_valid():
                deposit.save()
            else:
                return Response(deposit.errors, status=status.HTTP_400_BAD_REQUEST)

            # TODO: call merchants API: getPlayerInfo(private_token), return total balance

            return Response({'balance': 100})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['POST'])
# def deposit_view(request, *args, **kwargs):
#     """
#     post:
#         Депозит

#         -
#     """
#     serializer = DepositCreateSerializer(data=request.data)
#     if serializer.is_valid():

#         player = get_player_by_private_token(serializer.data['player_private_token'])

#         deposit = DepositSerializer(data={
#             'amount': serializer.data['amount'],
#             'player': player.id,
#             'currency': serializer.data['currency'],
#         })
#         if deposit.is_valid():
#             deposit.save()
#         else:
#             return Response(deposit.errors, status=status.HTTP_400_BAD_REQUEST)

#         # TODO: call merchants API: getPlayerInfo(private_token), return total balance

#         return Response({'balance': 100})

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


