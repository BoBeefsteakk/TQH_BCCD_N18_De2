---
id: T003
title: Từ điển dữ liệu và thống kê mô tả
phase: P2
checklist: 2.1
owner: huan
status: todo
due: 27/11/2026
files: docs/DATA_DICTIONARY.md
depends: T001
---
# T003 — Từ điển dữ liệu và thống kê mô tả

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Điền từ điển dữ liệu: mỗi cột một dòng (ý nghĩa, kiểu, đơn vị, khoảng giá trị, vai trò). Thống kê mô tả lấy từ tệp do mã chạy ra.

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
