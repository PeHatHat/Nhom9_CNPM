from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Bao gồm URL của core app
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('jewelry/', include('jewelry.urls')),
    path('auctions/', include('auctions.urls')),
    path('bids/', include('bids.urls')),
    path('notifications/', include('notifications.urls')),
    path('transactions/', include('transactions.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)