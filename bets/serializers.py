from django.core.exceptions import ValidationError
from players.models import Player
from rest_framework import serializers

from bets.models import Bet
from rocket_game.settings import BETS_MAX_NUMBER


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['id', 'player', 'amount', 'game', 'round', 'currency']

    # def create(self, validated_data):
    #     validated_data['player'].active_bets += 1
    #     validated_data['player'].balance -= validated_data['amount']
    #     validated_data['player'].save()
    #     return super(BetSerializer, self).create(validated_data)

    # def validate(self, attrs):
    #     if attrs['player'].active_bets >= BETS_MAX_NUMBER:
    #         raise ValidationError("The player's maximum number of active bets has been exceeded")
    #     return attrs