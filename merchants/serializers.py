from django.core.exceptions import ValidationError
from rest_framework import serializers
from games.models import Game
from games.serializers import GameSerializer
from merchants.models import Merchant
from merchants.services import generate_token
from players.serializers import PlayerSerializer


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['id', 'username', 'password', 'name', 'date_joined']
        read_only_fields = ['id', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # all_tokens = [merchant.auth_token for merchant in Merchant.objects.all()]
        # validated_data['auth_token'] = generate_token(all_tokens)
        merchant = Merchant(
            username=validated_data['username'],
            name=validated_data['name'],
        )
        merchant.set_password(validated_data['password'])
        merchant.save()
        return merchant


class MerchantAuthSerializer(serializers.Serializer):
    # merchant_auth_token = serializers.CharField(max_length=256)
    player_id = serializers.IntegerField()
    player_private_token = serializers.CharField(max_length=256)

    # token = serializers.CharField(max_length=256)
    # game_id = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    # player = PlayerSerializer()
    # platform = serializers.ChoiceField(choices=[
    #     ('desktop', 'desktop'),
    #     ('mobile', 'mobile')
    # ])

    # def validate(self, attrs):
    #     merchant_auth_token = attrs['merchant_auth_token']
    #     merchant = Merchant.objects.filter(auth_token=merchant_auth_token)
    #     if not merchant.exists():
    #         raise ValidationError(f'Merchant does not exists with token: {merchant_auth_token}')
    #     return attrs


# class MerchantAuthLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Merchant
#         fields = ['login', 'password']

#     def validate(self, attrs):
#         return super().validate(attrs)