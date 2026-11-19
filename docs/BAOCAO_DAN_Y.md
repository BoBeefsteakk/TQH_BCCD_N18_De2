# Dàn ý đầy đủ báo cáo thuyết minh (Đề 2, nhóm 18, 004759)

Đây là **dàn ý**, không phải văn bản báo cáo. Báo cáo viết trên Google Docs (không để trong git). Số liệu chưa có thì ghi `[results/...]`, **không điền số trước khi mã chạy ra**. Cấu trúc theo mục "Cấu trúc báo cáo thuyết minh" và Rubric R3 của đề (`docs/DE2.md`). Chỗ PDF vỡ bảng khi đọc ghi `NOT VERIFIED`; chỗ chưa biết ghi `UNKNOWN`.

> **Cảnh báo cho nhóm (AI):** đề yêu cầu "khai báo công cụ AI đã dùng" trong phụ lục (mục Tài liệu tham khảo và phụ lục). Trưởng nhóm đã bỏ nhật ký AI trong repo, nên **mỗi người tự nhớ và tự khai đúng thực tế** vào phụ lục khai báo. Khai thiếu hoặc sai có thể bị coi là vi phạm liêm chính học thuật; mức xử lý do Trường quyết (`UNKNOWN`).

## Quy tắc chung
- Trình bày: A4, Times New Roman 13, giãn dòng 1,3; **20–30 trang không kể phụ lục**; hình và bảng đánh số, có chú thích và được nhắc trong bài.
- Mỗi hình có tiêu đề, nhãn trục, đơn vị và **một nhận xét rút ra**. Tệp hình: `results/figures/<khối>_<số>_<mô_tả>.png`, truy vết ở `docs/trace_<tên>.md`.
- Mọi số liệu và hình phải do mã đã nộp sinh ra (đề). Dấu phẩy thập phân trong văn bản.
- Ghi nguồn dữ liệu, tài liệu, mã tham khảo; sao chép không trích dẫn thì không được tính điểm.
- Điểm 7.1 xét: báo cáo đầy đủ, cấu trúc logic, có trích dẫn nguồn.

## Kiểm cộng điểm (khớp 10,0)
| Tiêu chí | Mục | Điểm | Chấm |
|---|---|---|---|
| 1. Cơ sở lý thuyết, quy trình | 1.1 | 0,5 | Nhóm |
| 2. Dữ liệu, tiền xử lý | 2.1 (0,25) + 2.2 (0,5) + 2.3 (0,25) | 1,0 | Nhóm |
| 3. Trực quan hóa | 3.1 + 3.2 + 3.3 + 3.4 (mỗi mục 0,5) | 2,0 | Nhóm |
| 4. Cài đặt mô hình | 4.1 + 4.2 + 4.3 + 4.4 (mỗi mục 0,5) | 2,0 | Nhóm |
| 5. Phân tích, đánh giá | 5.1 + 5.2 + 5.3 (mỗi mục 0,5) | 1,5 | Nhóm |
| 6. Quản lý dự án | 6.1 (0,75) nhóm + 6.2 (0,75) cá nhân | 1,5 | Nhóm + cá nhân |
| 7. Báo cáo, trình bày, vấn đáp | 7.1 (0,5) + 7.2 (0,25) nhóm + 7.3 (0,75) cá nhân | 1,5 | Nhóm + cá nhân |
| **Tổng** | | **10,0** | Nhóm 8,5; cá nhân 1,5 |

Nhóm: 0,5 + 1,0 + 2,0 + 2,0 + 1,5 + 0,75 + 0,75 = 8,5. Cá nhân: 0,75 + 0,75 = 1,5. (Đã cộng lại khớp với đề.)

## Trang bìa và phần mở đầu (không tính số trang)
Trang bìa: tên trường, khoa, học phần (Phân tích và trực quan hóa dữ liệu, 004759), tên đề (Đề 2), lớp D18CNPM1, nhóm 18, danh sách thành viên (tên, MSSV), giảng viên (`UNKNOWN`: tên giảng viên chưa biết; đề ghi tác giả đề là Đặng Hoàng Anh nhưng chưa rõ người dạy), năm học. Rồi: mục lục, danh mục hình, danh mục bảng, danh mục từ viết tắt.

