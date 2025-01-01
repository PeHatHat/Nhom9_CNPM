from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationList.as_view(), name='notification-list'),
    path('<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
]