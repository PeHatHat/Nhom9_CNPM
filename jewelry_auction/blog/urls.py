from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog-list'),
    path('create/', views.blog_create, name='blog-create'),
    path('<int:pk>/', views.blog_detail, name='blog-detail'),
    path('<int:pk>/approve/', views.blog_approve, name='blog-approve'),
    path('<int:pk>/reject/', views.blog_reject, name='blog-reject'),
    path('pending/', views.blog_pending_list, name='blog-pending-list'),
]