# TEST API

**I. API cho `users` app (`/api/users/`)**

1. **`POST /api/users/register/` (Đăng ký)**

    * **Method:** `POST`
    * **Headers:** `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "password": "newpassword123",
            "password_confirm": "newpassword123"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `201 Created`, response body chứa thông tin user mới tạo.
        * **Lỗi:**
            * Trùng username: `400 Bad Request`, response body chứa lỗi `"Username already exists."`.
            * Password không khớp: `400 Bad Request`, response body chứa lỗi `"Passwords do not match."`.
            * Thiếu trường dữ liệu: `400 Bad Request`.

2. **`POST /api/users/login/` (Đăng nhập)**

    * **Method:** `POST`
    * **Headers:** `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "username": "newuser",
            "password": "newpassword123"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin user và token. Ví dụ: `{"user": {"user_id": 6, "username": "newuser", ...}, "token": "YOUR_TOKEN"}`. Lưu lại giá trị `token` này.
        * **Lỗi:** Sai username/password: `401 Unauthorized`, response body chứa lỗi `"Invalid credentials"`.

3. **`POST /api/users/logout/` (Đăng xuất)**

    * **Method:** `POST`
    * **Headers:** `Authorization: Token YOUR_TOKEN`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa message `"Logged out successfully"`.
        * **Lỗi:** Sai token: `401 Unauthorized`.

4. **`GET /api/users/profile/` (Lấy thông tin cá nhân)**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/users/profile/`
    * **Headers:** `Authorization: Token YOUR_TOKEN`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin cá nhân của user.
        * **Lỗi:** Sai token: `401 Unauthorized`.

5. **`GET /api/users/` (Lấy danh sách users - Admin)**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/users/`
    * **Headers:** `Authorization: Token <token_cua_admin>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách tất cả users.
        * **Lỗi:** Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.

6. **`GET /api/users/<user_id>/` (Lấy thông tin chi tiết user - Admin)**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/users/<user_id>/` (ví dụ: `http://127.0.0.1:8000/api/users/2/`)
    * **Headers:** `Authorization: Token <token_cua_admin>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin chi tiết của user có `user_id` tương ứng.
        * **Lỗi:** Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
        * **Lỗi:** Không tìm thấy user: `404 Not Found`.

7. **`PATCH /api/users/<user_id>/` (Cập nhật user - Admin):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/users/<user_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_admin>`
        * `Content-Type: application/json`
    * **Body (raw, JSON):** (ví dụ: cập nhật `first_name` và `last_name`)

        ```json
        {
            "first_name": "New",
            "last_name": "Name"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin user sau khi cập nhật.
        * **Lỗi:** Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
        * **Lỗi:** Không tìm thấy user: `404 Not Found`.

8. **`DELETE /api/users/<user_id>/` (Xóa user - Admin):**

    * **Method:** `DELETE`
    * **URL:** `http://127.0.0.1:8000/api/users/<user_id>/`
    * **Headers:** `Authorization: Token <token_cua_admin>`
    * **Test Cases:**
        * **Thành công:** `204 No Content`.
        * **Lỗi:** Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
        * **Lỗi:** Không tìm thấy user: `404 Not Found`.

9. **`PUT /api/users/<user_id>/manage_jcoin/` (Quản lý JCoin - Admin):**
    * **Method:** `PUT`
    * **URL:** `http://127.0.0.1:8000/api/core/manage-jcoin/<user_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_admin>`
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "amount": 100
        }
        ```

        * **Test Case:**
            * **Thành công:** `200 OK`, response body chứa thông báo `{"message": "JCoin balance updated for user <username>. New balance: <new_balance>"}`
            * **Lỗi:** Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
            * **Lỗi:** Không tìm thấy user: `404 Not Found`.

10. **`GET /api/users/my_notifications/` (Lấy danh sách thông báo):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/users/my_notifications/`
    * **Headers:**
         * `Authorization: Token YOUR_TOKEN`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách các thông báo của user.
        * **Lỗi:** Sai token: `401 Unauthorized`.

**B. `bids` app:**

