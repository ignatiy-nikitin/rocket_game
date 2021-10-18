from django.shortcuts import render

# Create your views here.
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

from rest_framework.permissions import IsAuthenticated


from rest_framework import mixins

from bets.models import Bet

from rest_framework.views import APIView

from rest_framework import generics, status

from players.services import get_player_by_private_token
from withdraws.serializers import WithdrawCreateSerializer, WithdrawSerializer

from withdraws.models import Withdraw


class WithdrawViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]
    queryset = Withdraw.objects.all()


class WithdrawAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = WithdrawCreateSerializer(data=request.data)
        if serializer.is_valid():

            player = get_player_by_private_token(serializer.data['player_private_token'])

            deposit = WithdrawSerializer(data={
                'amount': serializer.data['amount'],
                'player': player.id,
                'currency': serializer.data['currency'],
            })
            if deposit.is_valid():
                deposit.save()
            else:
                return Response(deposit.errors, status=status.HTTP_400_BAD_REQUEST)

            # TODO: call merchants API: getPlayerInfo(private_token), return total balance (-= amount)

            return Response({'balance': 100})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['POST'])
# def withdraw_view(request, *args, **kwargs):
#     """
#     post:
#         Депозит

#         -
#     """
#     serializer = WithdrawCreateSerializer(data=request.data)
#     if serializer.is_valid():

#         player = get_player_by_private_token(serializer.data['player_private_token'])

#         deposit = WithdrawSerializer(data={
#             'amount': serializer.data['amount'],
#             'player': player.id,
#             'currency': serializer.data['currency'],
#         })
#         if deposit.is_valid():
#             deposit.save()
#         else:
#             return Response(deposit.errors, status=status.HTTP_400_BAD_REQUEST)

#         # TODO: call merchants API: getPlayerInfo(private_token), return total balance (-= amount)

#         return Response({'balance': 100})

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
