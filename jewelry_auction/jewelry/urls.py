from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'', views.JewelryViewSet, basename='jewelry')

app_name = 'jewelry'

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/update_jewelry/', views.JewelryViewSet.as_view({'patch': 'update_jewelry'}), name='jewelry-update-jewelry'),
    path('<int:pk>/confirm_auction/', views.JewelryViewSet.as_view({'patch': 'confirm_auction'}), name='jewelry-confirm-auction'),
]