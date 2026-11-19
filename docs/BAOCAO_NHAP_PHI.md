# Bản nháp báo cáo — phần của Phi (Chương 1, 3, 4.1, 4.4, 5.2, 5.3, 6)

Bản nháp làm việc, chưa phải bản nộp. Báo cáo thật viết trên Google Docs. Số liệu lấy từ `results/tables/` (tên bảng ghi trong ngoặc vuông); sửa số thì chạy lại `python run_all.py` rồi đối chiếu. Chỗ `[…]` là việc của người khác hoặc chưa có. Nhãn **UNKNOWN** / **NOT VERIFIED** giữ nguyên đến khi có bằng chứng. Phi đọc và sửa lời văn trước khi chép sang Docs.

---

## Chương 1. Mở đầu

### 1.1 Bối cảnh
Khách hàng công nghiệp lớn như nhà máy thép dùng lượng điện lớn và biến động mạnh trong ngày. Với công ty điện lực, việc biết một khoảng 15 phút thuộc chế độ phụ tải nhẹ, trung bình hay cực đại giúp điều độ và đề xuất dịch chuyển phụ tải. Với nhà máy, đó là căn cứ theo dõi điện năng và hệ số công suất. Dữ liệu là bộ UCI Steel Industry Energy Consumption (nhà máy thép ở Hàn Quốc, theo mô tả của đề): 35.040 bản ghi cách nhau 15 phút trong năm 2018, 11 cột.

### 1.2 Người dùng kết quả
(1) Bộ phận điều độ và tư vấn của công ty điện lực. (2) Bộ phận năng lượng của nhà máy.

### 1.3 Mục tiêu và câu hỏi phân tích
Xây quy trình phân tích dữ liệu từ làm sạch đến mô hình, để trả lời ba câu hỏi:
1. Chế độ phụ tải phụ thuộc thế nào vào khung giờ và ngày trong tuần?
2. Từ các đại lượng đo, mô hình nhận biết chế độ phụ tải chính xác đến mức nào?
3. Thuộc tính nào ảnh hưởng nhiều nhất đến điện năng tiêu thụ mỗi 15 phút?

### 1.4 Phạm vi và giới hạn
Một nhà máy, một năm, không có dữ liệu thời tiết hay sản lượng. Kết quả không suy rộng cho nhà máy khác. Nhãn `Load_Type` do nguồn dữ liệu gán; cách gán không được nêu trong dữ liệu mà nhóm có (**UNKNOWN**).

### 1.5 Cấu trúc báo cáo
Bảy chương theo yêu cầu của đề: […]

---

## Chương 3. Thiết kế sơ bộ
> Từ 19/11/2026 Việt viết Chương 3 (T011) dựa trên khung này; Phi chốt phần quy trình ở 3.1.

### 3.1 Quy trình phân tích: CRISP-DM
> Đề xuất của bản nháp, chờ Phi chốt (đề cho chọn CRISP-DM, KDD hoặc SEMMA; chưa có quyết định ghi ở `docs/decisions/`).

Hiểu nghiệp vụ → hiểu dữ liệu → chuẩn bị dữ liệu → mô hình hóa → đánh giá → triển khai. Ánh xạ vào đề: hiểu nghiệp vụ là Chương 1; hiểu dữ liệu là Chương 2 và các hình khám phá (4.2); chuẩn bị dữ liệu là 4.1; mô hình hóa là 4.3 đến 4.5; đánh giá là Chương 5. Triển khai chỉ ở mức đề xuất (Chương 6) vì đề không yêu cầu đưa vào vận hành. Chọn CRISP-DM vì quy trình lặp, phù hợp việc quay lại sửa dữ liệu khi phát hiện rò rỉ (xem 4.1).

### 3.2 Kế hoạch tiền xử lý
Kiểm thiếu, trùng, ngoại lai (1,5×IQR), giá trị vô lý; tách giờ; mã hóa one-hot cho loại ngày; chuẩn hóa chỉ khớp trên tập huấn luyện (nằm trong pipeline của mô hình cần thang đo: k-NN, hồi quy logistic, hồi quy tuyến tính); giảm chiều bằng PCA (Việt).

### 3.3 Danh mục biểu đồ dự kiến
[Bảng 3.1: lấy từ `docs/BAOCAO_DAN_Y.md` mục 4.2, Huấn xác nhận.]

### 3.4 Thuật toán và độ đo, kèm lý do
| Việc | Thuật toán | Lý do |
|---|---|---|
| Phân lớp `Load_Type` | Cây quyết định, k-NN, hồi quy logistic | Ba họ khác nhau, đều thuộc Chương 4; cây diễn giải được |
| Hồi quy `Usage_kWh` | Hồi quy tuyến tính, cây hồi quy | Mốc tuyến tính và mốc phi tuyến |
| Độ đo phân lớp | F1 macro (chính), accuracy, precision, recall từng lớp | Lớp Light chiếm 51,6%, nên accuracy dễ đánh lừa; F1 macro cho mỗi lớp trọng số bằng nhau |
| Độ đo hồi quy | RMSE (chính), MAE, R² | RMSE cùng đơn vị kWh, phạt sai số lớn |
Luật kết hợp và k-means: xem 4.3 và 4.5 (Việt).

