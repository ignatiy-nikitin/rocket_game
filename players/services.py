from players.models import Player


def get_player_by_private_token(private_token):
    return Player.objects.get(private_token=private_token)
