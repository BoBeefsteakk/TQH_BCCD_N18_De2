"""Cấu hình trung tâm (Đề 2 - phân loại chế độ phụ tải khách hàng công nghiệp, UCI Steel Industry).

Mọi thông số đặt ở đây; không rải số "ma thuật" ở nơi khác (có test chặn).
Đổi một hằng số = đổi quyết định của nhóm -> ghi vào docs/decisions/.
Nhãn NOT VERIFIED = chưa đối chiếu với tệp dữ liệu thật. Dữ liệu và tên cột đã kiểm ở T001 (18/11/2026).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
CLEAN_DIR = DATA_DIR / "clean"
RESULTS_DIR = ROOT / "results"
FIG_DIR = RESULTS_DIR / "figures"
TABLE_DIR = RESULTS_DIR / "tables"

# --- Nhóm, hạt giống ---------------------------------------------------------------------------
GROUP_ID = 18
CLASS_CODE = "D18CNPM1"
TOPIC_NO = 2
# Đề KHÔNG quy định công thức SEED. Nhóm tự chọn mã học phần (quyết định 17/11/2026).
SEED = 4759

# --- Dữ liệu (đề, Đề 2; nguồn UCI Machine Learning Repository) ---------------------------------
# URL, kích thước, SHA-256: ĐÃ KIỂM (T001, 18/11/2026): tải thật từ UCI, 35.040 dòng, 11 cột.
DATA_URL = "https://archive.ics.uci.edu/static/public/851/steel+industry+energy+consumption.zip"
DATA_LOCAL_NAME = "steel.csv"
DATA_SIZE_BYTES: int | None = 2731389
DATA_SHA256: str | None = "9b1cee6f9cb9cd9df2b95814ca90a9a2ff15b7f5f1fba0fae3c643e82072eacc"

EXPECTED_ROWS = 35040  # theo đề: 35.040 bản ghi 15 phút trong năm 2018
EXPECTED_COLS = 11  # theo đề: mười một cột

TIME_COL = "date"
DATE_FORMAT = "%d/%m/%Y %H:%M"  # định dạng chuỗi ngày trong tệp (ĐÃ KIỂM T001)
TARGET_REG = "Usage_kWh"
TARGET_CLS = "Load_Type"
# Tên cột: ĐÃ KIỂM với tệp thật (T001). NSM = số giây từ nửa đêm.
FEATURE_COLS_NUMERIC = [
    "Lagging_Current_Reactive.Power_kVarh",
    "Leading_Current_Reactive_Power_kVarh",
    "Lagging_Current_Power_Factor",
    "Leading_Current_Power_Factor",
    "NSM",
]
FEATURE_COLS_CATEGORICAL = ["WeekStatus", "Day_of_week"]
LOAD_CLASSES = ["Light_Load", "Medium_Load", "Maximum_Load"]  # ĐÃ KIỂM (T001): 51,6% / 27,7% / 20,8%
# Rò rỉ (T001/T002, 18/11/2026): CO2 tương quan 0,988 với Usage_kWh và chỉ là Usage_kWh làm tròn
# nhân hệ số -> loại khỏi đặc trưng (đề yêu cầu kiểm CO2 trước khi dùng). Load_Type KHÔNG suy ra được từ
# Usage_kWh (cây quyết định chỉ trên Usage_kWh: accuracy 0,65), nên không phải rò rỉ theo nghĩa suy ra trực tiếp.
LEAKY_COLS: list[str] = ["CO2(tCO2)"]
# Hồi quy Usage_kWh: Load_Type là nhãn dựng từ mức tiêu thụ nên cũng bị loại khỏi đặc trưng của hồi quy.
# Phân lớp Load_Type: Usage_kWh không dùng làm đầu vào (đo thử: bỏ Usage_kWh không làm giảm F1).
CLS_EXCLUDE_COLS = [TARGET_REG]
REG_EXCLUDE_COLS = [TARGET_CLS]
# Bản đối chứng hồi quy (18/11/2026): bỏ công suất phản kháng và hệ số công suất (Usage_kWh = Q*PF/sqrt(1-PF^2))
REG_NO_PHYSICS_COLS = ["Lagging_Current_Reactive.Power_kVarh", "Leading_Current_Reactive_Power_kVarh",
                       "Lagging_Current_Power_Factor", "Leading_Current_Power_Factor"]
# Giá trị vô lý (khối B): hệ số công suất ngoài khoảng này, NSM ngoài một ngày
PF_RANGE = (0.0, 100.0)
NSM_MAX = 85500  # 23:45 = 85.500 giây từ nửa đêm

# --- Chia dữ liệu, kiểm định -------------------------------------------------------------------
# Đề xuất của Phi, chờ chốt (decisions/): chia theo thời gian, phần cuối làm tập kiểm tra,
# vì mẫu 15 phút liền kề tương quan mạnh, chia ngẫu nhiên gây rò rỉ.
SPLIT_MODE = "time"
TEST_FRACTION = 0.2
CV_FOLDS = 5  # kiểm định chéo phân tầng (đề, khối E)

# --- Tiền xử lý (đề, khối B) -------------------------------------------------------------------
IQR_K = 1.5  # ngoại lai theo quy tắc 1,5 x IQR
PCA_VARIANCE = 0.95  # giữ phương sai tích lũy tối thiểu khi giảm chiều bằng PCA

# --- Phân cụm (đề, khối F) ---------------------------------------------------------------------
KMEANS_K_MIN = 2
KMEANS_K_MAX = 10

# --- Luật kết hợp (đề, khối D): ngưỡng ban đầu, chỉnh khi có dữ liệu ----------------------------
MIN_SUPPORT = 0.05
MIN_CONFIDENCE = 0.6
MIN_LIFT = 1.0

# --- Đầu ra bắt buộc ---------------------------------------------------------------------------
MIN_FIGURES = 8  # đề, khối C: ít nhất 8 biểu đồ thuộc 4 loại trở lên
MIN_FIGURE_TYPES = 4
MIN_RULES_DISCUSSED = 5  # đề, khối D
CLEAN_DATA_NAME = "steel_clean.csv"  # dữ liệu đã làm sạch, lưu ở data/clean/

# --- Quyết định đã chốt (17/11/2026; docs/decisions/, docs/CONVENTIONS.md mục 6) ---------------------
PRIMARY_METRIC_CLS = "f1_macro"  # độ đo chính phân lớp: F1 trung bình macro (không để lớp lớn lấn át); báo thêm từng lớp
PRIMARY_METRIC_REG = "rmse"  # độ đo chính hồi quy: RMSE (kWh); báo thêm MAE, R2
OUTLIER_POLICY = "flag"  # ngoại lai 1,5xIQR: đánh dấu, KHÔNG xóa (phụ tải cao thật chính là chế độ Maximum_Load)
SAMPLING = "none"  # 35.040 dòng là nhỏ, dùng toàn bộ, không lấy mẫu con
HOUR_BIN_EDGES = (0, 6, 12, 18, 24)  # khung giờ cho luật kết hợp: đêm, sáng, chiều, tối
DISCRETIZE_LEVELS = ("thap", "trung_binh", "cao")  # mức tiêu thụ, mức hệ số công suất: 3 mức theo tam phân vị của TRAIN
N_KMEANS_INIT = 10  # số lần khởi tạo k-means
# Lưới siêu tham số (chỉ chọn trên train bằng kiểm định chéo phân tầng, tên tham số theo scikit-learn)
CLASSIFIER_GRID = {
    "decision_tree": {"max_depth": [3, 5, 7, 10, None]},
    "knn": {"n_neighbors": [3, 5, 7, 11]},
    "logistic_regression": {"C": [0.1, 1.0, 10.0]},
}
REGRESSOR_GRID = {
    "decision_tree": {"max_depth": [3, 5, 7, 10, None]},
    "linear_regression": {},
}

# --- Đầu ra bảng (docs/CONVENTIONS.md mục 4: results/tables/<khối>_<số>_<mô_tả>.csv) ---------------
TBL_QUALITY_BEFORE = "b_01_chat_luong_truoc.csv"
TBL_QUALITY_AFTER = "b_02_chat_luong_sau.csv"
TBL_LEAKAGE = "b_03_kiem_ro_ri.csv"
TBL_CLS_CV = "e_01_phan_lop_cv.csv"
TBL_REG_CV = "e_02_hoi_quy_cv.csv"
TBL_CLS_TUNE = "e_03_chinh_tham_so.csv"
TBL_CLS_TEST = "g_01_phan_lop_tung_lop.csv"
TBL_CLS_CONFUSIONS = "g_02_cap_nham_lan.csv"
TBL_REG_TEST = "g_03_hoi_quy_kiem_tra.csv"

LOGREG_MAX_ITER = 1000  # số vòng lặp tối đa của hồi quy logistic (đủ hội tụ trên dữ liệu đã chuẩn hóa)
TBL_REG_NO_PHYSICS = "g_04_hoi_quy_bo_cot_vat_ly.csv"
