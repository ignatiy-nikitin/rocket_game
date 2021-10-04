from django.contrib import admin
from django.urls import path
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from rocket_game import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title='ROCKET GAME API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns_api_v1 = [
    path('players/', include(('players.urls', 'players'))),
    path('bets/', include(('bets.urls', 'bets'))),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api_v1)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
