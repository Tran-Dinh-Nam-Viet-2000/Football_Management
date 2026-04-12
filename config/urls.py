from django.urls import path, include
from rest_framework import permissions
from rest_framework.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Football Management API",
        default_version='v1',
        description="API quản lý đội bóng đá",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    # # Apps
    # path('api/', include('apps.users.urls')),
    # path('api/', include('apps.players.urls')),
    # path('api/', include('apps.teams.urls')),
    # path('api/', include('apps.matches.urls')),
]