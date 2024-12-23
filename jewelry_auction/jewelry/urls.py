from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.JewelryViewSet, basename='jewelry')

urlpatterns = router.urls