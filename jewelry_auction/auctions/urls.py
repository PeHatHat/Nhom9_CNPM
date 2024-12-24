from django.urls import path
from . import views

app_name = 'auctions'

urlpatterns = [
    path('', views.AuctionList.as_view(), name='auction_list'),
    path('<int:pk>/', views.AuctionDetail.as_view(), name='auction_detail'),
    path('create/<int:jewelry_id>/', views.create_auction, name='create_auction'),
]