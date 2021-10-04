from rest_framework.routers import DefaultRouter

from bets.views import BetViewSet
from django.urls import path

bet_router = DefaultRouter()
bet_router.register('', BetViewSet, basename='bet')

urlpatterns = bet_router.urls


# urlpatterns = [
#     path('', BetViewSet.as_view(), name='bet')
# ]
