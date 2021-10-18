from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from games.views import GameViewSet
from games.views import GameViewSet

from players.views import  PlayerViewSet


router = SimpleRouter()
router.register('', GameViewSet, basename='game')

urlpatterns = router.urls
