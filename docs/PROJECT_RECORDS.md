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
| 3 | Nguyễn Serov Trọng Việt | 23810310019 | Luật kết hợp, phân cụm, giảm chiều |

## Phụ lục B — Kế hoạch, phân công, rủi ro
Ngày thi: **10/01/2027** (Phi báo). Ngày giao đề và hạn nộp thật: **UNKNOWN**; các mốc tuần dưới đây là tự phân của nhóm, tính lùi từ ngày thi, chưa phải hạn chính thức.

| Tuần | Công việc | Người phụ trách | Sản phẩm | Trạng thái |
|---|---|---|---|---|
| 1 | Khối A, tải dữ liệu, phiếu đăng ký | Phi | Phụ lục A, B | todo |
| 2 | Khối B, C, D | Phi, Huấn, Việt | Báo cáo tiến độ 1 + notebook | todo |
| 3 | Khối E, F, G | Phi, Việt, Huấn | Báo cáo tiến độ 2 + bản nháp | todo |
| 4 | Hoàn thiện, slide, chạy thử demo | Cả nhóm | Tệp nén cuối | todo |

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
| 18/11/2026 (tuần 1 của nhóm) | T001, T002 (dữ liệu, làm sạch, rò rỉ, chia tập); T007 phần chính (3 mô hình phân lớp, 2 hồi quy, bản bỏ cột vật lý, phân tích lỗi, thử điều chỉnh); `run_all.py`; bản nháp báo cáo phần Phi | So sánh có/không giảm chiều (chờ T006); hình và từ điển dữ liệu (Huấn); luật kết hợp, giảm chiều, phân cụm (Việt) | Tuần tự đặt, chưa phải tuần chính thức |

## Phụ lục C — Bảng tự đánh giá đóng góp
Tổng tỷ lệ bằng 100%; bảng chỉ có giá trị khi mọi thành viên xác nhận.

| STT | Họ và tên | Phần việc đã làm | Minh chứng | Tỷ lệ (%) | Xác nhận |
|---|---|---|---|---|---|
| 1 | Nguyễn Bảo Phi | | | | |
| 2 | Đỗ Minh Huấn | | | | |
| 3 | Nguyễn Serov Trọng Việt | | | | |
