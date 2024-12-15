Tôi hiểu rồi. Dưới đây là file HELP.md với toàn bộ các bước cài đặt, từ clone repository đến chạy server, đều nằm trong các code block để bạn có thể dễ dàng copy:

# Hướng Dẫn Cài Đặt và Sử Dụng - Jewelry Auction System

File này cung cấp hướng dẫn chi tiết để cài đặt, cấu hình và sử dụng hệ thống đấu giá trang sức trực tuyến **Jewelry Auction System**.

## Cài Đặt

### 1. Clone Repository


git clone <URL_repository_Nhom9_CNPM>
cd Nhom9_CNPM

Thay <URL_repository_Nhom9_CNPM> bằng URL của repository này.

### 2. Tạo và Kích Hoạt Môi Trường Ảo

Nếu bạn chưa có môi trường ảo:

Trên Windows:

python -m venv .venv

.venv\Scripts\activate

Trên macOS/Linux:

python3 -m venv .venv

source .venv/bin/activate


### 3. Cài Đặt Dependencies

pip install -r requirements.txt

### 4. Thiết Lập Cơ Sở Dữ Liệu

#### a. Tạo Database

Mở MySQL Workbench

Kết nối đến MySQL Server.

Tạo một database mới với tên jewelry_auction

##### b. Import Dữ Liệu Mẫu
cd Nhom9_CNPM

mysql -u [username] -p jewelry_auction < data.sql

Thay [username] bằng username MySQL của bạn và nhập password khi được yêu cầu.

### 5. Cấu Hình settings.py

Mở file jewelry_auction/settings.py.

Cấu hình phần DATABASES để kết nối với database MySQL trên máy của bạn:

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


Lưu ý: Thay your_mysql_username và your_mysql_password bằng thông tin đăng nhập MySQL của bạn. Không commit mật khẩu lên repository.

### Cách Chạy Server
python manage.py runserver

Mở trình duyệt và truy cập địa chỉ http://127.0.0.1:8000/ để kiểm tra.

Đăng nhập vào trang admin (http://127.0.0.1:8000/admin) với tài khoản superuser đã được tạo trong file data.sql (liên hệ nhóm trưởng để biết thông tin đăng nhập).

