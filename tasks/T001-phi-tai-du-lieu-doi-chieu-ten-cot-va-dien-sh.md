---
id: T001
title: Tải dữ liệu, đối chiếu tên cột và điền SHA-256
phase: P1
checklist: A,1.1
owner: phi
status: todo
due: TBD
files: src/config.py,data/download_data.py
depends: -
---
# T001 — Tải dữ liệu, đối chiếu tên cột và điền SHA-256

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Tải bộ UCI Steel, xác nhận 35.040 dòng và 11 cột, sửa tên cột trong config, điền DATA_SIZE_BYTES và DATA_SHA256. Việc tải cần Phi đồng ý.

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
