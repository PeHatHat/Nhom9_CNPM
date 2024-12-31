**I. Kế hoạch Test:**

1. **Chuẩn bị môi trường test:**
    *   Đảm bảo database test sạch sẽ (có thể dùng lệnh `python manage.py flush` **cẩn thận** hoặc tạo một database riêng cho test).
    *   Chạy server: `python manage.py runserver`
    *   Chuẩn bị sẵn các user với các role khác nhau: Admin, Manager, Staff, Member (có thể tạo qua trang admin hoặc viết script).
    *   Chuẩn bị sẵn một số data mẫu (có thể dùng file `fixtures` đã tạo hoặc tạo data qua API).
2. **Sử dụng Postman hoặc Insomnia:**
    *   Tạo các collection và folder để tổ chức các request API.
    *   Lưu lại các request để có thể sử dụng lại sau này.
3. **Test từng API theo từng role:**
    *   Thực hiện các test case cho từng API (bao gồm cả trường hợp thành công và thất bại).
    *   Kiểm tra response code, response body, và các thay đổi trong database (nếu có).
4. **Ghi lại kết quả test:**
    *   Ghi lại kết quả test (pass/fail) cho từng test case.
    *   Nếu có lỗi, ghi lại chi tiết lỗi (request, response, status code, ...) và báo cáo.
5. **Fix bug và retest:**
    *   Fix các bug được tìm thấy trong quá trình test.
    *   Chạy lại các test case để đảm bảo bug đã được fix và không có lỗi regression.

**II. Test Cases:**

**A. Guest:**

1. **`GET /api/jewelry/`**
    *   **TH1:** Không có parameters: Lấy tất cả trang sức (đã approved), kiểm tra phân trang.
    *   **TH2:** Tìm kiếm theo tên: `?search=<keyword>`
    *   **TH3:** Sắp xếp theo giá: `?ordering=initial_price`, `?ordering=-initial_price`
    *   **TH4:** Kết hợp filter, search, ordering.
2. **`GET /api/jewelry/<jewelry_id>/`**
    *   **TH1:** `jewelry_id` hợp lệ: Lấy thông tin chi tiết trang sức.
    *   **TH2:** `jewelry_id` không tồn tại: `404 Not Found`.
3. **`GET /api/blog/`**
    *   **TH1:** Không có parameters: Lấy tất cả bài blog.
    *   **TH2:** Tìm kiếm theo tiêu đề: `?search=<keyword>`
    *   **TH3:** Sắp xếp theo ngày đăng: `?ordering=publication_date`, `?ordering=-publication_date`
    *   **TH4:** Kết hợp filter, search, ordering.
4. **`GET /api/blog/<blog_id>/`**
    *   **TH1:** `blog_id` hợp lệ: Lấy thông tin chi tiết bài blog.
    *   **TH2:** `blog_id` không tồn tại: `404 Not Found`.

**B. Member:**

1. **`POST /api/users/register/`**
    *   **TH1:** Đăng ký thành công (đầy đủ thông tin hợp lệ).
    *   **TH2:** Thiếu thông tin: `400 Bad Request`.
    *   **TH3:** Username đã tồn tại: `400 Bad Request`.
    *   **TH4:** Mật khẩu không khớp: `400 Bad Request`.
2. **`POST /api/users/login/`**
    *   **TH1:** Đăng nhập thành công (đúng username/password).
    *   **TH2:** Sai username/password: `401 Unauthorized`.
3. **`GET /api/users/profile/`**
    *   **TH1:** User đã đăng nhập: Lấy thông tin cá nhân.
    *   **TH2:** User chưa đăng nhập: `401 Unauthorized`.
4. **`POST /api/users/logout/`**
    *   **TH1:** Đăng xuất thành công.
5. **`POST /api/bids/place/<auction_id>/`**
    *   **TH1:** Đặt giá thầu thành công (đủ JCoin, giá thầu hợp lệ).
    *   **TH2:** `auction_id` không tồn tại: `404 Not Found`.
    *   **TH3:** Phiên đấu giá đã đóng/bị hủy: `400 Bad Request`.
    *   **TH4:** Không đủ JCoin: `400 Bad Request`.
    *   **TH5:** Giá thầu thấp hơn giá cao nhất hiện tại: `400 Bad Request`.
    *   **TH6:** Giá thầu thấp hơn giá khởi điểm: `400 Bad Request`.
    *   **TH7:** User tự đặt giá thầu cho trang sức của mình: `400 Bad Request`.
    *   **TH8:** User chưa đăng nhập: `401 Unauthorized`
6. **`GET /api/auctions/`**
    *   **TH1:** Không có parameters: Lấy tất cả phiên đấu giá đang `OPEN` hoặc `CLOSED`.
    *   **TH2:** Lọc theo trạng thái: `?status=OPEN`, `?status=CLOSED`.
    *   **TH3:** Sắp xếp: `?ordering=start_time`, `?ordering=-end_time`.
    *   **TH4:** Lọc các phiên đấu giá user đã tham gia: `?my_auctions=true`
    *   **TH5:** User chưa đăng nhập: `401 Unauthorized`
