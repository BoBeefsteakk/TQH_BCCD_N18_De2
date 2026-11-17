# DE2 — yêu cầu gốc của đề (tóm lược, chỉ để tra cứu)

Nguồn: `KTHP_DeBai_BaoCaoChuyenDe_004759.pdf` (không nằm trong git). Nếu file này lệch PDF thì PDF đúng.

## Chung
- Học phần 004759, 3 tín chỉ; KTHP chiếm 70% điểm học phần; chấm Rubric R3 thang 10: 8,5 nhóm + 1,5 cá nhân.
- Nhóm 3–5 người; nhóm 3 làm đủ yêu cầu tối thiểu. 4 tuần kể từ ngày giao đề (ngày giao `UNKNOWN`).
- Công cụ: Python với NumPy, Pandas, Matplotlib; thêm scikit-learn, mlxtend, statsmodels, NetworkX.
- Mã chạy lại được từ dữ liệu gốc đến kết quả; mọi số liệu và hình trong báo cáo sinh từ mã đã nộp.
- AI: "Được dùng để tra cứu, giải thích và gỡ lỗi, nhưng phải khai báo công cụ và mục đích sử dụng trong phụ lục. Mỗi thành viên phải giải thích được mã nguồn và kết quả thuộc phần mình khi vấn đáp."
- Chỉ dùng dữ liệu công khai; nguồn dữ liệu, tài liệu, mã tham khảo phải ghi rõ; sao chép không trích dẫn không được tính điểm.
- Nộp muộn chỉ khi có lý do chính đáng và giảng viên đồng ý trước.

## Khối A–H (mọi đề)
- A: bối cảnh, người dùng, ≥ 3 câu hỏi phân tích; chọn CRISP-DM/KDD/SEMMA.
- B: từ điển dữ liệu, thống kê mô tả; làm sạch có số liệu trước/sau; ≥ 1 phép tích hợp/chuyển hóa; giảm chiều hoặc chọn thuộc tính; lưu dữ liệu sạch ra tệp riêng.
- C: ≥ 8 biểu đồ, ≥ 4 loại (phân bố, quan hệ, so sánh nhóm/thời gian, kết quả mô hình); mỗi hình có tiêu đề, nhãn trục, đơn vị, nhận xét.
- D: Apriori hoặc FP-growth; support, confidence, lift; diễn giải ≥ 5 luật; tương quan.
- E: ≥ 2 mô hình Chương 4 cho cùng bài toán; chia tập hợp lý; chỉnh ≥ 1 tham số; so sánh.
- F: ≥ 1 kỹ thuật phân cụm/chuỗi thời gian/đồ thị, giải thích chọn tham số.
- G: độ đo phù hợp; bảng ca kiểm thử; phân tích lỗi, đề xuất điều chỉnh.
- H: kế hoạch, phân công, nhật ký tuần, bảng rủi ro, tự đánh giá; báo cáo, slide, demo.

## Đề 2 — phân loại chế độ phụ tải khách hàng công nghiệp
Dữ liệu: UCI Steel Industry Energy Consumption, 35.040 bản ghi 15 phút, năm 2018, nhà máy thép Gwangyang; 11 cột; không thiếu giá trị. Khối trọng tâm: **E** (và F phân cụm).

| Khối | Việc phải làm |
|---|---|
| B | Kiểm chất lượng dù không thiếu: trùng, ngoại lai 1,5×IQR, giá trị vô lý; tách thời điểm thành giờ và tháng; mã hóa phân loại; chuẩn hóa; kiểm CO2 có gần suy ra từ Usage_kWh không trước khi dùng làm đầu vào; giảm chiều PCA hoặc chọn thuộc tính |
| C | Phân bố Usage_kWh theo Load_Type; heatmap giờ × thứ; tán xạ công suất phản kháng – điện năng; hình cây quyết định hoặc độ quan trọng thuộc tính; ma trận nhầm lẫn |
| D | Rời rạc hóa khung giờ, mức tiêu thụ, mức hệ số công suất; luật có vế phải là Load_Type; ma trận tương quan, nhận xét thuộc tính trùng thông tin |
| E | Phân lớp Load_Type ≥ 3 mô hình; hồi quy Usage_kWh; kiểm định chéo; chỉnh tham số; so sánh có và không giảm chiều |
| F | k-means trên các khoảng 15 phút hoặc biểu đồ phụ tải ngày; đối chiếu cụm với Load_Type |
| G | Accuracy, precision, recall, F1 từng lớp, ma trận nhầm lẫn; MAE, RMSE, R² cho hồi quy; phân tích các cặp lớp bị nhầm nhiều nhất |

Câu hỏi gợi ý: chế độ phụ tải phụ thuộc thế nào vào khung giờ và ngày trong tuần; mô hình nhận biết chế độ chính xác đến đâu; thuộc tính nào ảnh hưởng nhiều nhất đến điện năng mỗi 15 phút. Mở rộng gợi ý (không bắt buộc với nhóm 3): Random Forest; dự báo giờ kế tiếp; khuyến nghị dịch chuyển phụ tải từ luật và cụm.

## Sản phẩm và mốc
- Một tệp nén `Lớp_Nhóm_Đề`: báo cáo 20–30 trang (PDF + DOCX), mã nguồn (.ipynb hoặc .py, README, danh sách thư viện), dữ liệu sạch và từ điển (CSV/Parquet), slide 10–12 trang, hồ sơ làm việc nhóm. Nộp chậm nhất 2 ngày trước buổi báo cáo.
- Mốc: hết tuần 1 phiếu đăng ký và kế hoạch; hết tuần 2 khối B, C, D + báo cáo tiến độ 1; hết tuần 3 khối E, F, G + báo cáo tiến độ 2 + bản nháp; tuần 4 hoàn thiện; buổi thi: trình bày 10 phút và vấn đáp 5–10 phút.
- Điểm: 1 (0,5) · 2 (1,0) · 3 (2,0) · 4 (2,0) · 5 (1,5) · 6 (1,5: 6.1 nhóm 0,75, 6.2 cá nhân 0,75) · 7 (1,5: 7.1 0,5, 7.2 0,25, 7.3 cá nhân 0,75). Điểm mỗi người = điểm nhóm + điểm cá nhân.
