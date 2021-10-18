from django.core.exceptions import ValidationError
from rest_framework import serializers
from games.models import Game
from games.serializers import GameSerializer
from merchants.models import Merchant
from merchants.services import generate_token, get_merchant_by_auth_token
from deposits.models import Deposit
from players.services import get_player_by_private_token


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id', 'amount', 'player', 'currency', 'creation_datetime']
        read_only_fields = ['id', 'creation_datetime']

    # def create(self, validated_data):
    #     all_tokens = [merchant.auth_token for merchant in Merchant.objects.all()]
    #     validated_data['auth_token'] = generate_token(all_tokens)
    #     return super(MerchantSerializer, self).create(validated_data)


class DepositCreateSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    # merchant_auth_token = serializers.CharField()
    player_private_token = serializers.CharField()
    player_id = serializers.IntegerField()
    currency = serializers.CharField()


    # def validate(self, attrs):
    #     merchant = get_merchant_by_auth_token(attrs['merchant_auth_token'])
    #     # get by player_id, check if exists
    #     return attrs