from django.core.exceptions import ValidationError
from django.db.models import query
from django.db.models.fields import IntegerField
from rest_framework import serializers
from games.serializers import GameSerializer
from merchants.models import Merchant
from players.models import Player

from games.models import Game


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'merchant', 'id_ms']

    def create(self, validated_data):
        if Player.objects.filter(token=validated_data['token']).exists():
            player = Player.objects.get(token=validated_data['token'])
            return self.update(player, validated_data)
        return Player.objects.create(**validated_data)



# class DepositSerializer(serializers.Serializer):
#     amount = serializers.IntegerField()
#     merchant_id = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())
#     token = serializers.CharField(max_length=256)
#     user_id = serializers.IntegerField()


class WithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    merchant_id = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())
    token = serializers.CharField(max_length=256)
    user_id = serializers.IntegerField()


class GetBalanceSerializer(serializers.Serializer):
    merchant_id = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())
    token = serializers.CharField(max_length=256)
    user_id = serializers.IntegerField()


class BetSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=256)
    amount = serializers.IntegerField()
    # betTypeId
    merchant_id = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())
    game_id = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    round_id = IntegerField()

    def validate(self, attrs):
        player = Player.objects.filter(merchant_id=attrs['merchant_id'], token=attrs['token'])
        if not player.exists():
            token = attrs['token']
            raise ValidationError(f'Can not find player with token: {token}')
        return attrs

# ------