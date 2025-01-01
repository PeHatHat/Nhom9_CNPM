from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'auctions'

router = DefaultRouter()
router.register(r'', views.AuctionViewSet, basename='auction')

urlpatterns = [
    path('', include(router.urls)),
    path('create/<int:jewelry_id>/', views.AuctionViewSet.as_view({'post': 'create'}), name='auction-create'),
    path('<int:pk>/cancel/', views.AuctionViewSet.as_view({'patch': 'cancel_auction'}), name='auction-cancel'),
]