from .views import get_unread_notifications_count

def unread_notifications(request):
    return {'unread_notifications_count': get_unread_notifications_count(request.user)}