## Ngân sách trang (phần thân 20–30 trang; mục tiêu khoảng 26)
| Chương | Trang | Mã chấm liên quan | Người viết chính |
|---|---|---|---|
| 1. Mở đầu | 3 | 1.1 | Phi |
| 2. Yêu cầu và dữ liệu | 4 | 1.1, 2.1 | Huấn |
| 3. Thiết kế sơ bộ | 3 | 1.1 | Việt (khung của Phi, Phi chốt) |
| 4. Cài đặt | 9 | 2.2, 2.3, 3.1–3.4, 4.1–4.4 | Phi, Huấn, Việt |
| 5. Kiểm thử và đánh giá | 4 | 5.1, 5.2, 5.3 | Phi, Huấn |
| 6. Kết luận | 1 | 5.3 | Việt |
| 7. Quản lý công việc nhóm | 2 | 6.1, 6.2 | Phi |
| **Tổng** | **26** | | |

Cấu trúc 7 chương theo đề. Cột "Khối liên quan" của bảng cấu trúc trong PDF bị vỡ khi đọc (chương 6 và 7 lẫn dòng): `NOT VERIFIED`, ánh xạ khối ở trên là cách đọc của nhóm.

---

## Chương 1. Mở đầu (3 trang; mã 1.1, 0,5 điểm)
**Người viết: Phi.** Điều kiện được điểm (mức xuất sắc): liên hệ chính xác quy trình phân tích, lựa chọn mô hình với đề tài và giải thích rõ vì sao chọn cách tiếp cận.
- 1.1 Bối cảnh: lưới điện, khách hàng công nghiệp lớn, nhà máy thép Gwangyang, nhu cầu nhận biết chế độ phụ tải.
- 1.2 Người dùng kết quả: công ty điện lực (điều độ, tư vấn dịch chuyển phụ tải) và nhà máy (theo dõi điện năng, hệ số công suất).
- 1.3 Mục tiêu và câu hỏi phân tích (≥ 3): (1) chế độ phụ tải phụ thuộc thế nào vào khung giờ và ngày trong tuần; (2) mô hình nhận biết chế độ phụ tải chính xác đến mức nào; (3) thuộc tính nào ảnh hưởng nhiều nhất đến điện năng mỗi 15 phút. Nhóm có thể đổi hoặc thêm; đã đăng ký chưa là `UNKNOWN`.
- 1.4 Phạm vi và giới hạn (một nhà máy, một năm).
- 1.5 Cấu trúc báo cáo.
- Hình/bảng: không bắt buộc; có thể một sơ đồ tổng thể quy trình (dùng lại ở Chương 3).

## Chương 2. Yêu cầu và dữ liệu (4 trang; mã 2.1, 0,25 điểm)
**Người viết: Huấn.** Điều kiện được điểm: nguồn dữ liệu, từ điển dữ liệu, thống kê mô tả, phân loại thuộc tính đủ và kiểm tra được.
- 2.1 Yêu cầu phân tích (chuyển từ câu hỏi ở 1.3 sang việc cần làm).
- 2.2 Nguồn dữ liệu: UCI Steel Industry Energy Consumption; quyền sử dụng; 35.040 bản ghi, 11 cột (theo đề; xác nhận bằng tệp thật ở T001).
- 2.3 Từ điển dữ liệu: bảng mọi cột (ý nghĩa, kiểu, đơn vị, khoảng giá trị, vai trò). Nguồn: `docs/DATA_DICTIONARY.md`.
- 2.4 Thống kê mô tả: bảng trung bình, độ lệch chuẩn, min/max, phân vị; tỉ lệ ba lớp `Load_Type` `[results/tables/b_*]`.
- 2.5 Phân loại thuộc tính (số, phân loại, thời gian; đặc trưng, đích, loại bỏ).
- Hình/bảng: Bảng 2.1 từ điển dữ liệu; Bảng 2.2 thống kê mô tả; Bảng 2.3 phân bố lớp.

