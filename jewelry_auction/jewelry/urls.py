from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'jewelry'

urlpatterns = [
    path('create/', views.create_jewelry, name='create_jewelry'),
    path('my-jewelry/', views.MyJewelryList.as_view(), name='my_jewelry'),
]

router = DefaultRouter()
router.register(r'staff', views.StaffJewelryViewSet, basename='staff_jewelry')
router.register(r'', views.JewelryViewSet, basename='jewelry')

urlpatterns += router.urls