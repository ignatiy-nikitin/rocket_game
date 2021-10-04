from rest_framework.routers import DefaultRouter

from players.views import PlayerViewSet

player_router = DefaultRouter()
player_router.register('', PlayerViewSet, basename='player')

urlpatterns = player_router.urls