## Chương 3. Thiết kế sơ bộ (3 trang; mã 1.1, 0,5 điểm dùng chung với Chương 1)
**Người viết: Việt** (chuyển từ Phi 19/11/2026, task T011; khung ở `docs/BAOCAO_NHAP_PHI.md`; Phi chốt quy trình).
- 3.1 Quy trình phân tích: chọn **CRISP-DM, KDD hoặc SEMMA** và giải thích cách áp dụng vào đề (chưa chọn: `UNKNOWN`, nhóm chọn ở P1).
- 3.2 Kế hoạch tiền xử lý (kiểm chất lượng, làm sạch, mã hóa, chuẩn hóa, giảm chiều).
- 3.3 Danh mục biểu đồ dự kiến (bảng: mã hình, loại, câu hỏi phục vụ).
- 3.4 Thuật toán và độ đo sẽ dùng, kèm lý do: cây quyết định, k-NN, hồi quy logistic; hồi quy tuyến tính và cây; Apriori hoặc FP-growth; k-means; F1 macro, RMSE (xem `docs/CONVENTIONS.md` mục 6).
- 3.5 Chiến lược chia tập (theo thời gian), tránh rò rỉ.
- Hình/bảng: Hình 3.1 sơ đồ quy trình; Bảng 3.1 danh mục biểu đồ; Bảng 3.2 thuật toán và độ đo.

## Chương 4. Cài đặt (9 trang; mã 2.2, 2.3, 3.1–3.4, 4.1–4.4)
Điều kiện chung được điểm cao: mỗi hình đúng loại, đủ tiêu đề, nhãn trục, đơn vị, nhận xét (3.4); cài đặt đủ mô hình, tổ chức dữ liệu huấn luyện tốt, chỉnh được tham số (mức xuất sắc của tiêu chí 4).

### 4.1 Tiền xử lý (1,5 trang; 2.2 = 0,5, 2.3 = 0,25) — Phi (giảm chiều: Việt)
- Làm sạch: trùng, ngoại lai 1,5×IQR (đánh dấu, không xóa), giá trị vô lý, không nhất quán; **bảng số liệu trước và sau**.
- Kiểm CO2 và `Load_Type` có gần suy ra từ `Usage_kWh` không (`UNKNOWN` đến khi T002 chạy); quyết định đưa/loại cột.
- Tách thời điểm thành giờ, tháng; mã hóa phân loại; chuẩn hóa (khớp trên train).
- Giảm chiều: PCA hoặc chọn thuộc tính; lưu `data/clean/steel_clean.csv`.
- Hình/bảng: Bảng 4.1 chất lượng trước/sau; Bảng 4.2 kiểm rò rỉ; Hình 4.1 phương sai tích lũy PCA.

### 4.2 Trực quan hóa khám phá và quan hệ (2,5 trang; 3.1, 3.2, 3.4) — Huấn
Tối thiểu **8 hình, 4 loại** (phân bố, quan hệ, so sánh nhóm/thời gian, kết quả mô hình). Đề xuất:
| Hình | Loại | Nội dung | Mã |
|---|---|---|---|
| 4.2 | Phân bố | `Usage_kWh` theo `Load_Type` (histogram/hộp) | 3.1 |
| 4.3 | So sánh nhóm | Hộp `Usage_kWh` theo thứ trong tuần | 3.1 |
| 4.4 | Thời gian | Heatmap giờ × thứ (tỉ lệ từng `Load_Type`) | 3.1 |
| 4.5 | Thời gian | Đường phụ tải một số ngày điển hình | 3.1 |
| 4.6 | Quan hệ | Tán xạ công suất phản kháng và điện năng | 3.2 |
| 4.7 | Quan hệ | Ma trận tương quan, nhận xét thuộc tính trùng thông tin | 3.2 |
Hình/bảng liên quan luật kết hợp và mô hình xếp ở 4.3, 4.4, 4.5.

### 4.3 Mẫu thường xuyên, luật kết hợp, tương quan (1,5 trang; 4.1, 3.2) — Việt
- Rời rạc hóa (4 khung giờ, 3 mức theo tam phân vị của train); Apriori hoặc FP-growth; luật vế phải `Load_Type`; support, confidence, lift.
- **Diễn giải ≥ 5 luật** (nhận xét nghiệp vụ, không chỉ liệt kê).
- Hình/bảng: Bảng 4.3 luật hàng đầu theo lift; Hình 4.8 tán xạ support–confidence (trực quan luật, 3.2); bảng tương quan.

### 4.4 Phân lớp và dự đoán (2 trang; 4.2, 4.4, 3.3) — Phi (hình: Huấn)
- Ít nhất 3 mô hình phân lớp, hồi quy `Usage_kWh`; chia theo thời gian; kiểm định chéo phân tầng; chỉnh tham số (lưới ở `src/config.py`); so sánh có và không giảm chiều (Việt viết đoạn này, T010).
- Hình/bảng: Bảng 4.4 lưới tham số và kết quả chọn; Hình 4.9 ma trận nhầm lẫn; Hình 4.10 độ quan trọng thuộc tính hoặc hình cây quyết định.