1. **`POST /api/bids/place/<auction_id>/` (Đặt giá thầu):**

    * **Method:** `POST`
    * **URL:** `http://127.0.0.1:8000/api/bids/place/<auction_id>/` (ví dụ: `http://127.0.0.1:8000/api/bids/place/2/`)
    * **Headers:**
        * `Authorization: Token <token_cua_member>` (sử dụng token của user có role `MEMBER`)
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "amount": "350.00"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `201 Created`, response body chứa thông báo `{"message": "Your bid has been placed successfully.", "bid_amount": "350.00"}`.
        * **Lỗi:**
            * Sai token hoặc user không phải `MEMBER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * `auction_id` không tồn tại: `404 Not Found`.
            * Phiên đấu giá không `OPEN`: `400 Bad Request`.
            * Số tiền đặt giá không đủ: `400 Bad Request`.
            * Giá thầu thấp hơn giá thầu cao nhất hiện tại: `400 Bad Request`.
            * User đặt giá cho trang sức của chính mình: `400 Bad Request`.

2. **`GET /api/bids/my-bids/` (Lấy danh sách các giá thầu của user):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/bids/my-bids/`
    * **Headers:**
        * `Authorization: Token <token_cua_user>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách các giá thầu của user.
        * **Lỗi:** Sai token: `401 Unauthorized`.

**C. `jewelry` app:**

1. **`GET /api/jewelry/` (Lấy danh sách trang sức):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **`GUEST`, `MEMBER`:** `200 OK`, response body chứa danh sách trang sức có status `APPROVED`, `AUCTIONING`, `NO_BIDS`.
        * **`STAFF`, `MANAGER`:** `200 OK`, response body chứa danh sách tất cả trang sức.
        * **Query parameters:**
            * `is_approved=false` (`STAFF`, `MANAGER`): Lấy danh sách trang sức `PENDING`.
            * `search=<từ khóa>`: Tìm kiếm trang sức theo tên.
            * `ordering=initial_price` hoặc `ordering=-initial_price`: Sắp xếp theo giá.

2. **`GET /api/jewelry/<jewelry_id>/` (Lấy thông tin chi tiết trang sức):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/<jewelry_id>/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **`GUEST`, `MEMBER`:** `200 OK`, response body chứa thông tin chi tiết của trang sức nếu status là `APPROVED`, `AUCTIONING`, `NO_BIDS`.
        * **`STAFF`, `MANAGER`:** `200 OK`, response body chứa thông tin chi tiết của tất cả trang sức.
        * **Lỗi:** Không tìm thấy trang sức: `404 Not Found`.

3. **`POST /api/jewelry/create/` (Tạo trang sức):**

    * **Method:** `POST`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/create/`
    * **Headers:**
        * `Authorization: Token <token_cua_member>`
        * `Content-Type`: `application/json` hoặc `multipart/form-data` (nếu upload ảnh)
    * **Body (raw, JSON):**

        ```json
        {
            "name": "Tên trang sức",
            "description": "Mô tả trang sức",
            "initial_price": "100.00",
            "image_1": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
        }
        ```

        hoặc **Body (form-data):**

        | Key         | Value Type | Value                       |
        | ----------- | ---------- | --------------------------- |
        | `name`      | `Text`     | Tên trang sức              |
        | `description` | `Text`     | Mô tả                       |
        | `initial_price` | `Text`     | Giá khởi điểm (ví dụ: 100.00) |
        | `image_1`   | `File`     | Chọn file ảnh              |
        | `image_2`   | `File`     | (Optional) Chọn file ảnh   |
        | `image_3`   | `File`     | (Optional) Chọn file ảnh   |

    * **Test Cases:**
        * **Thành công:** `201 Created`, response body chứa thông tin của trang sức mới tạo.
        * **Lỗi:**
            * User chưa đăng nhập: `401 Unauthorized`.
            * User không phải `MEMBER`: `403 Forbidden`.
            * Thiếu trường dữ liệu: `400 Bad Request`.
            * `initial_price` không hợp lệ: `400 Bad Request`.

