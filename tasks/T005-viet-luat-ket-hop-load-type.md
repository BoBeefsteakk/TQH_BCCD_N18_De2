---
id: T005
title: Luật kết hợp Load_Type
phase: P2
checklist: 4.1
owner: viet
status: todo
due: 04/12/2026
files: src/assoc.py
depends: T002
---
# T005 — Luật kết hợp Load_Type

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Rời rạc hóa khung giờ, mức tiêu thụ, mức hệ số công suất; Apriori hoặc FP-growth; luật vế phải Load_Type; diễn giải ít nhất 5 luật; bảng tương quan.

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