### 4.5 Phân cụm (1,5 trang; 4.3, 3.3) — Việt
- k-means; chọn k bằng khuỷu tay và silhouette; mô tả cụm; đối chiếu với `Load_Type`. (Chương 5 chưa có tài liệu: `UNKNOWN`; giải thích rõ cách chọn tham số.)
- Hình/bảng: Hình 4.11 khuỷu tay và silhouette; Hình 4.12 cụm; Bảng 4.5 đối chiếu cụm với `Load_Type`.

## Chương 5. Kiểm thử và đánh giá (4 trang; mã 5.1, 5.2, 5.3, 1,5 điểm)
**Người viết: Phi (5.2, 5.3), Huấn (5.1).** Điều kiện được điểm: ca kiểm thử phù hợp, ghi nhận kết quả rõ; phân tích lỗi và đề xuất điều chỉnh hợp lý nhằm cải thiện độ chính xác.
- 5.1 Bảng ca kiểm thử (Phụ lục D: mã ca, mục tiêu, dữ liệu, kết quả mong đợi, kết quả thực tế, nhận xét). Nguồn: `docs/TESTCASES.md`.
- 5.2 Độ đo và bảng so sánh mô hình: accuracy, precision, recall, F1 từng lớp, F1 macro; MAE, RMSE, R²; so với đoán theo lớp đa số (mốc cơ sở; `UNKNOWN` tỉ lệ lớp).
- 5.3 Phân tích lỗi: cặp lớp bị nhầm nhiều nhất, nguyên nhân, **đề xuất điều chỉnh và thử lại** (có số trước/sau), trả lời từng câu hỏi phân tích.
- Hình/bảng: Bảng 5.1 so sánh mô hình; Bảng 5.2 chỉ số từng lớp; Bảng 5.3 cặp lớp nhầm nhiều nhất; Bảng 5.4 trước/sau điều chỉnh.

## Chương 6. Kết luận (1 trang; mã 5.3)
**Người viết: Việt** (chuyển từ Phi 19/11/2026, T012; khung ở `docs/BAOCAO_NHAP_PHI.md`). Trả lời từng câu hỏi phân tích bằng số từ `results/`; hạn chế (một nhà máy, một năm, rò rỉ nếu có); hướng phát triển (Random Forest, dự báo giờ kế tiếp, khuyến nghị dịch chuyển phụ tải: gợi ý mở rộng của đề, không bắt buộc với nhóm 3).

## Chương 7. Quản lý công việc nhóm (2 trang; mã 6.1, 6.2)
**Người viết: Phi (cả nhóm xác nhận).** Điều kiện được điểm: kế hoạch rõ, phân công hợp lý, theo dõi tiến độ, quản lý rủi ro, minh chứng đóng góp cá nhân rõ.
- Kế hoạch 4 tuần và phân công (từ `docs/PROJECT_RECORDS.md`); nhật ký tiến độ hằng tuần; bảng rủi ro; tự đánh giá đóng góp (tổng 100%, cả nhóm xác nhận); minh chứng: lịch sử git từng người, task.
- Hai báo cáo tiến độ là minh chứng cho tiêu chí này (theo đề).

## Tài liệu tham khảo
IEEE hoặc APA, nhất quán. Bắt buộc: nguồn dữ liệu (UCI Steel Industry Energy Consumption), giáo trình và bài giảng Chương 1–4 (Russell & Norvig 2022; Han, Kamber, Pei; Lê Văn Phùng và Quách Xuân Trưởng 2017, theo slide: `NOT VERIFIED` tên đầy đủ), tài liệu scikit-learn và mlxtend đã dùng. Không đưa tài liệu chưa đọc.

---

## Phụ lục (không tính số trang thân)
- **A. Phiếu đăng ký nhóm và đề tài** (từ `docs/PROJECT_RECORDS.md`).
- **B. Kế hoạch, phân công, rủi ro.**
- **C. Bảng tự đánh giá đóng góp** (tổng 100%, mọi thành viên xác nhận).
- **D. Bảng ca kiểm thử.**
- **E. Khai báo công cụ AI** (công cụ, mục đích; mỗi người tự khai; xem cảnh báo ở đầu file).
- **F. Hướng dẫn chạy mã** và bảng truy vết hình/bảng → hàm/ô notebook (từ `docs/trace_*.md`).
Đề đặt tên A–D cho bốn mẫu biểu (phiếu đăng ký, kế hoạch và rủi ro, tự đánh giá, ca kiểm thử); mục E, F do nhóm thêm.

