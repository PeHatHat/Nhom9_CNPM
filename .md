Ok, tôi sẽ giải thích rõ hơn về đoạn cấu hình Swagger Schema View và hướng dẫn bạn cách dùng Postman để test API.

### Cấu hình Swagger Schema View

Đoạn code này dùng để cấu hình `schema_view` - một thành phần của thư viện `drf-yasg` giúp tạo ra tài liệu API (dưới dạng Swagger UI hoặc Redoc). Bạn **không cần phải chỉnh sửa nhiều** trong phần này, chủ yếu là thay đổi các thông tin cho phù hợp với dự án của bạn.

Đây là đoạn code đó:

```python
schema_view = get_schema_view(
   openapi.Info(
      title="Jewelry Auction API",
      default_version='v1',
      description="API documentation for Jewelry Auction System",
      terms_of_service="https://www.yourapp.com/terms/", # Thay bằng URL terms of service của bạn
      contact=openapi.Contact(email="contact@yourapp.com"), # Thay bằng email của bạn
      license=openapi.License(name="Your License"), # Thay bằng license của bạn
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
```

**Giải thích từng phần:**

*   **`get_schema_view(...)`:** Hàm này tạo ra một view (hiểu đơn giản là một thành phần xử lý request) để hiển thị tài liệu API.
*   **`openapi.Info(...)`:**  Chứa các thông tin metadata về API của bạn.
    *   **`title`:** Tiêu đề của API (bạn có thể giữ nguyên hoặc thay đổi).
    *   **`default_version`:** Phiên bản API (bạn có thể giữ nguyên).
    *   **`description`:** Mô tả API (bạn có thể giữ nguyên hoặc thay đổi).
    *   **`terms_of_service`:** URL đến trang điều khoản sử dụng của API (bạn cần thay bằng URL của bạn, hoặc xóa dòng này nếu không có).
    *   **`contact`:** Thông tin liên hệ (bạn nên thay `email` bằng email của bạn hoặc của nhóm).
    *   **`license`:** Giấy phép sử dụng API (bạn nên thay `name` bằng tên giấy phép bạn sử dụng, ví dụ: "MIT License", "Apache License 2.0", hoặc xóa dòng này nếu không có).
*   **`public=True`:** Cho phép truy cập tài liệu API mà không cần xác thực.
*   **`permission_classes=(permissions.AllowAny,)`:**  Cho phép bất kỳ ai cũng có thể xem tài liệu API.

**Tóm lại, bạn chỉ cần thay đổi các thông tin trong `openapi.Info(...)` cho phù hợp, đặc biệt là `terms_of_service`, `contact`, và `license`. Nếu không có các thông tin này, bạn có thể xóa các dòng tương ứng.**

### Hướng dẫn sử dụng Postman

Postman là một công cụ phổ biến để test API. Dưới đây là hướng dẫn cơ bản để bạn bắt đầu:

**1. Tải và cài đặt Postman:**

*   Truy cập trang web của Postman: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
*   Tải phiên bản phù hợp với hệ điều hành của bạn và cài đặt.

**2. Giao diện Postman:**

*   **Sidebar (bên trái):** Chứa các Collections (tập hợp các request), History (lịch sử request).
*   **Builder (ở giữa):** Nơi bạn xây dựng request (chọn method, nhập URL, header, body, v.v.).
*   **Response (bên phải):** Hiển thị response trả về từ API.

**3. Tạo một request mới:**

*   Nhấn vào nút "**+**" ở tab mới hoặc chọn "**New**" -> "**Request**" từ sidebar.
*   Đặt tên cho request (ví dụ: "Get Jewelry List").

**4. Cấu hình request:**

*   **Method:** Chọn phương thức HTTP (GET, POST, PUT, PATCH, DELETE, v.v.).
*   **URL:** Nhập URL của API endpoint (ví dụ: `http://127.0.0.1:8000/api/jewelry/`).
*   **Params:** Thêm các query parameters (nếu có), ví dụ: `search=diamond`, `sort=-initial_price`.
*   **Headers:** Thêm các header (nếu cần), ví dụ: `Authorization` (cho authentication).
*   **Body:** Nhập dữ liệu cần gửi đi (nếu là POST, PUT, PATCH), thường là JSON.
    *   Chọn "raw" và chọn "JSON" từ dropdown.
    *   Nhập dữ liệu JSON vào, ví dụ:

        ```json
        {
            "username": "testuser",
            "password": "testpassword"
        }
        ```

**5. Gửi request:**

*   Nhấn nút "**Send**".

**6. Xem response:**

*   **Status code:** Mã trạng thái HTTP (ví dụ: 200 OK, 400 Bad Request, 404 Not Found).
*   **Body:** Nội dung response trả về (thường là JSON).
*   **Headers:** Các header của response.
*   **Time:** Thời gian thực thi request.

**Ví dụ test API `GET /api/jewelry/`:**

1. Mở Postman, tạo request mới.
2. Chọn method **GET**.
3. Nhập URL: `http://127.0.0.1:8000/api/jewelry/`
4. (Optional) Thêm Params:
    *   `search`: `diamond`
    *   `sort`: `-initial_price`
5. Nhấn **Send**.
6. Xem response: Bạn sẽ thấy danh sách trang sức trả về dưới dạng JSON.

**Ví dụ test API `POST /api/users/register/`:**

1. Mở Postman, tạo request mới.
2. Chọn method **POST**.
3. Nhập URL: `http://127.0.0.1:8000/api/users/register/`
4. Chọn **Body**, chọn "raw" và "JSON".
5. Nhập JSON data:

    ```json
    {
        "username": "testuser2",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword",
        "password_confirm": "testpassword"
    }
    ```
6. Nhấn **Send**.
7. Xem response: Nếu thành công, bạn sẽ thấy thông tin user đã đăng ký (status code 201 Created). Nếu lỗi, bạn sẽ thấy thông báo lỗi tương ứng.

**Làm quen với Postman:**

*   Hãy thử nghiệm với các API khác mà bạn đã tạo.
*   Tạo các Collections để nhóm các request liên quan lại với nhau.
*   Lưu các request để sử dụng lại sau này.
*   Khám phá các tính năng khác của Postman như: Environments, Variables, Tests, v.v.

Postman là một công cụ rất hữu ích, bạn nên dành thời gian để tìm hiểu thêm về nó. Nếu bạn có bất kỳ câu hỏi nào, đừng ngần ngại hỏi tôi!
