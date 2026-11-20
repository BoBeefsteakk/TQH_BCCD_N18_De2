# Hồ sơ làm việc nhóm (Phụ lục A, B, C của đề; chủ: Phi)

Bản làm việc; cuối kỳ chép sang báo cáo. Bảng ca kiểm thử (Phụ lục D) ở `docs/TESTCASES.md`.

## Phụ lục A — Phiếu đăng ký
| Mục | Thông tin |
|---|---|
| Lớp và tên nhóm | D18CNPM1, Nhóm 18 |
| Đề tài chọn | Đề 2 — Phân loại chế độ phụ tải của khách hàng công nghiệp |
| Dữ liệu và nguồn | UCI Steel Industry Energy Consumption (đề gợi ý), 35.040 bản ghi 15 phút năm 2018, 11 cột, SHA-256 trong `src/config.py` |
| Câu hỏi phân tích 1 | Chế độ phụ tải phụ thuộc thế nào vào khung giờ và ngày trong tuần? (gợi ý của đề) |
| Câu hỏi phân tích 2 | Từ các đại lượng đo, mô hình nhận biết chế độ phụ tải chính xác đến mức nào? (gợi ý của đề) |
| Câu hỏi phân tích 3 | Thuộc tính nào ảnh hưởng nhiều nhất đến điện năng tiêu thụ mỗi 15 phút? (gợi ý của đề) |

Đã đăng ký đề với giảng viên: có (Phi xác nhận trên sheet đăng ký, 18/11/2026). Ngày đăng ký cụ thể: UNKNOWN.

| STT | Họ và tên | Mã sinh viên | Vai trò |
|---|---|---|---|
| 1 | Nguyễn Bảo Phi | 23810310017 | Nhóm trưởng; dữ liệu, tiền xử lý, mô hình, đánh giá |
| 2 | Đỗ Minh Huấn | 23810310075 | Từ điển dữ liệu, trực quan hóa, kiểm thử |
| 3 | Nguyễn Serov Trọng Việt | 23810310019 | Luật kết hợp, phân cụm, giảm chiều, so sánh có/không giảm chiều, Chương 3 và 6 báo cáo, slide |

## Phụ lục B — Kế hoạch, phân công, rủi ro
Ngày thi: **10/01/2027** (Phi báo). Ngày giao đề và hạn nộp thật: **UNKNOWN**. Lịch dưới đây do nhóm tự đặt (19–20/11/2026), tính lùi từ ngày thi, chưa phải hạn chính thức; hạn nộp tệp nén theo đề là "trước buổi báo cáo 2 ngày", nếu buổi đó là 10/01 thì 08/01 (UNKNOWN). Khung thời gian: khoảng 6 tuần làm việc đến 04/01/2027. Ước lượng khối lượng còn lại (giờ, tự đoán): Phi khoảng 24, Huấn khoảng 26, Việt khoảng 32, tức mỗi người 4 đến 5,5 giờ mỗi tuần. Chưa tính lịch học và thi môn khác của từng người (UNKNOWN, báo Phi khi có).

