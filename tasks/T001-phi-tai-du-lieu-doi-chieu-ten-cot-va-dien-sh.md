---
id: T001
title: Tải dữ liệu, đối chiếu tên cột và điền SHA-256
phase: P1
checklist: A,1.1
owner: phi
status: done
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
Đã tải bằng `python data/download_data.py` (URL trong config chạy được). 2.731.389 byte, SHA-256 `9b1cee6f…2eacc` (đủ ở `src/config.py`). 35.040 dòng, 11 cột, không thiếu, không trùng. Tên cột trong config khớp tệp thật. Ba lớp Load_Type: Light 51,6% / Medium 27,7% / Maximum 20,8%.
Phát hiện: (1) mốc 00:00 của mỗi ngày nằm CUỐI khối 96 dòng của ngày đó, chuỗi ngày vẫn ghi ngày D; chia tập dựa theo thứ tự dòng; mốc đó thuộc ngày D hay D+1 là UNKNOWN (365 dòng). (2) Bản tải về không có cột nào ngoài 11 cột của đề.
