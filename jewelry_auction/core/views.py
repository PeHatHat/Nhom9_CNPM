from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import Auction
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from .models import Auction
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('home')  # Chuyển hướng đến trang chủ sau khi đăng ký
        else:
            messages.error(request, "Đã xảy ra lỗi, vui lòng kiểm tra lại thông tin")
    else:
        form = RegistrationForm()
    return render(request, 'core/user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Chào mừng {username}!")
                return redirect('home')  # Chuyển hướng đến trang chủ sau khi đăng nhập
            else:
                messages.error(request,"Tên đăng nhập hoặc mật khẩu không đúng.")
        else:
            messages.error(request, "Đã xảy ra lỗi, vui lòng kiểm tra lại thông tin")
    else:
        form = LoginForm()
    return render(request, 'core/user/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Đã đăng xuất!")
    return redirect('home')  # Chuyển hướng đến trang chủ sau khi đăng xuất

def home(request):
    return render(request, 'core/home.html')

def auction_list(request):
    now = timezone.now()
    auctions = Auction.objects.filter(status='open')

    # Lấy các tham số từ request để lọc (nếu có)
    search_query = request.GET.get('search', '')
    status = request.GET.get('status', '')
    sort_by = request.GET.get('sort', '')  # Thêm tham số sắp xếp

    # Lọc theo từ khóa tìm kiếm (nếu có)
    if search_query:
        auctions = auctions.filter(
            Q(jewelry__name__icontains=search_query) |  # Tìm theo tên trang sức
            Q(jewelry__description__icontains=search_query)  # Tìm theo mô tả trang sức
        )

    # Lọc theo trạng thái (nếu có)
    if status:
        auctions = auctions.filter(status=status)

    # Lọc theo role của user (Guest chỉ xem phiên đấu giá đang mở)
    if request.user.is_anonymous:
        auctions = auctions.filter(status='open')
    
    # Chỉ hiển thị các phiên đấu giá chưa kết thúc
    auctions = auctions.filter(end_time__gte=now)

    # Sắp xếp
    if sort_by == 'price_asc':
        auctions = auctions.order_by('jewelry__initial_price')
    elif sort_by == 'price_desc':
        auctions = auctions.order_by('-jewelry__initial_price')
    elif sort_by == 'end_time_asc':
        auctions = auctions.order_by('end_time')
    elif sort_by == 'end_time_desc':
        auctions = auctions.order_by('-end_time')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(auctions, 10)  # Hiển thị 10 phiên đấu giá trên mỗi trang
    try:
        auctions = paginator.page(page)
    except PageNotAnInteger:
        auctions = paginator.page(1)
    except EmptyPage:
        auctions = paginator.page(paginator.num_pages)

    context = {
        'auctions': auctions,
        'search_query': search_query,
        'status': status,
        'sort_by': sort_by,
    }
    return render(request, 'core/auction_list.html', context)