4. **`GET /api/jewelry/my-jewelry/` (Lấy danh sách trang sức của user):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/my-jewelry/`
    * **Headers:**
        * `Authorization: Token <token_cua_member>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách trang sức của user.
        * **Lỗi:** User chưa đăng nhập hoặc không phải `MEMBER`: `401 Unauthorized` hoặc `403 Forbidden`.

5. **`PATCH /api/jewelry/<jewelry_id>/approve/` (Duyệt trang sức):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/<jewelry_id>/approve/`
    * **Headers:**
        * `Authorization: Token <token_cua_staff>` (sử dụng token của user có role `STAFF` hoặc `MANAGER`)
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin trang sức sau khi được duyệt (status chuyển thành `APPROVED`).
        * **Lỗi:**
            * Sai token hoặc user không phải `STAFF`, `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy trang sức: `404 Not Found`.

6. **`PATCH /api/jewelry/<jewelry_id>/reject/` (Từ chối trang sức):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/<jewelry_id>/reject/`
    * **Headers:**
        * `Authorization: Token <token_cua_staff>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin trang sức sau khi bị từ chối (status chuyển thành `REJECTED`).
        * **Lỗi:**
            * Sai token hoặc user không phải `STAFF`, `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy trang sức: `404 Not Found`.

7. **`PATCH /api/jewelry/<jewelry_id>/update_jewelry/` (Cập nhật thông tin trang sức):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/<jewelry_id>/update_jewelry/`
    * **Headers:**
        * `Authorization: Token <token_cua_staff_manager>` (sử dụng token của user có role `STAFF` hoặc `MANAGER`)
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "preliminary_price": "123.45",
            "final_price": "456.78",
            "received_at": "2024-01-01T10:00:00Z"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin trang sức sau khi cập nhật.
        * **Lỗi:**
            * Sai token hoặc user không phải `STAFF`, `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy trang sức: `404 Not Found`.
            * Dữ liệu không hợp lệ: `400 Bad Request`.

8. **`PATCH /api/jewelry/<jewelry_id>/confirm_auction/` (Xác nhận đấu giá trang sức):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/jewelry/<jewelry_id>/confirm_auction/`
    * **Headers:**
        * `Authorization: Token <token_cua_owner>` (sử dụng token của user là `owner` của trang sức)
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "seller_approved": true
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin trang sức sau khi cập nhật.
        * **Lỗi:**
            * Sai token hoặc user không phải là `owner`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy trang sức: `404 Not Found`.
            * Trạng thái của trang sức không phải là `APPROVED`: `400 Bad Request`.
            * Dữ liệu không hợp lệ: `400 Bad Request`.

**D. `auctions` app:**

1. **`POST /api/auctions/create/<jewelry_id>/` (Tạo phiên đấu giá):**

    * **Method:** `POST`
    * **URL:** `http://127.0.0.1:8000/api/auctions/create/<jewelry_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_manager>` (sử dụng token của user có role `MANAGER`)
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "start_time": "2025-01-15T10:00:00Z",
            "end_time": "2025-01-15T12:00:00Z",
            "staff": null
        }
        ```

    * **Test Cases:**
        * **Thành công:** `201 Created`, response body chứa thông tin của phiên đấu giá mới tạo, `staff` có thể null.
        * **Lỗi:**
            * Sai token hoặc user không phải `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * `jewelry_id` không tồn tại: `404 Not Found`.
            * Trang sức chưa được duyệt: `400 Bad Request`.
            * Thiếu trường dữ liệu: `400 Bad Request`.
            * `start_time`, `end_time` không hợp lệ: `400 Bad Request`.

2. **`GET /api/auctions/` (Lấy danh sách phiên đấu giá):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/auctions/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **`MANAGER`:** `200 OK`, response body chứa danh sách tất cả phiên đấu giá (có thể filter theo `status`).
        * **`MEMBER`, `STAFF`:** `200 OK`, response body chứa danh sách các phiên đấu giá có status `OPEN` và `CLOSED`.
        * **`GUEST`:** `200 OK`, response body chứa danh sách các phiên đấu giá có status `OPEN`.

