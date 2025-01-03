from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.transaction_list, name='transaction-list'),
    path('<int:pk>/', views.transaction_detail, name='transaction-detail'),
]