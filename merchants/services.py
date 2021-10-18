import binascii
import os

from merchants.models import Merchant


def generate_token(all_tokens):
    """Сгенерировать токен"""
    token_length = 20
    while True:
        token = binascii.hexlify(os.urandom(token_length)).decode()
        if token not in all_tokens:
            return token


def get_merchant_by_auth_token(auth_token):
    return Merchant.objects.get(auth_token=auth_token)
