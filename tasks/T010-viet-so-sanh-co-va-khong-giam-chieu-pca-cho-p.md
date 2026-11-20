---
id: T010
title: So sánh có và không giảm chiều (PCA) cho phân lớp và hồi quy
phase: P3
checklist: 4.2
owner: viet
status: todo
due: 11/12/2026
files: src/reduce.py
depends: T006,T007
---
# T010 — So sánh có và không giảm chiều (PCA) cho phân lớp và hồi quy

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Chuyển từ T007 (Phi chuyển việc cho Việt, 19/11/2026). Sau khi T006 xong: viết `compare_with_reduction(...)` trong `src/reduce.py` huấn luyện lại cùng 3 mô hình phân lớp và 2 mô hình hồi quy trên đặc trưng sau PCA (khớp chỉ trên train, `config.PCA_VARIANCE`), cùng tập chia và cùng độ đo như bản gốc; trả bảng có/không giảm chiều (F1 macro, accuracy; RMSE, MAE, R²). Dùng hàm có sẵn: `data_prep.make_features`, `models.train_classifiers`, `models.train_regressors`, `evaluate.*`. Không sửa các file đó; thiếu gì ghi vào task và báo Phi. Phi nối một dòng vào `run_all.py` để sinh bảng `e_04`.

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