## Báo cáo tiến độ (không phải phần của báo cáo thuyết minh)
| Mốc | Hạn | Nội dung 1–2 trang | Kèm theo |
|---|---|---|---|
| 1 | Hết tuần 2 | Khối B, C, D đã làm gì, hình/bảng đã có, vướng mắc, kế hoạch tuần 3 | Notebook |
| 2 | Hết tuần 3 | Khối E, F, G đã làm gì, kết quả sơ bộ, rủi ro, kế hoạch hoàn thiện | Bản nháp báo cáo |
Hai báo cáo tiến độ là minh chứng chấm tiêu chí quản lý dự án (đề). Ngày thật: `UNKNOWN` (ngày giao đề chưa biết). Có bị trừ điểm khi không nộp hay không: đề không nói (`UNKNOWN`).

## Thứ tự viết (theo phase của `docs/CHECKLIST.md`)
1. P1: Chương 1, 3.1 và phiếu đăng ký (Phụ lục A, B).
2. P2: Chương 2, 4.1, 4.2, 4.3 và báo cáo tiến độ 1.
3. P3: 4.4, 4.5, Chương 5 và báo cáo tiến độ 2 kèm bản nháp.
4. P4: Chương 3 (hoàn thiện), 6, 7, phụ lục, soát số liệu với `results/`, định dạng, tài liệu tham khảo, slide.
Quy tắc: viết chương sau khi mã chương đó chạy ra kết quả.

## Danh sách kiểm trước khi nộp
- [ ] 20–30 trang thân; A4, Times New Roman 13, giãn 1,3; xuất PDF và DOCX.
- [ ] ≥ 8 hình, ≥ 4 loại; mỗi hình có tiêu đề, nhãn trục, đơn vị, nhận xét; đánh số và được nhắc trong bài.
- [ ] Mọi số và hình khớp `results/`; chạy lại `python run_all.py` từ dữ liệu gốc ra cùng kết quả.
- [ ] Có số liệu làm sạch trước và sau; dữ liệu sạch và từ điển dữ liệu nộp kèm.
- [ ] ≥ 5 luật được diễn giải; ≥ 3 mô hình phân lớp; chỉnh ≥ 1 tham số; có bảng so sánh.
- [ ] Bảng ca kiểm thử, phân tích lỗi, trả lời đủ câu hỏi phân tích.
- [ ] Phụ lục A–D điền đủ; bảng tự đánh giá có xác nhận cả nhóm; khai báo công cụ AI (mục E).
- [ ] Nguồn dữ liệu, tài liệu, mã tham khảo đã ghi.
- [ ] Slide 10–12 trang; mã có README và danh sách thư viện.
- [ ] Tệp nén `D18CNPM1_Nhom18_De2.zip`; nộp chậm nhất 2 ngày trước buổi báo cáo qua kênh giảng viên thông báo.

## Chưa biết / chưa kiểm chứng (UNKNOWN, NOT VERIFIED)
- Ngày giao đề, ngày thi, hạn thật; kênh nộp bài (`UNKNOWN`).
- Tên giảng viên phụ trách lớp (`UNKNOWN`).
- Nhóm đã đăng ký đề với giảng viên chưa (`UNKNOWN`).
- Chương 5 (phân cụm, chuỗi thời gian, đồ thị) có tài liệu hay được dạy không (`UNKNOWN`).
- Thư viện ngoài danh sách của đề (seaborn, plotly, streamlit) có được dùng không (`UNKNOWN`).
- Giảng viên có chấp nhận AI viết mã và đoạn báo cáo không (`UNKNOWN`; nhóm tự chịu rủi ro).
- Tên cột, tỉ lệ ba lớp, CO2 và `Load_Type` có suy ra từ `Usage_kWh` không (`UNKNOWN` đến khi tải dữ liệu thật).
- Bảng cấu trúc báo cáo, bảng sản phẩm và bảng rubric trong PDF bị vỡ khi trích chữ (`NOT VERIFIED`); điểm đã cộng lại khớp 10,0 nhưng nên đối chiếu PDF gốc.
- Trọng số 70% KTHP và nội dung Rubric R3 lấy từ đề, chưa đối chiếu đề cương chi tiết (`NOT VERIFIED`).
- Cách quy đổi điểm trong mỗi mức Rubric R3 (`UNKNOWN`).
