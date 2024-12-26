**Test API:**

***Sử dụng Postman:**

    ***Method:** `GET`

    ***URL:** `http://127.0.0.1:8000/api/auctions/`

    ***Headers:**

        *`Authorization: Token <your_token>` (thay `<your_token>` bằng token của user).

    ***Test cases:**

        ***TH1: Không có parameters:** Lấy tất cả các phiên đấu giá.

        ***TH2: Lọc theo trạng thái:**

            *`GET /api/auctions/?status=OPEN`: Lấy các phiên đấu giá đang mở.

            *`GET /api/auctions/?status=CLOSED`: Lấy các phiên đấu giá đã đóng.

        ***TH3: Sắp xếp:**

            *`GET /api/auctions/?ordering=start_time`: Sắp xếp theo thời gian bắt đầu tăng dần.

            *`GET /api/auctions/?ordering=-end_time`: Sắp xếp theo thời gian kết thúc giảm dần.

        ***TH4: Lọc các phiên đấu giá user đã tham gia:**

            *`GET /api/auctions/?my_auctions=true`: Lấy các phiên đấu giá user đã tham gia

        ***TH5: Tìm kiếm theo tên trang sức:**

               `GET /api/auctions/?search=nhẫn` (ví dụ tìm cácphiên đấu giá có trang sức tên chứa "nhẫn").

        ***TH6: Kết hợp các filter và sort:** Thử kết hợp các query parameters trên.
***Kiểm tra response:**

    *Status code: `200 OK`

    *Body: Danh sách phiên đấu giá (JSON) đúng với filter và sort.

    *Kiểm tra thông tin trả về có đúng không (bao gồm cả `jewelry` và `bids`).

**Lưu ý:**

*Bạn cần tạo dữ liệu mẫu cho `Auction`, `Jewelry`, và `Bid` để test API này.

*Hãy chú ý đến các trường hợp lỗi (ví dụ: không tìm thấy phiên đấu giá) và đảm bảo API trả về response phù hợp.

*Đảm bảo rằng `start_time` và `end_time` được đặt hợp lý để test các trường hợp đấu giá `OPEN`, `CLOSED`.

Tiếp theo, chúng ta sẽ làm `GET /api/auctions/<auction_id>/`. Bạn đã sẵn sàng chưa?
