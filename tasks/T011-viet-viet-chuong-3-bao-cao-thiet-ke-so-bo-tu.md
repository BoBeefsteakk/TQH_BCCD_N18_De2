---
id: T011
title: Viết Chương 3 báo cáo (thiết kế sơ bộ) từ bản nháp của Phi
phase: P2
checklist: 1.1
owner: viet
status: todo
due: 04/12/2026
files: docs/BAOCAO_NHAP_VIET.md
depends: T002
---
# T011 — Viết Chương 3 báo cáo (thiết kế sơ bộ) từ bản nháp của Phi

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Chuyển từ Phi (19/11/2026). Viết Chương 3 báo cáo (Thiết kế sơ bộ, khoảng 3 trang) vào `docs/BAOCAO_NHAP_VIET.md`, lấy khung và số liệu từ mục "Chương 3" trong `docs/BAOCAO_NHAP_PHI.md` và `docs/CONVENTIONS.md` mục 6. Gồm: 3.1 quy trình phân tích (CRISP-DM là đề xuất, Phi chốt), 3.2 kế hoạch tiền xử lý, 3.3 danh mục biểu đồ dự kiến (hỏi Huấn), 3.4 thuật toán và độ đo kèm lý do, 3.5 chiến lược chia tập. Tự viết lại bằng lời của mình và phải giải thích được từng mục khi vấn đáp. Số liệu chỉ lấy từ `results/tables/`; chỗ chưa biết giữ nhãn UNKNOWN.

## Đầu vào cần đọc
- `TEAM.md`, `docs/<TÊN>.md`, `docs/CONVENTIONS.md`, `src/config.py`
- (thêm file/mục cụ thể cho task này)

## Không được làm
- Không sửa file ngoài `files:`.
- Không tự đặt thông số ngoài `src/config.py`; thiếu thông số thì ghi vào task và báo Phi.

## Xong khi
- (tiêu chí kiểm được: test nào xanh, hình/bảng nào phải có trong `results/`)
- `python -m pytest` không có test đỏ.

## Kết quả (người làm điền)
(Đã làm gì, lệnh đã chạy, kết quả test/số liệu, chỗ còn dở hoặc không chắc.)
