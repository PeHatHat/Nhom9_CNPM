from django.urls import path
from . import views

app_name = 'auctions'

urlpatterns = [
    path('', views.auction_list, name='auction-list'),
    path('create/', views.auction_create, name='auction-create'),
    path('<int:pk>/', views.auction_detail, name='auction-detail'),
    path('<int:pk>/update/', views.auction_update, name='auction-update'),
    path('<int:pk>/delete/', views.auction_delete, name='auction-delete'),
    path('<int:pk>/cancel/', views.auction_cancel, name='auction-cancel'),
]