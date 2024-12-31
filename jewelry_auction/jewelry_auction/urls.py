from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet
# from jewelry.views import JewelryViewSet # Xóa dòng này
from auctions.views import AuctionList, AuctionDetail, create_auction
from bids.views import place_bid, UserBidsList
from users.views import register, user_login, user_logout, profile

schema_view = get_schema_view(
    openapi.Info(
        title="Jewelry Auction API",
        default_version='v1',
        description="API for Jewelry Auction project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
# Xóa dòng này: 
# router.register(r'jewelry', JewelryViewSet, basename='jewelry')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/my-bids/', UserBidsList.as_view(), name='user-bids'),
    path('api/', include(router.urls)),
    path('api/auctions/', include('auctions.urls', namespace='auctions')),
    path('api/bids/', include('bids.urls', namespace='bids')),
    path('api/users/', include('users.urls', namespace='users')),
    path('api/jewelry/', include('jewelry.urls', namespace='jewelry')), # Giữ nguyên dòng này
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)