### 3.5 Chiến lược chia tập
Chia theo thời gian: 80% đầu (28.032 dòng, đến 19/10/2018) huấn luyện, 20% cuối (7.008 dòng, từ 20/10/2018) kiểm tra. Lý do: hai mốc 15 phút liền kề gần giống nhau, chia ngẫu nhiên sẽ đưa mẫu gần như trùng sang tập kiểm tra và làm điểm cao giả. Kiểm định chéo phân tầng 5 lần chỉ chạy trên tập huấn luyện, không xáo trộn. Mọi phép khớp (chuẩn hóa, chọn tham số) chỉ trên tập huấn luyện. Hạn chế: tập kiểm tra là cuối năm nên mô hình chưa thấy mùa đó; vì vậy không dùng cột tháng.

---

## 4.1 Tiền xử lý
- **Chất lượng** [b_01, b_02]: không thiếu, không trùng, không giá trị vô lý; số dòng trước và sau đều 35.040. Ngoại lai 1,5×IQR gắn cờ ở 27,2% dòng (chủ yếu hệ số công suất sớm pha, 8.327 giá trị, và công suất phản kháng sớm pha, 7.759 giá trị). Không xóa: phụ tải cao là chế độ Maximum_Load thật.
- **Thứ tự thời gian:** mốc 00:00 của mỗi ngày nằm cuối khối 96 dòng của ngày đó nhưng chuỗi ngày ghi ngày D. Nhóm chia tập theo thứ tự dòng. Mốc đó thuộc ngày D hay D+1: **UNKNOWN** (365 dòng, khoảng 1%).
- **Kiểm rò rỉ** [b_03]: CO2 tương quan Pearson 0,988 với `Usage_kWh` nên bị loại khỏi đặc trưng. `Load_Type` không suy ra trực tiếp từ `Usage_kWh`: cây chỉ dùng `Usage_kWh` đạt accuracy 0,648 trên tập kiểm tra.
- **Phát hiện thêm (quan trọng):** `Usage_kWh` trùng công thức P = Q·PF/√(1−PF²) với Q là công suất phản kháng trễ và PF là hệ số công suất trễ (0–1): tương quan 0,9999994, sai số tương đối trung vị khoảng 1e-4, trên 27.002 dòng dùng được. Hệ quả ở 4.4.
- **Đặc trưng:** giờ (từ chuỗi ngày), `NSM` (giây từ nửa đêm), 4 cột công suất phản kháng và hệ số công suất, loại ngày và thứ (one-hot). Không dùng tháng. Phân lớp không dùng `Usage_kWh`; hồi quy không dùng `Load_Type` (nhãn dựng từ mức tiêu thụ).
- **Giảm chiều:** […] (Việt, T006).

## 4.4 Phân lớp và dự đoán
- **Cài đặt:** mỗi mô hình chọn tham số bằng GridSearchCV theo lưới trong `src/config.py`, 5 lần phân tầng, chấm bằng F1 macro (RMSE cho hồi quy). Tham số chọn [e_01, e_02, e_03]: cây `max_depth` 10; k-NN 11 láng giềng; hồi quy logistic C = 0,1; cây hồi quy không giới hạn độ sâu.
- **Ma trận nhầm lẫn và độ quan trọng** [g_02, g_07]: hình do Huấn vẽ từ bảng. Cây phân lớp dựa chủ yếu vào `NSM` (0,72) và công suất phản kháng trễ (0,13).
- **So sánh có và không giảm chiều:** […] (đợi T006).

---

## Chương 5. Kiểm thử và đánh giá (phần của Phi)

### 5.2 Độ đo và so sánh mô hình
**Phân lớp** (tập kiểm tra 7.008 dòng) [g_01]. Mốc cơ sở: luôn đoán lớp đa số (Light, 52,9% tập kiểm tra) cho accuracy 0,529.

| Mô hình | Accuracy | F1 macro | F1 Light | F1 Medium | F1 Maximum | F1 macro CV (train) |
|---|---|---|---|---|---|---|
| Cây quyết định | 0,746 | 0,658 | 0,961 | 0,562 | 0,452 | 0,866 |
| k-NN | 0,736 | 0,649 | 0,939 | 0,548 | 0,460 | 0,814 |
| Hồi quy logistic | 0,684 | 0,602 | 0,905 | 0,475 | 0,426 | 0,728 |

