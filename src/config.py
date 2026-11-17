"""Cấu hình trung tâm (Đề 2 - phân loại chế độ phụ tải khách hàng công nghiệp, UCI Steel Industry).

Mọi thông số đặt ở đây; không rải số "ma thuật" ở nơi khác (có test chặn).
Đổi một hằng số = đổi quyết định của nhóm -> ghi vào docs/decisions/.
Nhãn NOT VERIFIED = lấy từ đề hoặc trí nhớ, chưa đối chiếu với tệp dữ liệu thật (task T001 kiểm).
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
# URL, kích thước, SHA-256: NOT VERIFIED. Điền sau khi tải thật lần đầu (data/download_data.py in ra).
DATA_URL = "https://archive.ics.uci.edu/static/public/851/steel+industry+energy+consumption.zip"
DATA_LOCAL_NAME = "steel.csv"
DATA_SIZE_BYTES: int | None = None
DATA_SHA256: str | None = None

EXPECTED_ROWS = 35040  # theo đề: 35.040 bản ghi 15 phút trong năm 2018
EXPECTED_COLS = 11  # theo đề: mười một cột

TIME_COL = "date"
TARGET_REG = "Usage_kWh"
TARGET_CLS = "Load_Type"
# Tên cột: NOT VERIFIED (trí nhớ về bộ UCI; T001 đối chiếu với tệp thật rồi sửa tại đây).
FEATURE_COLS_NUMERIC = [
    "Lagging_Current_Reactive.Power_kVarh",
    "Leading_Current_Reactive_Power_kVarh",
    "CO2(tCO2)",
    "Lagging_Current_Power_Factor",
    "Leading_Current_Power_Factor",
    "NSM",
]
FEATURE_COLS_CATEGORICAL = ["WeekStatus", "Day_of_week"]
LOAD_CLASSES = ["Light_Load", "Medium_Load", "Maximum_Load"]  # NOT VERIFIED
# CO2 có suy ra trực tiếp từ Usage_kWh không? (đề yêu cầu kiểm trước khi dùng làm đầu vào). UNKNOWN: T001 kiểm.
# Cột bị loại khỏi đặc trưng vì rò rỉ nhãn/đích; để rỗng cho đến khi T001 có bằng chứng.
LEAKY_COLS: list[str] = []

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
