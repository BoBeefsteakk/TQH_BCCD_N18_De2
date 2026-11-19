# CONVENTIONS — quy ước chung (chỉ Phi sửa)

Mục tiêu: ba người, ba AI vẫn cho ra cùng một định nghĩa, cùng một con số. Thông số số học ở `src/config.py`; file này giữ **định nghĩa và quy ước**. Thấy chỗ mơ hồ → ghi vào task, báo Phi, không tự chọn.

## 1. Dữ liệu và nhãn
- Nguồn: UCI Steel Industry Energy Consumption (35.040 dòng 15 phút, năm 2018, 11 cột; theo đề). Không có giá trị thiếu (đã kiểm T001).
- Đích phân lớp: `Load_Type` (3 lớp). Đích hồi quy: `Usage_kWh`. Tên cột thật lấy từ tệp, sửa trong `src/config.py`.
- Đề yêu cầu kiểm CO2 có gần như suy ra trực tiếp từ `Usage_kWh` trước khi dùng làm đầu vào. Đã kiểm (T002, `results/tables/b_03`): CO2 tương quan 0,988 với `Usage_kWh` nên bị loại (`config.LEAKY_COLS`); `Load_Type` không suy ra trực tiếp từ `Usage_kWh`.
- Dữ liệu sạch lưu `data/clean/steel_clean.csv`; dữ liệu gốc không vào git.

## 2. Chia tập, rò rỉ
- Chia theo **thời gian** (`config.SPLIT_MODE`, `TEST_FRACTION`): phần cuối làm tập kiểm tra. Đã chốt (xem mục 6). Chia theo thứ tự dòng của tệp.
- Mọi phép khớp (chuẩn hóa, PCA, chọn thuộc tính, rời rạc hóa bằng phân vị) khớp **chỉ trên tập huấn luyện**, rồi áp cho tập kiểm tra.
- Kiểm định chéo phân tầng (`config.CV_FOLDS`) chỉ trên tập huấn luyện.
- Ngẫu nhiên: mọi `random_state` và `rng` lấy từ `config.SEED`.

## 3. Chỉ số
- Phân lớp: accuracy, precision, recall, F1 **theo từng lớp** (không chỉ trung bình), ma trận nhầm lẫn; báo các cặp lớp bị nhầm nhiều nhất.
- Hồi quy: MAE, RMSE, R².
- Luật kết hợp: support, confidence, lift (ngưỡng ở config); diễn giải ≥ `config.MIN_RULES_DISCUSSED` luật.
- Phân cụm: khuỷu tay (inertia) và silhouette để chọn k.
- So sánh có và không giảm chiều trên cùng tập chia và cùng độ đo.

## 4. Biểu đồ
- Mỗi hình: tiêu đề, nhãn trục, đơn vị, một nhận xét (ghi trong `docs/trace_<tên>.md`). Tổng ≥ 8 hình thuộc ≥ 4 loại.
- Hình: `results/figures/<khối>_<số>_<mô_tả>.png`; bảng: `results/tables/<khối>_<số>_<mô_tả>.csv`. Khối là chữ thường `b`…`g` theo đề (ví dụ `c_03_heatmap_gio_thu.png`). Số hình/bảng khớp số trong báo cáo.
- Mỗi hình/bảng ghi một dòng vào `docs/trace_<tên>.md`: số hình/bảng | tệp | hàm hoặc ô notebook | mã task | nhận xét.
- Mã quan trọng nằm trong `src/`; notebook chỉ gọi hàm trong `src/`, xóa output trước khi commit, đặt tên `notebooks/<tên>_*.ipynb` (tên: `phi`, `huan`, `viet`).
- Mã tham khảo ngoài (sách, GitHub, Kaggle) ghi nguồn ngay tại chỗ bằng chú thích.

## 5. Văn bản và báo cáo
- Báo cáo viết trên Google Docs (không để trong git), A4, Times New Roman 13, giãn dòng 1,3, 20–30 trang không kể phụ lục. Số liệu chỉ lấy từ tệp trong `results/`. Dấu phẩy thập phân trong văn bản (0,875).
- Tài liệu tham khảo: IEEE hoặc APA, nhất quán; ghi nguồn dữ liệu (UCI).
- Phụ lục A–D theo mẫu của đề, bản làm việc ở `docs/PROJECT_RECORDS.md` (A, B, C) và `docs/TESTCASES.md` (D).

## 6. Quyết định đã chốt (17/11/2026; hằng số ở `src/config.py`, lý do ở `docs/decisions/README.md`)
- **Hạt giống:** `SEED = 4759` cho mọi `random_state` và `rng`.
- **Chia tập:** theo thời gian, 80% đầu năm là huấn luyện, 20% cuối năm là kiểm tra (`SPLIT_MODE`, `TEST_FRACTION`). Kiểm định chéo phân tầng 5 lần chỉ trên tập huấn luyện.
- **Độ đo chính:** phân lớp là F1 macro; hồi quy là RMSE (kWh). Luôn báo thêm chỉ số từng lớp, MAE, R².
- **Mô hình phân lớp (≥ 3, Chương 4):** cây quyết định, k-NN, hồi quy logistic. Hồi quy: tuyến tính và cây hồi quy. Lưới tham số ở `CLASSIFIER_GRID`, `REGRESSOR_GRID`; chọn trên train.
- **Ngoại lai:** đánh dấu theo 1,5×IQR, không xóa.
- **Lấy mẫu:** không (dùng đủ 35.040 dòng).
- **Luật kết hợp:** khung giờ theo `HOUR_BIN_EDGES`; mức tiêu thụ và hệ số công suất chia 3 mức theo tam phân vị của train; ngưỡng ban đầu `MIN_SUPPORT`, `MIN_CONFIDENCE`, `MIN_LIFT`, chỉnh khi có dữ liệu và ghi vào `docs/decisions/`.
- **Phân cụm:** k-means trên đặc trưng số đã chuẩn hóa (khớp trên train), `N_KMEANS_INIT` lần khởi tạo, chọn k bằng khuỷu tay và silhouette.
- Loại **sự thật** chưa chốt: xem danh sách UNKNOWN trong `README.md` và `docs/BAOCAO_DAN_Y.md`.

