from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'nickname', 'token', 'provider', 'balance', 'active_bets']

    def create(self, validated_data):
        if Player.objects.filter(token=validated_data['token']).exists():
            player = Player.objects.get(token=validated_data['token'])
            return self.update(player, validated_data)
        return Player.objects.create(**validated_data)
