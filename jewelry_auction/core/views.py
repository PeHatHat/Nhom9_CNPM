from django.shortcuts import render
from blog.models import Blog
from jewelry.models import Jewelry
from notifications.models import Notification

def home(request):
    # Lấy danh sách bài viết mới nhất, giới hạn 10 bài
    blog_posts = Blog.objects.all().order_by('-publication_date')[:10]

    # Lấy danh sách trang sức đấu giá, giới hạn 10, lọc theo trạng thái
    jewelry_products = Jewelry.objects.filter(status__in=['APPROVED', 'AUCTIONING', 'NO_BIDS']).order_by('-jewelry_id')[:10]

    # Truyền dữ liệu vào context
    context = {
        'blog_posts': blog_posts,
        'jewelry_products': jewelry_products,
    }
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def policy(request):
    return render(request, 'core/policy.html')

def get_unread_notifications_count(user):
    if user.is_authenticated:
        return user.notifications.filter(is_read=False).count()
    else:
        return 0