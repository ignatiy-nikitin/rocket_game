from django.shortcuts import render
from rest_framework import viewsets
from players.models import Player
from players.serializers import PlayerSerializer


from rest_framework import mixins 


# Create your views here.
class PlayerViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        Создать игрока

        Создает игрока с данными от провайдера


    retrieve:
        Получить информацию о игроке

        -

    '''
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
