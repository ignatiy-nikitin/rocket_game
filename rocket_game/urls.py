from django.contrib import admin
from django.urls import path
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from rocket_game import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token

from players.views import bet_view, deposit_view, get_balance_view, withdraw_view

from rest_framework.routers import DefaultRouter, SimpleRouter

schema_view = get_schema_view(
    openapi.Info(
        title='ROCKET GAME API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from merchants import views as merchants_views
from deposits import views as deposits_views
from withdraws import views as withdraw_views


local_api_v1 = [
    path('admin/auth/login/', obtain_auth_token),
    path('admin/create_marchant/', merchants_views.MerchantCreateAPIView.as_view()),
]

router = SimpleRouter()
router.register('statistics/deposits', deposits_views.DepositViewSet, basename='statistics_deposit')
router.register('statistics/withdraws', withdraw_views.WithdrawViewSet, basename='statistics_withdraws')
local_api_v1 += router.urls


public_api_v1 = [
    # path('merchants/auth/login/', ...)
    path('login/', obtain_auth_token),
    path('auth/', merchants_views.MerchantAuthAPIView.as_view()),
    path('deposit/', deposits_views.DepositCreateAPIView.as_view()),
    path('withdraw/', withdraw_views.WithdrawAPIView.as_view())
]

urlpatterns_api_v1 = [
    # path('auth/login/', obtain_auth_token),

    # path('deposit/', deposit_view),
    # path('withdraw/', withdraw_view),
    # path('get_balance/', get_balance_view),
    # path('bet/', bet_view),

    path('public/', include(public_api_v1)),
    path('local/', include(local_api_v1)),

    # # path('players/', include(('players.urls', 'players'))),
    # # path('bets/', include(('bets.urls', 'bets'))),
    # # path('merchants/', include(('merchants.urls', 'merchants'))),
    # path('games/', include(('games.urls', 'games'))),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api_v1)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
