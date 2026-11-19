---
id: T014
title: Danh mục hình/bảng/viết tắt, tài liệu tham khảo, định dạng báo cáo
phase: P4
checklist: 7.1
owner: huan
status: todo
due: TBD
files: docs/BAOCAO_DINH_DANG.md
depends: T004
---
# T014 — Danh mục hình/bảng/viết tắt, tài liệu tham khảo, định dạng báo cáo

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Chuyển từ Phi (19/11/2026). Vào `docs/BAOCAO_DINH_DANG.md`: danh mục hình, danh mục bảng (từ `results/` và `docs/trace_*.md`, số khớp báo cáo), danh mục viết tắt, danh sách tài liệu tham khảo IEEE hoặc APA nhất quán (chỉ ghi tài liệu đã đọc; bắt buộc có nguồn UCI), và checklist định dạng Google Docs: A4, Times New Roman 13, giãn dòng 1,3, 20–30 trang không kể phụ lục, xuất PDF và DOCX.

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
