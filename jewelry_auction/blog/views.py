from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-publication_date')
    search_query = request.GET.get('search')
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)

    # Sắp xếp
    sort_by = request.GET.get('ordering')
    if sort_by:
        blogs = blogs.order_by(sort_by)

    context = {'blogs': blogs}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)