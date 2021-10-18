from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from merchants.views import MerchantAuthView, MerchantCreateUpdateViewSet

from players.views import  PlayerViewSet


router = SimpleRouter()
router.register('', MerchantCreateUpdateViewSet, basename='merchant')

urlpatterns = [
    path('auth/', MerchantAuthView.as_view()),
]

urlpatterns += router.urls
