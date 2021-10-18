import re
from django.shortcuts import redirect, render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bets.serializers import BetSerializer
from bets.views import BetViewSet
from merchants.models import Merchant
from merchants.serializers import MerchantAuthSerializer, MerchantSerializer
from merchants.services import get_merchant_by_auth_token
from players.models import Player
from players.serializers import PlayerSerializer

from rest_framework.decorators import action, api_view

from rest_framework.permissions import IsAuthenticated


from rest_framework import mixins

from bets.models import Bet

from rest_framework.views import APIView

from rest_framework import generics, status


class MerchantCreateUpdateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]
    queryset = Merchant.objects.all()


class MerchantAuthView(APIView):
    # serializer_class = MerchantAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = MerchantAuthSerializer(data=request.data)
        if serializer.is_valid():
            # request.session[... ]
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @api_view(http_method_names=['POST'])
# def auth_login_view(request, *args, **kwargs):
#     """
#     post:
#         Авторизия партнера

#         -
#     """
#     serializer = MerchantAuthSerializer(data=request.data)
#     if serializer.is_valid():
#         # request.session[... ]
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchantCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['POST'])
# def create_merchant_view(request, *args, **kwargs):
#     """
#     post:
#         Создать партнера

#         -
#     """
#     serializer = MerchantSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\


class MerchantAuthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MerchantAuthSerializer(data=request.data)
        if serializer.is_valid():
            player_id = serializer.data['player_id']
            # merchant_auth_token = serializer.data['merchant_auth_token']
            player_private_token = serializer.data['player_private_token']

            # merchant = get_merchant_by_auth_token(merchant_auth_token)
            merchant = request.user

            player = Player.objects.filter(merchant=merchant, id_ms=player_id)
            if not player.exists():
                player = Player.objects.create(id_ms=player_id, merchant=merchant)
            else:
                player = player[0]


            player.private_token = player_private_token
            player.save()

            return Response(
                {
                    'id': player.id,
                    'id_ms': player.id_ms,
                    'merchant_id': player.merchant.id
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['POST'])
# def auth_view(request, *args, **kwargs):
#     """
#     post:
#         Старт игры

#         -
#     """
#     serializer = MerchantAuthSerializer(data=request.data)
#     if serializer.is_valid():
#         player_id = serializer.data['player_id']
#         merchant_auth_token = serializer.data['merchant_auth_token']
#         player_private_token = serializer.data['player_private_token']

#         merchant = get_merchant_by_auth_token(merchant_auth_token)

#         player = Player.objects.filter(merchant=merchant, id_ms=player_id)
#         if not player.exists():
#             player = Player.objects.create(id_ms=player_id, merchant=merchant)
#         else:
#             player = player[0]


#         player.private_token = player_private_token
#         player.save()

#         return Response(
#             {
#                 'id': player.id,
#                 'id_ms': player.id_ms,
#                 'merchant_id': player.merchant.id
#             }
#         )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
