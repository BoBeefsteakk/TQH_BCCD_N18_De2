---
id: T007
title: Phân lớp, hồi quy, kiểm định chéo, chỉnh tham số
phase: P3
checklist: 4.2,4.4
owner: phi
status: doing
due: TBD
files: src/models.py
depends: T002,T006
---
# T007 — Phân lớp, hồi quy, kiểm định chéo, chỉnh tham số

> Phi tạo task. Người làm chỉ đổi `status` và điền mục "Kết quả". Chỉ sửa các file ghi ở `files:` ở trên.

## Mục tiêu
Ít nhất 3 mô hình phân lớp Load_Type, hồi quy Usage_kWh, kiểm định chéo phân tầng, chỉnh tham số, so sánh có và không giảm chiều.

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
Cài `src/models.py` (3 mô hình phân lớp + 2 hồi quy, GridSearchCV theo lưới config, CV 5 lần trên train, không xáo trộn) và `src/evaluate.py`. `python run_all.py` chạy khoảng 13 giây. Bảng: `e_01…e_03`, `g_01…g_03`.
Test (7.008 dòng cuối năm): F1 macro cây quyết định 0,658; k-NN 0,649; hồi quy logistic 0,602. Lớp Light tách tốt (F1 0,96); Medium và Maximum bị nhầm nhau nhiều nhất (cây: 763 và 734 mẫu). CV trên train cao hơn nhiều (cây 0,866), nghĩa là CV trong cùng giai đoạn lạc quan so với dự báo giai đoạn sau. Hồi quy Usage_kWh: cây RMSE 1,00 (R² 0,999), tuyến tính RMSE 9,33 (R² 0,912).
CHƯA XONG: so sánh có/không giảm chiều (đợi T006 của Việt, `reduce.pca_reduce`). Cần xem lại: hồi quy gần như tất định vì Usage_kWh có quan hệ vật lý với công suất phản kháng và hệ số công suất (NOT VERIFIED) – nhóm cần quyết định có giữ hai cột này làm đầu vào hồi quy không.
