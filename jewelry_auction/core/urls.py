from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'fee-configuration', views.FeeConfigurationViewSet, basename='fee-configuration')
urlpatterns = [
    path('', include(router.urls)),
    path('manage-jcoin/<int:user_id>/', views.FeeConfigurationViewSet.as_view({'put': 'manage_jcoin'}), name='manage_jcoin'),
]