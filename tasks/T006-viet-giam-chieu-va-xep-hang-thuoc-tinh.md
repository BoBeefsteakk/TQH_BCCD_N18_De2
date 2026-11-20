---
id: T006
title: Giảm chiều và xếp hạng thuộc tính
phase: P2
checklist: 2.3
owner: viet
status: todo
due: 27/11/2026
files: src/reduce.py
depends: T002
---
# T006 — Giảm chiều và xếp hạng thuộc tính

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
PCA khớp trên train (config.PCA_VARIANCE) và rank_features; để Phi so sánh có và không giảm chiều.

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
