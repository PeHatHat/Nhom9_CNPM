from django.urls import path
from core import views
from .dashboard_views import dashboard

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('dashboard/', dashboard, name='dashboard'),
]