from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path

from players.views import  PlayerViewSet



router = SimpleRouter()
# router.register('<int:id>/bets', PlayerBetsViewSet, basename='player_bet')
# router.
router.register('', PlayerViewSet, basename='player')


# player_router = DefaultRouter()
# player_router.register('', PlayerViewSet, basename='player')

# player_router = DefaultRouter()
# player_router.register('', PlayerViewSet, basename='player')


# player_router = DefaultRouter()
# player_router.register('', PlayerViewSet, basename='player')


# paluer_router = DefaultRouter()
# player_router.register('', PlayerViewSet, basename='player')


# urlpatterns = [
#     path('users/<int:id>/', CartRetrieveAPIView.as_view(), name='cart')
# ]


urlpatterns = router.urls
