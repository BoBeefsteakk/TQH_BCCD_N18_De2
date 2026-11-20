---
id: T004
title: Biểu đồ khám phá (phân bố, heatmap, tán xạ, tương quan)
phase: P2
checklist: 3.1,3.2
owner: huan
status: todo
due: 04/12/2026
files: src/viz.py,notebooks/huan_eda.ipynb
depends: T002
---
# T004 — Biểu đồ khám phá (phân bố, heatmap, tán xạ, tương quan)

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Cài đặt plot_distribution, plot_heatmap_hour_weekday, plot_scatter, plot_corr_matrix; sinh hình vào results/figures; mỗi hình có tiêu đề, nhãn trục, đơn vị, một nhận xét trong docs/trace_huan.md.

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