| Mốc (cuối tuần) | Ngày | Cần xong | Sản phẩm |
|---|---|---|---|
| M0 | 20/11/2026 | Khung repo, T001, T002, T007, hồ sơ Phase 1 (đã xong) | Phụ lục A, B bản đầu; bản nháp báo cáo phần Phi |
| M1 | 27/11/2026 | T003 (Huấn), T006 (Việt) | Từ điển dữ liệu; PCA, xếp hạng thuộc tính (mở khóa T010) |
| M2 | 04/12/2026 | T004 (Huấn), T005, T011 (Việt); Phi chốt Chương 1, 4.1 | Báo cáo tiến độ 1 (khối B, C, D: 2.1 đến 4.1) + notebook |
| M3 | 11/12/2026 | T008, T010 (Việt); Phi chốt 4.4 | Phân cụm; so sánh có/không giảm chiều |
| M4 | 18/12/2026 | T009 (Huấn); Phi chốt 5.2, 5.3 | Báo cáo tiến độ 2 (khối E, F, G) + bản nháp toàn báo cáo |
| M5 | 23/12 đến 31/12/2026 | T012 (23/12), T013 (30/12), T014 (31/12); mọi người viết xong phần mình trước 28/12 | Chương 6; dàn ý slide; danh mục, tài liệu tham khảo |
| M6 | 04/01/2027 | Chốt báo cáo (Phi ghép Google Docs, cả nhóm đọc); chạy `run_all.py` từ dữ liệu gốc | Báo cáo PDF, DOCX; bảng tự đánh giá (Phụ lục C) xác nhận |
| M7 | 05/01/2027 | Tệp nén `D18CNPM1_Nhom18_De2.zip` | Hạn nội bộ nộp, sớm 3 ngày so với 08/01 |
| M8 | 06/01 đến 09/01/2027 | Dự phòng, slide, tập trình bày 10 phút và vấn đáp | Mỗi người trả lời được phần mình và phần chung |
| Thi | 10/01/2027 | Vấn đáp (7.3) | |

Phi: Chương 1, 4.1, 4.4, 5.2, 5.3, 7, hồ sơ, ghép báo cáo, đóng gói: chưa tạo thành task, theo các mốc M2 đến M7.

| Rủi ro | Khả năng | Mức ảnh hưởng | Biện pháp | Người theo dõi |
|---|---|---|---|---|
| Rò rỉ làm mô hình đạt điểm cao giả | Đã xảy ra, đã xử lý (T002, g_03, g_04) | Cao | `Load_Type` không suy ra trực tiếp từ `Usage_kWh` (accuracy 0,648); CO2 bị loại (tương quan 0,988); hồi quy giữ công suất phản kháng và hệ số công suất nhưng báo kèm bản bỏ 4 cột đó (R² 0,999 và 0,665) | Phi |
| Phân lớp Medium/Maximum nhầm nhau nhiều (F1 0,56 và 0,45) | Đã xảy ra | Trung bình | Đã thử class_weight và đặc trưng trễ (g_09): không cải thiện; ghi trung thực vào báo cáo 5.3 | Phi |
| Chương 5 (phân cụm) chưa có tài liệu | Cao | Trung bình | Chọn k-means, ghi rõ cách chọn k; hỏi giảng viên | Việt |
| Đề không nói rõ AI viết code có được không | UNKNOWN | Cao | Mỗi người tự chịu trách nhiệm, tự giải thích được phần mình khi vấn đáp | Cả nhóm |
| Ngày giao đề, hạn thật chưa biết | Cao | Cao | Hỏi giảng viên; điền ngày thật vào tài liệu này | Phi |

## Nhật ký tiến độ hằng tuần
| Tuần | Đã làm | Chưa xong | Ghi chú |
|---|---|---|---|
| 18/11/2026 (tuần 1 của nhóm) | T001, T002 (dữ liệu, làm sạch, rò rỉ, chia tập); T007 phần chính (3 mô hình phân lớp, 2 hồi quy, bản bỏ cột vật lý, phân tích lỗi, thử điều chỉnh); `run_all.py`; bản nháp báo cáo phần Phi | So sánh có/không giảm chiều (chuyển cho Việt, T010); hình và từ điển dữ liệu (Huấn); luật kết hợp, giảm chiều, phân cụm (Việt) | Tuần tự đặt, chưa phải tuần chính thức |

## Phụ lục C — Bảng tự đánh giá đóng góp
Tổng tỷ lệ bằng 100%; bảng chỉ có giá trị khi mọi thành viên xác nhận.

| STT | Họ và tên | Phần việc đã làm | Minh chứng | Tỷ lệ (%) | Xác nhận |
|---|---|---|---|---|---|
| 1 | Nguyễn Bảo Phi | | | | |
| 2 | Đỗ Minh Huấn | | | | |
| 3 | Nguyễn Serov Trọng Việt | | | | |
