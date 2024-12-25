# Hướng Dẫn Cài Đặt và Sử Dụng - Jewelry Auction System

File này cung cấp hướng dẫn chi tiết để cài đặt, cấu hình và sử dụng hệ thống đấu giá trang sức trực tuyến **Jewelry Auction System**.

## Cài Đặt

### 1. Clone Repository

`git clone https://github.com/HieuPT2212/Nhom9_CNPM.git`

`cd Nhom9_CNPM`

### 2. Tạo và Kích Hoạt Môi Trường Ảo

Trên Windows:

`python -m venv .venv`

`.venv\Scripts\activate`

Lưu ý: Nên dùng Command Prompt

Trên macOS/Linux:

`python3 -m venv .venv`

`.venv/bin/activate`

### 3. Cài Đặt Dependencies( Thư viện cần cho dự án)

`pip install -r requirements.txt`

### 4. Thiết Lập Cơ Sở Dữ Liệu

#### a. Tạo Database

1.Mở MySQL Workbench

2.Kết nối đến MySQL Server.

Tạo một database mới với tên jewelry_auction ( nếu lần đầu)

##### b. Đồng bộ dữ liệu mẫu

Áp dụng các migrations đó vào database local mỗi khi thay đổi models hoặc lần đầu chạy dự án:

1.`python manage.py makemigrations`

2.`python manage.py migrate`

Lưu ý: Cần cài biến môi trường cho mySQL.

Nhớ chạy makemigrations(export các models) và migrate(import các models) mỗi khi bạn thay đổi models để giữ cho database và code đồng bộ.

### 5. Cấu Hình settings.py

Mở file jewelry_auction/settings.py.

Cấu hình phần DATABASES để kết nối với database MySQL trên máy của bạn:

```python
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'jewelry_auction',  # Tên database

        'USER': 'your_mysql_username',  # Username MySQL của bạn

        'PASSWORD': 'your_mysql_password',  # Password MySQL của bạn

        'HOST': 'localhost',  # Hoặc IP address của MySQL server

        'PORT': '3306',  # Cổng mặc định của MySQL

    }

}
```

Lưu ý:

Thay your_password bằng thông tin đăng nhập MySQL của bạn.

Không commit mật khẩu lên repository.

### Cách Chạy Server

`python manage.py runserver`

Mở trình duyệt và truy cập địa chỉ [http://127.0.0.1:8000/] để kiểm tra.

Đăng nhập vào trang admin [http://127.0.0.1:8000/admin] với tài khoản superuser đã được tạo trong jewelry_auction_data.sql (liên hệ nhóm trưởng để biết thông tin đăng nhập).

### Front-end

tạo và chỉnh sửa các file FE trong thư mục templates:

- Trang chủ: index.html

- Trang đăng nhập: login.html

- Trang đăng ký: register.html

- Trang cá nhân: profile.html