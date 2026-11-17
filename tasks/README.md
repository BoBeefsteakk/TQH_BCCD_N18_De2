# Task của nhóm

1. Task do Phi tạo (`python scripts\tasks.py new ...`); người làm không tự tạo hay đổi nội dung giao việc.
2. Tìm task có `owner` là bạn và `status: todo`, ưu tiên theo hạn (`due`).
3. Chỉ sửa các file ghi ở dòng `files:` của task; thông số lấy từ `src/config.py`.
4. Người làm chỉ đổi `status` (todo → doing → review) và điền mục "Kết quả"; Phi đặt `done` sau khi merge.
5. Commit theo mẫu `T003 feat(b3): ...`.
6. Kiểm tra: `python scripts\tasks.py check`. Bảng dưới do `python scripts\tasks.py readme` sinh, không sửa tay.


## P1

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T001 | phi | todo | TBD | A,1.1 | [Tải dữ liệu, đối chiếu tên cột và điền SHA-256](T001-phi-tai-du-lieu-doi-chieu-ten-cot-va-dien-sh.md) |

## P2

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T002 | phi | todo | TBD | 2.2,2.3 | [Làm sạch, kiểm rò rỉ, chia theo thời gian, lưu dữ liệu sạch](T002-phi-lam-sach-kiem-ro-ri-chia-theo-thoi-gian.md) |
| T003 | huan | todo | TBD | 2.1 | [Từ điển dữ liệu và thống kê mô tả](T003-huan-tu-dien-du-lieu-va-thong-ke-mo-ta.md) |
| T004 | huan | todo | TBD | 3.1,3.2 | [Biểu đồ khám phá (phân bố, heatmap, tán xạ, tương quan)](T004-huan-bieu-do-kham-pha-phan-bo-heatmap-tan-xa.md) |
| T005 | viet | todo | TBD | 4.1 | [Luật kết hợp Load_Type](T005-viet-luat-ket-hop-load-type.md) |
| T006 | viet | todo | TBD | 2.3 | [Giảm chiều và xếp hạng thuộc tính](T006-viet-giam-chieu-va-xep-hang-thuoc-tinh.md) |

## P3

| id | owner | status | due | checklist | tiêu đề |
|---|---|---|---|---|---|
| T007 | phi | todo | TBD | 4.2,4.4 | [Phân lớp, hồi quy, kiểm định chéo, chỉnh tham số](T007-phi-phan-lop-hoi-quy-kiem-dinh-cheo-chinh-th.md) |
| T008 | viet | todo | TBD | 4.3 | [Phân cụm k-means](T008-viet-phan-cum-k-means.md) |
| T009 | huan | todo | TBD | 5.1,3.3 | [Bảng ca kiểm thử và biểu đồ kết quả mô hình](T009-huan-bang-ca-kiem-thu-va-bieu-do-ket-qua-mo-h.md) |
