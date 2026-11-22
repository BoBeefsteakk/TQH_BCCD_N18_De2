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
| 18/11/2026 | Ngày thi 10/01/2027; hạn nộp thật và kênh nộp vẫn UNKNOWN | Phi báo ngày thi; hạn nộp tự phân | Task giữ `due: TBD` đến khi có ngày |
| 18/11/2026 | Loại CO2 khỏi đặc trưng (`LEAKY_COLS`); hồi quy bỏ Load_Type; phân lớp không dùng Usage_kWh | CO2 tương quan 0,988 với Usage_kWh; Load_Type dựng từ mức tiêu thụ; bỏ Usage_kWh không giảm F1 phân lớp | `config.LEAKY_COLS`, `CLS_EXCLUDE_COLS`, `REG_EXCLUDE_COLS`, `results/tables/b_03` |
| 18/11/2026 | Không dùng cột tháng làm đặc trưng | Chia theo thời gian: tập kiểm tra có tháng chưa từng thấy ở train | `data_prep.feature_columns` |
| 18/11/2026 | Chia tập theo THỨ TỰ DÒNG, không theo chuỗi ngày | Mốc 00:00 mỗi ngày nằm cuối khối 96 dòng của ngày đó | `data_prep.time_split` |
| 18/11/2026 | `data/clean/*.csv` không vào git, nộp bằng zip | Tệp > 1 MB bị CI chặn | `.gitignore` |
| 18/11/2026 | Hồi quy giữ công suất phản kháng và hệ số công suất làm đầu vào, ghi rõ trong báo cáo | Phi quyết; đã kiểm Usage_kWh = Q·PF/√(1−PF²) (tương quan 0,9999994) | R² 0,999 là tái tạo công thức, nêu ở kết quả và hạn chế; so sánh thêm bản bỏ hai cột nếu còn thời gian |
| 18/11/2026 | Thêm bản hồi quy bỏ 4 cột công suất phản kháng và hệ số công suất (`REG_NO_PHYSICS_COLS`, bảng g_04) | Phi yêu cầu; để có con số dự báo không dựa vào công thức | Báo cáo nêu cả hai bản: cây R² 0,999 (có công thức) và 0,665 (không) |
| 19/11/2026 | Chuyển từ Phi sang Việt: so sánh có/không giảm chiều (T010) và viết Chương 3 báo cáo (T011); 1.1 và 4.2 thành điểm chung Phi và Việt | Phi nặng nhất (khoảng 15 trang, 3,75 điểm riêng), Việt nhẹ nhất (khoảng 3 trang) | Phi còn khoảng 11 trang; Việt khoảng 7; `scripts/tasks.py` OWNED, `TEAM.md`, `CHECKLIST.md`, `BAOCAO_DAN_Y.md` |
| 19/11/2026 | Chuyển thêm: Chương 6 (T012) và dàn ý slide, kịch bản demo (T013) sang Việt; danh mục hình/bảng/viết tắt, tài liệu tham khảo, định dạng báo cáo (T014) sang Huấn | Cân bằng tiếp sau lần chia thứ nhất | Phi còn khoảng 9–10 trang; Việt khoảng 8; Huấn khoảng 8,5 |
| 19/11/2026 | CHỐT phân công: Phi 3 task đã xong + 6 mục báo cáo (Chương 1, 4.1, 4.4, 5.2, 5.3, Chương 7) + điều phối; Huấn T003, T004, T009, T014; Việt T005, T006, T008, T010, T011, T012, T013 + mục 4.3, 4.5 | Phi chốt sau hai lần chia lại; tính cả quá trình Phi 15, Việt 9, Huấn 7 đầu việc (tự đếm, không đo giờ) | Không đổi nếu không có quyết định mới ở đây; T013 vẫn ở Việt; 11 việc còn lại của Phi chưa tạo thành task |
| 20/11/2026 | Đặt hạn nội bộ cho 11 task còn mở và mốc M0 đến M8, tính lùi từ ngày thi 10/01/2027; nộp zip nội bộ 05/01/2027 | Phi giao Claude tự ước lượng thời gian vì chỉ biết ngày thi | `tasks/*.md` (`due`), `docs/PROJECT_RECORDS.md`; sửa khi có hạn thật hoặc khi có phát sinh Phi báo |
| 22/11/2026 | Bỏ cột `hour` khỏi đặc trưng của mọi mô hình; giữ cột `hour` trong dữ liệu sạch; nối bảng b_04 (PCA) và b_05 (xếp hạng thuộc tính) vào `run_all.py`; T006 (Việt) chuyển `done` | `hour` = `NSM` // 3600 chính xác (trùng 100%); đo: F1 macro đổi tối đa 0,002; PCA và khoảng cách k-NN không còn đếm thời gian hai lần. Việt nêu vấn đề này ở T006 | `data_prep.feature_columns`, `run_all.stage_reduce`, `config.TBL_PCA_VARIANCE`, `TBL_FEATURE_RANK`; số trong `docs/BAOCAO_NHAP_PHI.md` và T007 đã cập nhật |
