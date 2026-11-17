---
id: T002
title: Làm sạch, kiểm rò rỉ, chia theo thời gian, lưu dữ liệu sạch
phase: P2
checklist: 2.2,2.3
owner: phi
status: todo
due: TBD
files: src/data_prep.py
depends: T001
---
# T002 — Làm sạch, kiểm rò rỉ, chia theo thời gian, lưu dữ liệu sạch

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Cài đặt load_raw, quality_report, clean, time_split, save_clean. Kiểm trùng, ngoại lai 1,5xIQR, giá trị vô lý; kiểm CO2 và Load_Type có gần suy ra từ Usage_kWh không; ghi số liệu trước và sau; lưu data/clean/steel_clean.csv.

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
