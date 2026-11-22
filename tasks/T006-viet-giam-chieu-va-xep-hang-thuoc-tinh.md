---
id: T006
title: Giảm chiều và xếp hạng thuộc tính
phase: P2
checklist: 2.3
owner: viet
status: done
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
**Đã làm (21/11/2026)** trong `src/reduce.py`:
- `pca_reduce(x_train, x_test)`: Pipeline chuẩn hóa (StandardScaler) rồi PCA giữ `config.PCA_VARIANCE`, `random_state=config.SEED`; khớp chỉ trên train, áp sang test. Trả mô hình là Pipeline, lấy PCA bằng `model.named_steps["pca"]`. Phải chuẩn hóa vì NSM lên tới 85.500 còn hệ số công suất chỉ 0-100.
- `rank_features(x_train, y_train)`: thông tin tương hỗ (mutual information) giữa từng thuộc tính và đích; đích số dùng bản hồi quy, đích chuỗi dùng bản phân lớp; cột one-hot khai báo rời rạc. Trả bảng `(feature, score)` sắp giảm dần.
- Thêm hàm `pca_summary(model)`: bảng phương sai giải thích từng thành phần và lũy kế (dùng cho biểu đồ scree, báo cáo).
- Test: `tests/test_viet_reduce.py` (4 test, dữ liệu tổng hợp). `python -m pytest`: 52 passed.

**Số liệu trên dữ liệu thật** (chạy tay sau `python run_all.py`, chia theo thời gian, đặc trưng từ `data_prep.make_features`):
- PCA: 15 cột (sau one-hot) còn 9 thành phần, phương sai lũy kế 0,9765; PC1 0,2596, PC2 0,1905, PC3 0,0926. Tập đặc trưng của "cls" và "reg" giống nhau nên kết quả PCA như nhau.
- Xếp hạng với Load_Type: NSM 0,629; hour 0,539; Lagging_Current_Power_Factor 0,408; Lagging_Current_Reactive.Power_kVarh 0,328; Leading_Current_Power_Factor 0,122; Leading_Current_Reactive_Power_kVarh 0,112; các cột ngày trong tuần dưới 0,03.
- Xếp hạng với Usage_kWh: Lagging_Current_Power_Factor 1,338; Lagging_Current_Reactive.Power_kVarh 0,871; NSM 0,463; Leading_Current_Power_Factor 0,461; hour 0,408; Leading_Current_Reactive_Power_kVarh 0,377.

**Còn dở, cần Phi:**
- Chưa sinh bảng vào `results/tables/` vì tên bảng phải nằm trong `src/config.py` và nối vào `run_all.py` (file của Phi). Đề xuất: `b_04_pca_phuong_sai.csv` (từ `pca_summary`), `b_05_xep_hang_thuoc_tinh.csv` (từ `rank_features`, cột thêm `dich`). Các số ở trên vì vậy chưa dùng được cho báo cáo cho tới khi có bảng.
- NSM và hour trùng thông tin (hour = NSM chia 3600), cả hai đều đứng đầu; giữ hay bỏ một cột là quyết định của Phi.

**Cập nhật của Phi (22/11/2026):** đã kiểm lại số của Việt, khớp với bản chạy tại thời điểm đó (PCA 9 thành phần, lũy kế 0,9765). Phi bỏ cột `hour` khỏi đặc trưng vì trùng `NSM` (hour = NSM chia 3600), nên số hiện hành khác chút: 14 cột sau one-hot, PCA vẫn 9 thành phần, lũy kế 0,9754; xếp hạng Load_Type: NSM 0,627, hệ số công suất trễ 0,406, công suất phản kháng trễ 0,328. Dùng bảng `b_04`, `b_05` do `run_all.py` sinh (đã nối), không dùng số tay ở trên.
