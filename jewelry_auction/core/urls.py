from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('db/backup/', views.backup_db, name='backup_db'),
    path('db/restore/', views.restore_db, name='restore_db'),
    
]