---
id: T009
title: Bảng ca kiểm thử và biểu đồ kết quả mô hình
phase: P3
checklist: 5.1,3.3
owner: huan
status: todo
due: 18/12/2026
files: docs/TESTCASES.md,src/viz.py
depends: T007
---
# T009 — Bảng ca kiểm thử và biểu đồ kết quả mô hình

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Điền Phụ lục D từ kết quả thật; thêm plot_confusion_matrix và biểu đồ độ quan trọng thuộc tính.

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
