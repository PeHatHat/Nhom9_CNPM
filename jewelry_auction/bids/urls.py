from django.urls import path
from . import views

app_name = 'bids'

urlpatterns = [
    path('place/<int:auction_id>/', views.place_bid, name='place_bid'),
    path('my-bids/', views.UserBidsList.as_view(), name='user_bids'),
]