3. **`GET /api/auctions/<auction_id>/` (Lấy thông tin chi tiết phiên đấu giá):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/auctions/<auction_id>/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **`MANAGER`:** `200 OK`, response body chứa thông tin chi tiết của phiên đấu giá.
        * **`MEMBER`, `STAFF`:** `200 OK`, response body chứa thông tin chi tiết của phiên đấu giá nếu status là `OPEN` hoặc `CLOSED`.
        * **`GUEST`:** `200 OK`, response body chứa thông tin chi tiết của phiên đấu giá nếu status là `OPEN`.
        * **Lỗi:** Không tìm thấy phiên đấu giá: `404 Not Found`.

4. **`PUT /api/auctions/<auction_id>/` (Cập nhật phiên đấu giá):**

    * **Method:** `PUT`
    * **URL:** `http://127.0.0.1:8000/api/auctions/<auction_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_manager>`
        * `Content-Type: application/json`
    * **Body (raw, JSON):** (ví dụ: cập nhật `end_time`)

        ```json
        {
            "end_time": "2025-01-16T12:00:00Z"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin của phiên đấu giá sau khi cập nhật.
        * **Lỗi:**
            * Sai token hoặc user không phải `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy phiên đấu giá: `404 Not Found`.
            * Dữ liệu không hợp lệ: `400 Bad Request`.

5. **`DELETE /api/auctions/<auction_id>/` (Xóa phiên đấu giá):**

    * **Method:** `DELETE`
    * **URL:** `http://127.0.0.1:8000/api/auctions/<auction_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_manager>`
    * **Test Cases:**
        * **Thành công:** `204 No Content`.
        * **Lỗi:**
            * Sai token hoặc user không phải `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy phiên đấu giá: `404 Not Found`.

6. **`PATCH /api/auctions/<auction_id>/cancel/` (Hủy phiên đấu giá):**

    * **Method:** `PATCH`
    * **URL:** `http://127.0.0.1:8000/api/auctions/<auction_id>/cancel/`
    * **Headers:**
        * `Authorization: Token <token_cua_manager>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin của phiên đấu giá sau khi hủy (status `CANCELED`).
        * **Lỗi:**
            * Sai token hoặc user không phải `MANAGER`: `403 Forbidden` hoặc `401 Unauthorized`.
            * Không tìm thấy phiên đấu giá: `404 Not Found`.
            * Phiên đấu giá không ở trạng thái `CREATED`: `400 Bad Request`.

**E. `core` app:**

1. **`GET /api/core/fee-configuration/` (Lấy thông tin cấu hình phí):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/core/fee-configuration/`
    * **Headers:** (Không bắt buộc)
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin `fee_rate`. Ví dụ: `{"id": 1, "fee_rate": "0.05"}`.

2. **`PUT /api/core/fee-configuration/<pk>/` (Cập nhật thông tin cấu hình phí):**

    * **Method:** `PUT`
    * **URL:** `http://127.0.0.1:8000/api/core/fee-configuration/1/` (Lưu ý: `pk` thường là 1 vì `FeeConfiguration` là `SingletonModel`)
    * **Headers:**
        * `Authorization: Token <token_cua_admin>`
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "fee_rate": "0.10"
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin cấu hình phí sau khi cập nhật.
        * **Lỗi:**
            * Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
            * `fee_rate` không hợp lệ (ví dụ: số âm): `400 Bad Request`.

3. **`PUT /api/core/manage-jcoin/<user_id>/` (Quản lý JCoin của user):**

    * **Method:** `PUT`
    * **URL:** `http://127.0.0.1:8000/api/core/manage-jcoin/<user_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_admin>`
        * `Content-Type: application/json`
    * **Body (raw, JSON):**

        ```json
        {
            "amount": 100
        }
        ```

    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông báo cập nhật JCoin thành công và số dư mới. Ví dụ: `{"message": "JCoin balance updated for user member1. New balance: 1100.00"}`
        * **Lỗi:**
            * Sai token hoặc user không phải `ADMIN`: `403 Forbidden` hoặc `401 Unauthorized`.
            * `user_id` không tồn tại: `404 Not Found`.
            * `amount` không hợp lệ (ví dụ: không phải số): `400 Bad Request`.

**F. `blogs` app:**

