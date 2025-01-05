from django.urls import path
from . import views

app_name = 'jewelry'

urlpatterns = [
    path('', views.jewelry_list, name='jewelry-list'),
    path('create/', views.jewelry_create, name='jewelry-create'),
    path('<int:pk>/', views.jewelry_detail, name='jewelry-detail'),
    path('<int:pk>/update/', views.jewelry_update, name='jewelry-update'),
    path('<int:pk>/delete/', views.jewelry_delete, name='jewelry-delete'),
    path('my_jewelry/', views.my_jewelry_list, name='my_jewelry'),
    path('<int:pk>/update_jewelry/', views.jewelry_update_by_staff, name='jewelry-update-jewelry-by-staff-or-manager'),
    path('<int:pk>/confirm_auction/', views.jewelry_confirm_auction, name='jewelry-confirm-auction'),
    path('<int:pk>/approve/', views.jewelry_approve, name='jewelry-approve'),
    path('<int:pk>/reject/', views.jewelry_reject, name='jewelry-reject'),
]