7. **`GET /api/auctions/<auction_id>/`**
    *   **TH1:** `auction_id` hợp lệ: Lấy thông tin chi tiết phiên đấu giá, bao gồm `highest_bid`.
    *   **TH2:** `auction_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User chưa đăng nhập: `401 Unauthorized`
8. **`GET /api/users/my-bids/`**
    *   **TH1:** User đã đặt giá thầu: Lấy danh sách các giá thầu của user.
    *   **TH2:** User chưa đặt giá thầu: Lấy danh sách rỗng.
    *   **TH3:** User chưa đăng nhập: `401 Unauthorized`
9. **`POST /api/jewelry/create/`**
    *   **TH1:** Tạo trang sức thành công (đầy đủ thông tin hợp lệ).
    *   **TH2:** Thiếu thông tin: `400 Bad Request`.
    *   **TH3:** Sai định dạng ảnh: `400 Bad Request`.
    *   **TH4:** User không phải Member: `403 Forbidden`.
    *   **TH5:** User chưa đăng nhập: `401 Unauthorized`
10. **`GET /api/users/my-jewelry/`**
    *   **TH1:** User có trang sức: Lấy danh sách trang sức của user, kiểm tra thông báo.
    *   **TH2:** User không có trang sức: Lấy danh sách rỗng.
    *   **TH3:** User chưa đăng nhập: `401 Unauthorized`

**C. Staff:**

1. **`GET /api/jewelry/?is_approved=false`**
    *   **TH1:** Lấy danh sách trang sức chờ duyệt.
    *   **TH2:** User không phải Staff/Manager/Admin: `403 Forbidden`.
2. **`PATCH /api/jewelry/<jewelry_id>/approve/`**
    *   **TH1:** Duyệt thành công: `200 OK`.
    *   **TH2:** `jewelry_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Staff/Manager/Admin: `403 Forbidden`.
    *   **TH4:** Trang sức không ở trạng thái `PENDING`: `400 Bad Request`.
3. **`PATCH /api/jewelry/<jewelry_id>/reject/`**
    *   **TH1:** Từ chối thành công: `200 OK`.
    *   **TH2:** `jewelry_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Staff/Manager/Admin: `403 Forbidden`.
    *   **TH4:** Trang sức không ở trạng thái `PENDING`: `400 Bad Request`.

**D. Manager:**

1. **`POST /api/auctions/create/<jewelry_id>/`**
    *   **TH1:** Tạo thành công (đầy đủ thông tin, `start_time` < `end_time`).
    *   **TH2:** `jewelry_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Manager/Staff: `403 Forbidden`.
    *   **TH4:** Trang sức chưa được duyệt: `400 Bad Request`.
    *   **TH5:** Thiếu thông tin: `400 Bad Request`.
    *   **TH6:** `start_time` >= `end_time`: `400 Bad Request`.
2. **`GET /api/auctions/`**
    *   (Đã test ở phần Member)
3. **`GET /api/auctions/<auction_id>/`**
    *   (Đã test ở phần Member)
4. **`PUT /api/auctions/<auction_id>/`**
    *   **TH1:** Cập nhật thành công (đầy đủ thông tin hợp lệ).
    *   **TH2:** `auction_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Manager/Staff/Admin: `403 Forbidden`.
    *   **TH4:** `start_time` >= `end_time`: `400 Bad Request`.
5. **`DELETE /api/auctions/<auction_id>/`**
    *   **TH1:** Xóa thành công (nếu `status` là `CREATED`).
    *   **TH2:** `auction_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Manager/Admin: `403 Forbidden`.
    *   **TH4:** Phiên đấu giá đã bắt đầu/kết thúc: `400 Bad Request` (hoặc response code khác tùy bạn).
6. **`PATCH /api/auctions/<auction_id>/cancel/`**
    *   **TH1:** Hủy thành công.
    *   **TH2:** `auction_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Manager/Admin: `403 Forbidden`.
    *   **TH4:** Phiên đấu giá đã `CANCELED` hoặc `CLOSED`: `400 Bad Request`.

**E. Admin:**

1. **`GET /api/users/`**
    *   **TH1:** Lấy danh sách user thành công, kiểm tra phân trang, filter, ordering.
    *   **TH2:** User không phải Admin: `403 Forbidden`.
2. **`GET /api/users/<user_id>/`**
    *   **TH1:** `user_id` hợp lệ: Lấy thông tin chi tiết user.
    *   **TH2:** `user_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Admin: `403 Forbidden`.
3. **`PATCH /api/users/<user_id>/`**
    *   **TH1:** Cập nhật thành công (một số field).
    *   **TH2:** `user_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Admin: `403 Forbidden`.
    *   **TH4:** Data không hợp lệ: `400 Bad Request`.
4. **`DELETE /api/users/<user_id>/`**
    *   **TH1:** Xóa thành công.
    *   **TH2:** `user_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Admin: `403 Forbidden`.
5. **`GET /api/core/fee-configuration/`**
    *   **TH1:** Lấy thông tin cấu hình phí thành công.
    *   **TH2:** User không phải Admin: `403 Forbidden`.
6. **`PUT /api/core/fee-configuration/`**
    *   **TH1:** Cập nhật thành công.
    *   **TH2:** User không phải Admin: `403 Forbidden`.
    *   **TH3:** Data không hợp lệ: `400 Bad Request`.
7. **`PUT /api/core/manage_jcoin/<user_id>/`**
    *   **TH1:** Cập nhật thành công.
    *   **TH2:** `user_id` không tồn tại: `404 Not Found`.
    *   **TH3:** User không phải Admin: `403 Forbidden`.
    *   **TH4:** `jcoin_balance` âm: `400 Bad Request`.
8. **`GET /api/db/backup/`**
    *   **TH1:** Backup thành công, trả về file JSON.
    *   **TH2:** User không phải Admin: `403 Forbidden`.
    *   **TH3:** Lỗi server: `500 Internal Server Error`.
9. **`POST /api/db/restore/`**
    *   **TH1:** Restore thành công.
    *   **TH2:** User không phải Admin: `403 Forbidden`.
    *   **TH3:** Không có file upload: `400 Bad Request`.
    *   **TH4:** Lỗi server (ví dụ: sai format file): `500 Internal Server Error`.
