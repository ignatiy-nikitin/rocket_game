from django.shortcuts import redirect, render
from rest_framework import serializers, viewsets
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


    # @action(detail=True, methods=['get'])
    # def bets(self, request, pk=None):
    #     bets = Bet.objects.filter(player_id=pk).order_by('-id')
    #     response = [BetSerializer(bet).data for bet in bets]
    #     return Response(response)

    # @action(detail=True, methods=['get'])
    # def bets_active(self, request, pk=None):
    #     bets = Bet.objects.filter(player_id=pk, status='active').order_by('-id')
    #     response = [BetSerializer(bet).data for bet in bets]
    #     return Response(response)

    @action(detail=False, methods=['post'])
    def deposit(self, request, pk=None):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            player = Player.objects.filter(id_ms=serializer.data['user_id'])
            if not player.exists():
                player = Player.objects.create(id_ms=serializer.data['user_id'])
            player = Player.objects.get(id_ms=serializer.data['user_id'])
            player.token = serializer.data['token']
            player.balance += serializer.data['amount']
            player.save()
            return Response(
                {
                    "balance": player.balance
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def withdraw(self, request, pk=None):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            player = Player.objects.filter(id_ms=serializer.data['user_id'])
            if not player.exists():
                player = Player.objects.create(id_ms=serializer.data['user_id'])
            player = Player.objects.get(id_ms=serializer.data['user_id'])
            player.token = serializer.data['token']
            player.balance += serializer.data['amount']
            player.save()
            return Response(
                {
                    "balance": player.balance
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @action(detail=True, methods=['get'])
    # def betss(self, request, pk=None):
    #     bets = Bet.objects.filter(user=self.kwargs['id'])
    #     return Response(self.get_serializer(bets).data)


from rest_framework.decorators import api_view

@api_view(http_method_names=['POST'])
def deposit_view(request, *args, **kwargs):
    """
    post:
        Внести

        -
    """
    serializer = DepositSerializer(data=request.data)
    if serializer.is_valid():
        player = Player.objects.filter(id_ms=serializer.data['user_id'])
        if not player.exists():
            player = Player.objects.create(id_ms=serializer.data['user_id'], merchant_id=serializer.data['merchant_id'])
        player = Player.objects.get(id_ms=serializer.data['user_id'])
        player.token = serializer.data['token']
        player.balance += serializer.data['amount']
        player.save()
        return Response(
            {
                "balance": player.balance
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def withdraw_view(request, *args, **kwargs):
    """
    post:
        Снять

        -
    """
    serializer = WithdrawSerializer(data=request.data)
    if serializer.is_valid():
        player = Player.objects.filter(id_ms=serializer.data['user_id'])
        if not player.exists():
            player = Player.objects.create(id_ms=serializer.data['user_id'], merchant_id=serializer.data['merchant_id'])
        player = Player.objects.get(id_ms=serializer.data['user_id'])
        player.token = serializer.data['token']
        player.balance -= serializer.data['amount']
        player.save()
        return Response(
            {
                "balance": player.balance
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def get_balance_view(request, *args, **kwargs):
    """
    post:
        Получить баланс

        -
    """
    serializer = GetBalanceSerializer(data=request.data)
    if serializer.is_valid():
        player = Player.objects.filter(id_ms=serializer.data['user_id'])
        if not player.exists():
            player = Player.objects.create(id_ms=serializer.data['user_id'], merchant_id=serializer.data['merchant_id'])
        player = Player.objects.get(id_ms=serializer.data['user_id'])
        player.token = serializer.data['token']
        player.save()
        return Response(
            {
                "balance": player.balance
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def bet_view(request, *args, **kwargs):
    """
    post:
        Сделать ставку

        -
    """
    serializer = BetSerializer(data=request.data)
    if serializer.is_valid():
        player = Player.objects.filter(merchant_id=serializer.data['merchant_id'], token=serializer.data['token'])
        # TODO: сделать ставку
        if not player.exists():
            player = Player.objects.create(id_ms=serializer.data['user_id'], merchant_id=serializer.data['merchant_id'])
        player.balance -= serializer.data['amount']
        player.save()
        return Response(
            {
                "balance": player.balance
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------


@api_view(http_method_names=['POST'])
def deposit_view(request, *args, **kwargs):
    """
    post:
        Депозит

        -
    """
    serializer = MerchantAuthSerializer(data=request.data)
    if serializer.is_valid():
        player_id = serializer.data['player_id']
        merchant_auth_token = serializer.data['merchant_auth_token']
        player_private_token = serializer.data['player_private_token']

        merchant = get_merchant_by_auth_token(merchant_auth_token)

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