**Hồi quy** `Usage_kWh` (kWh) [g_03, g_04]. Mốc cơ sở: đoán bằng trung bình huấn luyện, RMSE 31,49.

| Đầu vào | Mô hình | MAE | RMSE | R² |
|---|---|---|---|---|
| Đủ cột | Cây | 0,44 | 1,00 | 0,999 |
| Đủ cột | Tuyến tính | 6,89 | 9,33 | 0,912 |
| Bỏ 4 cột công suất phản kháng và hệ số công suất | Cây | 10,48 | 18,17 | 0,665 |
| Bỏ 4 cột đó | Tuyến tính | 23,78 | 29,37 | 0,123 |

Diễn giải: R² 0,999 của bản đủ cột là tái tạo công thức vật lý ở 4.1, không phải năng lực dự báo; năng lực dự báo thật là bản bỏ cột (cây R² 0,665, tuyến tính gần như không hơn mốc trung bình). Báo cáo phải nêu cả hai.

### 5.3 Phân tích lỗi và điều chỉnh
**Lớp nào nhầm lớp nào** [g_02]: Medium và Maximum nhầm nhau nhiều nhất. Với cây: 763 mẫu Medium bị đoán Maximum (40,4% lớp Medium) và 734 mẫu Maximum bị đoán Medium (51,8% lớp Maximum). Lớp Light gần như không nhầm sang Maximum.

**Lỗi tập trung ở giờ nào** [g_05, g_06, cây quyết định, mô hình tốt nhất theo CV]: từ 0h đến 11h độ chính xác 99–100%; từ 13h đến 19h chỉ 24–46% (thấp nhất 18h: 23,6%); 20h và 21h hồi lại 73% và 89%; 22h xuống 39,7%. Ngày thường 72,5%, cuối tuần 79,5%. Nghĩa là mô hình chỉ khó phân biệt Medium và Maximum ở buổi chiều và tối, khi tải vận hành cao.

**Nguyên nhân (giả thuyết, chưa chứng minh):** (a) hai lớp này chênh nhau ở mức tải mà đại lượng đo không tách được; (b) tập kiểm tra là cuối năm, khác giai đoạn huấn luyện: F1 macro CV của cây là 0,866 nhưng trên tập kiểm tra chỉ 0,658, tức CV trong cùng giai đoạn lạc quan so với dự báo cho giai đoạn sau; (c) cách gán nhãn `Load_Type` không biết (**UNKNOWN**).

**Điều chỉnh đã thử** [g_09, cây quyết định, cùng tập kiểm tra]:

| Biến thể | F1 macro CV | F1 macro kiểm tra | Accuracy kiểm tra |
|---|---|---|---|
| Gốc | 0,866 | 0,658 | 0,746 |
| Trọng số lớp cân bằng | 0,883 | 0,644 | 0,728 |
| Đặc trưng trễ (trung bình và hiệu trong 1 giờ gần nhất) | 0,862 | 0,656 | 0,748 |
| Cả hai | 0,890 | 0,653 | 0,741 |

Kết luận: không điều chỉnh nào cải thiện trên giai đoạn sau, dù CV tăng ở hai biến thể có trọng số lớp. Báo cáo ghi trung thực kết quả này, không chọn biến thể theo điểm kiểm tra. Hướng chưa thử (**đề xuất**): Random Forest, thêm đặc trưng lịch (ngày lễ), chia kiểm tra theo nhiều đoạn thời gian để đỡ phụ thuộc một mùa.

**Trả lời câu hỏi phân tích**
- Câu 1: […] (cần hình 4.4 của Huấn). Từ cây phân lớp: thời điểm trong ngày (`NSM`) là đặc trưng quan trọng nhất (0,72).
- Câu 2: mô hình tốt nhất (cây) đạt F1 macro 0,658 và accuracy 0,746 trên cuối năm, cao hơn mốc 0,529; nhận biết tốt lớp Light (F1 0,96), kém ở Medium và Maximum.
- Câu 3: khi bỏ công thức vật lý, `NSM` (0,55), giờ (0,22) và loại ngày (0,21) là các thuộc tính chính [g_08]; khi có công suất phản kháng và hệ số công suất thì chúng quyết định gần như hoàn toàn (xem 4.1).

---

## Chương 6. Kết luận (khung)
1. Tóm tắt trả lời ba câu hỏi bằng số ở 5.3.
2. Hạn chế: một nhà máy, một năm; tập kiểm tra cuối năm; nhãn do nguồn gán, cách gán **UNKNOWN**; hồi quy có công thức vật lý; mốc 00:00 mỗi ngày chưa rõ thuộc ngày nào.
3. Hướng phát triển: Random Forest; dự báo giờ kế tiếp; khuyến nghị dịch chuyển phụ tải (gợi ý của đề, không bắt buộc với nhóm 3 người).