1. **`GET /api/blogs/` (Lấy danh sách bài viết):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/blogs/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách tất cả bài viết.
        * **Query parameters:**
            * `search`: Tìm kiếm bài viết theo tiêu đề (ví dụ: `/api/blogs/?search=python`).
            * `ordering`: Sắp xếp theo `publication_date` hoặc `title` (ví dụ: `/api/blogs/?ordering=publication_date` hoặc `/api/blogs/?ordering=-publication_date`).

2. **`GET /api/blogs/<blog_id>/` (Lấy thông tin chi tiết bài viết):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/blogs/<blog_id>/`
    * **Headers:** (không bắt buộc)
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin chi tiết của bài viết có `blog_id` tương ứng.
        * **Lỗi:** Không tìm thấy bài viết: `404 Not Found`.

**G. `users` app:**

* Các API của `users` app đã được liệt kê và hướng dẫn test ở phần **A**.

**H. `transactions` app:**

1. **`GET /api/transactions/` (Lấy danh sách giao dịch):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/transactions/`
    * **Headers:**
        * `Authorization: Token <token_cua_user>`
    * **Test Cases:**
        * **`ADMIN`:** `200 OK`, response body chứa danh sách tất cả giao dịch.
        * **`MEMBER`, `STAFF`, `MANAGER`:** `200 OK`, response body chứa danh sách các giao dịch mà user đó là `winning_bidder` hoặc `jewelry_owner`.
        * **`GUEST`:** `401 Unauthorized`.

2. **`GET /api/transactions/<transaction_id>/` (Lấy thông tin chi tiết giao dịch):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/transactions/<transaction_id>/`
    * **Headers:**
        * `Authorization: Token <token_cua_user>`
    * **Test Cases:**
        * **`ADMIN`:** `200 OK`, response body chứa thông tin chi tiết giao dịch.
        * **`MEMBER`, `STAFF`, `MANAGER`:** `200 OK`, response body chứa thông tin chi tiết giao dịch nếu user đó là `winning_bidder` hoặc `jewelry_owner`.
        * **`GUEST`:** `401 Unauthorized`.
        * **Lỗi:** Không tìm thấy giao dịch: `404 Not Found`.

**I. `notifications` app:**

1. **`GET /api/notifications/` (Lấy danh sách thông báo của user):**

    * **Method:** `GET`
    * **URL:** `http://127.0.0.1:8000/api/notifications/`
    * **Headers:**
        * `Authorization: Token <token_cua_user>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa danh sách thông báo của user hiện tại.
        * **Lỗi:** Sai token: `401 Unauthorized`.

2. **`PUT /api/notifications/<pk>/` (Đánh dấu đã đọc thông báo):**

    * **Method:** `PUT`
    * **URL:** `http://127.0.0.1:8000/api/notifications/<pk>/`
    * **Headers:**
        * `Authorization: Token <token_cua_user>`
    * **Test Cases:**
        * **Thành công:** `200 OK`, response body chứa thông tin thông báo đã được cập nhật `is_read=True`.
        * **Lỗi:** Sai token: `401 Unauthorized`.
        * **Lỗi:** Không tìm thấy thông báo: `404 Not Found`.
        * **Lỗi:** Thông báo không thuộc sở hữu của user: `404 Not Found`.

**Lưu ý:**

* Đối với những API method `PUT`, `PATCH`, `DELETE` thì với mỗi `PUT`, `PATCH` sẽ luôn đi kèm với `GET` tương ứng để lấy data mới nhất và `DELETE` sẽ đi kèm với `GET` để xác nhận rằng đã xóa thành công.
* Với mỗi API trên bạn nhớ thay thế `<token_cua_user>` bằng token của user cần test nhé.
* Và đừng quên là nếu bạn muốn xem cấu trúc của các API trong project, bạn có thể truy cập các đường dẫn sau để xem:
  * `http://127.0.0.1:8000/swagger/`
  * `http://127.0.0.1:8000/redoc/`

Với hướng dẫn chi tiết trên, bạn có thể test tất cả các API của project một cách đầy đủ. Hãy nhớ kiểm tra các trường hợp thành công và thất bại, cũng như phân quyền user cho từng API.
