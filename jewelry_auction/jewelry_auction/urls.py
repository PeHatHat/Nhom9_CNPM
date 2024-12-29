from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core import views as core_views

schema_view = get_schema_view(
   openapi.Info(
      title="Jewelry Auction API",
      default_version='v1',
      description="API documentation for Jewelry Auction System",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('api/core/', include('core.urls')),
    path('api/jewelry/', include('jewelry.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/users/', include('users.urls')),
    path('api/bids/', include('bids.urls')),
    path('api/auctions/', include('auctions.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])