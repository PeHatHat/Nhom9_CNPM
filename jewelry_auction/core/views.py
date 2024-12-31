from django.shortcuts import render
import requests
from django.conf import settings

def home(request):
    # Lấy danh sách bài viết từ API
    blog_response = requests.get(f'{settings.BASE_URL}/api/blogs/')
    blog_posts = blog_response.json() if blog_response.status_code == 200 else []

    # Lấy danh sách trang sức từ API
    jewelry_response = requests.get(f'{settings.BASE_URL}/api/jewelry/')
    jewelry_products = jewelry_response.json() if jewelry_response.status_code == 200 else []

    # Truyền dữ liệu vào context
    context = {
        'blog_posts': blog_posts,
        'jewelry_products': jewelry_products,
    }

    return render(request, 'core/index.html', context)