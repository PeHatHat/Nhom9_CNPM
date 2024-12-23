
# Hướng Dẫn Cài Đặt và Sử Dụng - Jewelry Auction System

File này cung cấp hướng dẫn chi tiết để cài đặt, cấu hình và sử dụng hệ thống đấu giá trang sức trực tuyến **Jewelry Auction System**.

## Cài Đặt

### 1. Clone Repository


```git clone https://github.com/HieuPT2212/Nhom9_CNPM.git```

```cd Nhom9_CNPM```

Thay <URL_repository_Nhom9_CNPM> bằng URL của repository này.

### 2. Tạo và Kích Hoạt Môi Trường Ảo

Nếu bạn chưa có môi trường ảo:

Trên Windows:

```python -m venv .venv```

```.venv\Scripts\activate```

Lưu ý: Nên Command Prompt

Trên macOS/Linux:

```python3 -m venv .venv```

```.venv/bin/activate```


### 3. Cài Đặt Dependencies

```pip install -r requirements.txt```

### 4. Thiết Lập Cơ Sở Dữ Liệu

#### a. Tạo Database

Mở MySQL Workbench

Kết nối đến MySQL Server.

Tạo một database mới với tên jewelry_auction ( nếu lần đầu)

##### b. Export/Import Dữ Liệu Mẫu(Mỗi lần dùng là 1 lần import/export )

Export:

```mysqldump -u user -p jewelry_auction > jewelry_auction_data.sql```

Import:

```mysql -u root -p jewelry_auction < jewelry_auction_data.sql```

Áp dụng các migrations đó vào database local:(mỗi lần)

```python manage.py migrate```

```python manage.py makemigrations```


Lưu ý: Cần cài biến môi trường cho mySQL

Thay [root] bằng username MySQL của bạn và nhập password khi được yêu cầu.

Nhớ chạy makemigrations(export) và migrate(import) mỗi khi bạn thay đổi models để giữ cho database và code đồng bộ.

### 5. Cấu Hình settings.py

Mở file jewelry_auction/settings.py.

Cấu hình phần DATABASES để kết nối với database MySQL trên máy của bạn:

```
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

Thay your_mysql_username và your_mysql_password bằng thông tin đăng nhập MySQL của bạn. 

Không commit mật khẩu lên repository.

### Cách Chạy Server
```python manage.py runserver```

Mở trình duyệt và truy cập địa chỉ http://127.0.0.1:8000/ để kiểm tra.

Đăng nhập vào trang admin (http://127.0.0.1:8000/admin) với tài khoản superuser đã được tạo trong jewelry_auction_data.sql (liên hệ nhóm trưởng để biết thông tin đăng nhập).

