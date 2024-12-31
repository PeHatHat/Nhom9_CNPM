from . import views
from django.urls import path

app_name = 'jewelry'

urlpatterns = [
    path('', views.JewelryViewSet.as_view({'get': 'list'}), name='jewelry-list'),
    path('<int:pk>/', views.JewelryViewSet.as_view({'get': 'retrieve'}), name='jewelry-detail'),
    path('create/', views.JewelryViewSet.as_view({'post': 'create'}), name='jewelry-create'),
    path('my-jewelry/', views.JewelryViewSet.as_view({'get': 'my_jewelry'}), name='my-jewelry'),
]