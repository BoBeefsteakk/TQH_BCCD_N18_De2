# Nhật ký quyết định (chỉ Phi thêm dòng)

Đổi một hằng số trong `src/config.py` hoặc một quy ước trong `docs/CONVENTIONS.md` thì thêm một dòng ở đây trước khi merge.

| Ngày | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| 17/11/2026 | Nhóm 18 (lớp D18CNPM1) chọn Đề 2, nhóm 3 người | Phi quyết | Làm đủ yêu cầu tối thiểu, không có nội dung mở rộng bắt buộc |
| 17/11/2026 | `SEED = 4759` (mã học phần) | Đề không quy định công thức hạt giống; cần giá trị cố định để chạy lại được | Mọi `random_state` lấy từ `config.SEED` |
| 17/11/2026 | Bỏ tối đa ràng buộc AI: AI viết mã và hỗ trợ báo cáo; không nhật ký AI, không kiểm hiểu bắt buộc | Phi quyết; đề chỉ nói "tra cứu, giải thích, gỡ lỗi" và yêu cầu khai báo ở phụ lục, nên rủi ro do nhóm tự chịu | `TEAM.md` mục 8; mỗi người tự khai phụ lục |
| 17/11/2026 | CHỐT: chia tập theo thời gian (`TEST_FRACTION` = 0,2 cuối năm) | Mẫu 15 phút liền kề tương quan mạnh; chia ngẫu nhiên gây rò rỉ | `config.SPLIT_MODE`, `docs/CONVENTIONS.md` mục 2 |
| 17/11/2026 | Độ đo chính: F1 macro (phân lớp), RMSE (hồi quy) | Tỉ lệ ba lớp chưa biết (UNKNOWN); F1 macro không để lớp lớn lấn át | `PRIMARY_METRIC_CLS`, `PRIMARY_METRIC_REG` |
| 17/11/2026 | Ba mô hình phân lớp: cây quyết định, k-NN, hồi quy logistic; hồi quy: tuyến tính, cây | Đều thuộc Chương 4; đủ tối thiểu của đề | `CLASSIFIER_GRID`, `REGRESSOR_GRID` |
| 17/11/2026 | Ngoại lai chỉ đánh dấu, không xóa; không lấy mẫu con | Phụ tải cao là chế độ Maximum_Load thật; dữ liệu chỉ 35.040 dòng | `OUTLIER_POLICY`, `SAMPLING` |
| 17/11/2026 | Luật kết hợp: 4 khung giờ, 3 mức theo tam phân vị của train | Đủ gọn để Apriori chạy nhanh, diễn giải được | `HOUR_BIN_EDGES`, `DISCRETIZE_LEVELS` |
