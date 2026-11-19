# PHI — Nguyễn Bảo Phi (trưởng nhóm)

Nhánh: `phi-lead-data-models`. Đọc `TEAM.md` trước.

## Phần của bạn
- **Khối A**: bối cảnh, người dùng, ≥ 3 câu hỏi phân tích, chọn quy trình (CRISP-DM/KDD/SEMMA).
- **Khối B**: tải và kiểm dữ liệu, làm sạch, tạo đặc trưng, chia tập theo thời gian, lưu dữ liệu sạch (`src/data_prep.py`); kiểm CO2 và `Load_Type` có gần suy ra từ `Usage_kWh` không.
- **Khối E** (trọng tâm của đề 2): phân lớp ≥ 3 mô hình, hồi quy, kiểm định chéo, chỉnh tham số, so sánh có và không giảm chiều (`src/models.py`).
- **Khối G**: độ đo, bảng so sánh, phân tích lỗi (`src/evaluate.py`).
- **Khối H**: hồ sơ nhóm (`docs/PROJECT_RECORDS.md`), review và merge PR, ghép báo cáo trên Google Docs, `run_all.py`, đóng gói tệp nộp.
- Hạ tầng: `src/config.py`, `docs/`, `tasks/`, `scripts/`, `.github/`.

## Mã chấm chính
1.1 (cùng Việt: Phi viết Chương 1), 2.2, 2.3 (cùng Việt), 4.2 (cùng Việt: Phi làm mô hình, Việt làm so sánh giảm chiều), 4.4, 5.2, 5.3, 6.1, 7.1, 7.2.
