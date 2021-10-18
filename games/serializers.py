from rest_framework import serializers
from games.models import Game
from merchants.services import generate_token


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name']
        read_only_fields = ['id']
