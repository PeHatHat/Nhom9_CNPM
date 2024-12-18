from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

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