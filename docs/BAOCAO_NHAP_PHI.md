# Báo cáo — phần của Phi (bản viết đầy đủ để chép sang Google Docs)

Gồm: Chương 1, mục 4.1, mục 4.4, mục 5.2, mục 5.3, Chương 7. Cuối tệp là khung Chương 3 và Chương 6 để Việt viết (T011, T012). Số liệu lấy từ `results/tables/` (tên bảng trong ngoặc vuông); sửa số thì chạy lại `python run_all.py` rồi đối chiếu. Chỗ `[…]` là việc của người khác hoặc chưa có. Nhãn **UNKNOWN** và **NOT VERIFIED** giữ nguyên đến khi có bằng chứng. Dấu phẩy thập phân trong văn bản.

Đã chốt (22/11/2026): quy trình CRISP-DM. Còn chờ: hình của Huấn (Chương 4.2); so sánh có và không giảm chiều (T010, Việt); số trang đo thật khi chép sang Docs.

---

# CHƯƠNG 1. MỞ ĐẦU

## 1.1 Bối cảnh

Điện năng là đầu vào lớn và biến động mạnh của các khách hàng công nghiệp như nhà máy thép. Một nhà máy thép không dùng điện đều đặn suốt ngày: thường vận hành theo ca sản xuất nên công suất tiêu thụ tại mỗi thời điểm có thể khác nhau rất nhiều. Đối với công ty điện lực, biết một khoảng thời gian thuộc chế độ phụ tải nhẹ, trung bình hay cực đại giúp điều độ nguồn, dự báo nhu cầu và đề xuất khách hàng dịch chuyển phụ tải khỏi giờ cao điểm. Đối với nhà máy, đó là căn cứ để theo dõi điện năng tiêu thụ, hệ số công suất và chi phí.

Báo cáo này phân tích bộ dữ liệu UCI Steel Industry Energy Consumption: 35.040 bản ghi cách nhau 15 phút trong năm 2018 của một nhà máy thép (theo mô tả của đề, nhà máy ở Gwangyang), gồm 11 cột. Mỗi bản ghi có điện năng tiêu thụ (`Usage_kWh`), công suất phản kháng trễ và sớm, hệ số công suất trễ và sớm, lượng phát thải CO2, thời điểm trong ngày (`NSM`, số giây tính từ nửa đêm), loại ngày (ngày thường hay cuối tuần, thứ trong tuần) và nhãn chế độ phụ tải `Load_Type` với ba giá trị: `Light_Load` (nhẹ), `Medium_Load` (trung bình), `Maximum_Load` (cực đại). Bộ dữ liệu không có giá trị thiếu (nhóm đã kiểm lại ở mục 4.1).

## 1.2 Người dùng kết quả

Có hai nhóm người dùng. Thứ nhất là bộ phận điều độ và tư vấn khách hàng của công ty điện lực, cần biết khi nào khách hàng công nghiệp ở chế độ cực đại để điều phối và đề xuất giảm tải. Thứ hai là bộ phận năng lượng của nhà máy, cần nhận biết nhanh chế độ phụ tải từ các đại lượng đo thông thường và hiểu yếu tố nào quyết định điện năng tiêu thụ để cải thiện hệ số công suất và giảm chi phí.

## 1.3 Mục tiêu và câu hỏi phân tích

Mục tiêu là xây dựng một quy trình phân tích dữ liệu hoàn chỉnh, từ kiểm tra và làm sạch dữ liệu, trực quan hóa, khai phá luật kết hợp, phân lớp và hồi quy, phân cụm, đến đánh giá và phân tích lỗi, để trả lời ba câu hỏi:

1. **Câu hỏi 1.** Chế độ phụ tải phụ thuộc thế nào vào khung giờ trong ngày và ngày trong tuần?
2. **Câu hỏi 2.** Từ các đại lượng đo, mô hình nhận biết chế độ phụ tải chính xác đến mức nào, và nhầm lẫn nhiều nhất ở đâu?
3. **Câu hỏi 3.** Thuộc tính nào ảnh hưởng nhiều nhất đến điện năng tiêu thụ trong mỗi 15 phút?

Các câu hỏi được trả lời bằng số liệu ở mục 5.3 và tổng hợp ở Chương 6.

## 1.4 Hướng tiếp cận và quy trình phân tích

Nhóm chọn quy trình CRISP-DM vì đây là quy trình lặp, phù hợp với việc quay lại bước chuẩn bị dữ liệu khi phát hiện vấn đề. Điều này đã xảy ra thật trong đề tài: ở bước hiểu dữ liệu, nhóm phát hiện CO2 gần như là hàm của `Usage_kWh` và `Usage_kWh` trùng một công thức vật lý của công suất phản kháng và hệ số công suất (mục 4.1), nên phải quay lại điều chỉnh tập đặc trưng. Cách ánh xạ từng pha của CRISP-DM vào các chương của báo cáo được trình bày ở Chương 3.

Việc chọn mô hình gắn với bản chất của bài toán. Nhãn `Load_Type` có ba lớp rời rạc nên nhóm dùng ba mô hình phân lớp thuộc ba họ khác nhau: cây quyết định (diễn giải được bằng luật nếu–thì), k láng giềng gần nhất (dựa trên khoảng cách giữa các mẫu) và hồi quy logistic (mô hình tuyến tính làm mốc so sánh). Điện năng `Usage_kWh` là đại lượng liên tục nên nhóm dùng hồi quy tuyến tính (mốc) và cây hồi quy (bắt quan hệ phi tuyến). Vì dữ liệu là chuỗi thời gian với các mẫu liền kề rất giống nhau, nhóm chia tập huấn luyện và kiểm tra theo thời gian thay vì ngẫu nhiên để tránh điểm số cao giả (mục 3.5).

## 1.5 Phạm vi và giới hạn

Dữ liệu chỉ gồm một nhà máy và một năm, không có thông tin thời tiết, sản lượng hay lịch bảo trì, nên kết quả không suy rộng cho nhà máy khác hay năm khác. Nhãn `Load_Type` do nguồn dữ liệu gán; cách gán nhãn không được mô tả trong tài liệu nhóm có, nên nhóm không biết nhãn được tính từ đại lượng nào (**UNKNOWN**). Báo cáo chỉ dùng các thư viện được đề cho phép (NumPy, Pandas, Matplotlib, scikit-learn, mlxtend, statsmodels, NetworkX).

## 1.6 Cấu trúc báo cáo

Báo cáo gồm bảy chương. Chương 1 giới thiệu bối cảnh, mục tiêu và câu hỏi. Chương 2 trình bày yêu cầu, nguồn và từ điển dữ liệu. Chương 3 thiết kế sơ bộ quy trình, thuật toán và độ đo. Chương 4 mô tả cài đặt: tiền xử lý, trực quan hóa, luật kết hợp, phân lớp và hồi quy, phân cụm. Chương 5 trình bày kiểm thử và đánh giá. Chương 6 kết luận. Chương 7 trình bày quản lý công việc nhóm.

---

# 4.1 TIỀN XỬ LÝ

Phần giảm chiều bằng PCA và xếp hạng thuộc tính do Việt trình bày ở mục 4.1.4 (T006).

## 4.1.1 Kiểm tra và làm sạch dữ liệu

Nhóm kiểm tra bốn loại vấn đề: giá trị thiếu, dòng trùng lặp, giá trị vô lý (hệ số công suất ngoài khoảng 0 đến 100, thời điểm `NSM` ngoài một ngày, đại lượng đo âm) và ngoại lai theo quy tắc 1,5 lần khoảng tứ phân vị (IQR). Kết quả ở Bảng 4.1 [b_01, b_02].

**Bảng 4.1. Kết quả kiểm tra chất lượng dữ liệu**

| Chỉ tiêu | Trước làm sạch | Sau làm sạch |
|---|---|---|
| Số dòng | 35.040 | 35.040 |
| Giá trị thiếu | 0 | 0 |
| Dòng trùng lặp | 0 | 0 |
| Dòng có giá trị vô lý | 0 | 0 |
| Ngoại lai 1,5×IQR theo cột: `Usage_kWh` | 328 | (đánh dấu, không xóa) |
| Công suất phản kháng trễ | 1.059 | (đánh dấu, không xóa) |
| Công suất phản kháng sớm | 7.759 | (đánh dấu, không xóa) |
| CO2 | 437 | (đánh dấu, không xóa) |
| Hệ số công suất trễ | 1 | (đánh dấu, không xóa) |
| Hệ số công suất sớm | 8.327 | (đánh dấu, không xóa) |
| Dòng có ít nhất một cột ngoại lai | 27,2% | cờ `is_outlier` |

Dữ liệu sạch sẵn, nên bước làm sạch không loại dòng nào. Ngoại lai chỉ được **đánh dấu** bằng cột `is_outlier`, không xóa, vì các giá trị lớn của điện năng và công suất phản kháng chính là chế độ cực đại có thật của nhà máy; xóa chúng sẽ làm mất đúng lớp cần nhận biết. Phần lớn ngoại lai nằm ở hệ số công suất sớm và công suất phản kháng sớm, vốn có phân phối lệch với đa số giá trị bằng 0 hoặc 100, nên quy tắc IQR đánh dấu nhiều giá trị bình thường.

Về thứ tự thời gian, tệp gốc xếp theo thời gian thật nhưng mốc 00:00 của mỗi ngày nằm ở cuối khối 96 dòng của ngày đó, trong khi chuỗi ngày vẫn ghi ngày của khối. Nhóm chia tập theo thứ tự dòng và không sắp xếp lại theo chuỗi ngày. Việc mốc 00:00 thuộc ngày đó hay ngày kế tiếp là chưa rõ (**UNKNOWN**); ảnh hưởng nhỏ vì chỉ 365 dòng, khoảng 1%.

## 4.1.2 Kiểm tra rò rỉ thông tin

Đề yêu cầu kiểm tra CO2 có gần như suy ra trực tiếp từ `Usage_kWh` hay không trước khi dùng làm đầu vào. Nhóm mở rộng kiểm tra sang hai điều nữa: nhãn `Load_Type` có suy ra được từ `Usage_kWh` không, và `Usage_kWh` có suy ra được từ các đại lượng đo khác không. Kết quả ở Bảng 4.2 [b_03].

**Bảng 4.2. Kiểm tra rò rỉ thông tin**

| Kiểm tra | Kết quả | Quyết định |
|---|---|---|
| Tương quan Pearson giữa `Usage_kWh` và CO2 | 0,988 | Loại CO2 khỏi đặc trưng |
| Độ chính xác của cây quyết định chỉ dùng `Usage_kWh` để đoán `Load_Type` (tập kiểm tra) | 0,648 | `Load_Type` không suy ra trực tiếp từ `Usage_kWh`; không coi là rò rỉ |
| Tương quan giữa `Usage_kWh` và P = Q·PF/√(1−PF²) (Q là công suất phản kháng trễ, PF là hệ số công suất trễ trên thang 0 đến 1) | 0,9999994 (27.002 dòng dùng được) | Giữ hai cột trong hồi quy nhưng báo thêm bản bỏ hai cột (mục 5.2) |

Nhận xét. CO2 chỉ là `Usage_kWh` nhân một hệ số rồi làm tròn, nên nếu dùng làm đầu vào thì mô hình học lại đáp án. Nhóm loại CO2 khỏi mọi tập đặc trưng. Với `Load_Type`, độ chính xác 0,648 chỉ cao hơn một chút mốc đoán lớp đa số (0,529), nên nhãn không suy ra trực tiếp từ điện năng; tuy vậy nhóm vẫn không đưa `Usage_kWh` vào bài toán phân lớp, vì phép thử cho thấy bỏ nó không làm giảm F1. Phát hiện quan trọng nhất là `Usage_kWh` trùng gần như hoàn hảo một công thức công suất trong kỹ thuật điện (công suất tác dụng bằng công suất phản kháng nhân hệ số công suất chia căn của một trừ bình phương hệ số công suất). Hệ quả là mô hình hồi quy có công suất phản kháng và hệ số công suất làm đầu vào đạt R² gần 1 chủ yếu vì tái tạo công thức, không phải vì dự báo được. Nhóm giữ hai cột này trong bản hồi quy đầy đủ, nhưng nêu rõ điều này và báo cáo thêm bản bỏ hai cột để có con số dự báo thật (mục 5.2).

## 4.1.3 Tạo đặc trưng, mã hóa, chuẩn hóa

Từ chuỗi ngày, nhóm tách ra giờ và tháng. Cột giờ không đưa vào mô hình vì bằng đúng `NSM` chia 3600 (nhóm kiểm: trùng 100%), tức trùng thông tin với `NSM` có thang giây mịn hơn; bỏ giờ chỉ làm F1 macro đổi tối đa 0,002. Cột giờ vẫn nằm trong dữ liệu sạch để vẽ biểu đồ và rời rạc hóa khung giờ cho luật kết hợp. Cột tháng cũng không đưa vào mô hình, vì tập kiểm tra là cuối năm (từ 20/10/2018) có những tháng mà tập huấn luyện chưa từng thấy, mô hình chỉ có thể ngoại suy.

Đặc trưng đầu vào gồm 5 cột số (công suất phản kháng trễ và sớm, hệ số công suất trễ và sớm, `NSM`) và hai cột phân loại là loại ngày (ngày thường, cuối tuần) và thứ trong tuần, mã hóa one-hot thành 9 cột, tổng cộng 14 cột. Với các mô hình dựa trên khoảng cách hoặc hệ số (k láng giềng, hồi quy logistic, hồi quy tuyến tính) nhóm chuẩn hóa bằng `StandardScaler`, **khớp chỉ trên tập huấn luyện** bên trong từng bước kiểm định chéo để không rò rỉ thông tin từ tập kiểm tra. Dữ liệu sạch được lưu thành `data/clean/steel_clean.csv` và nộp kèm.

---

# 4.4 PHÂN LỚP VÀ DỰ ĐOÁN

## 4.4.1 Chia tập và kiểm định chéo

Nhóm chia theo thời gian: 28.032 dòng đầu (đến hết ngày 19/10/2018) làm tập huấn luyện, 7.008 dòng cuối (từ 20/10/2018) làm tập kiểm tra. Lý do là hai mốc 15 phút liền kề gần như giống nhau; chia ngẫu nhiên sẽ đưa những mẫu gần trùng sang tập kiểm tra và làm điểm số cao giả. Việc chọn tham số dùng kiểm định chéo 5 lần chỉ trên tập huấn luyện, phân tầng theo lớp với bài toán phân lớp, và không xáo trộn thứ tự để các fold gần với các đoạn thời gian liền nhau. Độ đo chọn tham số là F1 trung bình macro (phân lớp) và RMSE (hồi quy). F1 macro cho ba lớp trọng số bằng nhau, tránh để lớp `Light_Load` (51,6% số mẫu) lấn át lớp `Maximum_Load` (20,8%) vốn là lớp quan trọng nhất với bên điện lực.

## 4.4.2 Mô hình và chỉnh tham số

Mỗi mô hình có một lưới tham số trong `src/config.py` và được chọn bằng tìm kiếm lưới với kiểm định chéo (Bảng 4.4) [e_01, e_02, e_03].

**Bảng 4.4. Lưới tham số và kết quả chọn (chỉ trên tập huấn luyện)**

| Bài toán | Mô hình | Tham số và lưới | Giá trị chọn | Điểm kiểm định chéo |
|---|---|---|---|---|
| Phân lớp | Cây quyết định | độ sâu tối đa: 3, 5, 7, 10, không giới hạn | 10 | F1 macro 0,867 |
| Phân lớp | k láng giềng | số láng giềng: 3, 5, 7, 11 | 11 | F1 macro 0,809 |
| Phân lớp | Hồi quy logistic | hệ số điều chuẩn C: 0,1; 1; 10 | 0,1 | F1 macro 0,728 |
| Hồi quy | Cây hồi quy | độ sâu tối đa: 3, 5, 7, 10, không giới hạn | không giới hạn | RMSE 1,57 kWh |
| Hồi quy | Tuyến tính | không có tham số | không có | RMSE 10,49 kWh |

Nhận xét. Với cây phân lớp, độ sâu 10 tốt hơn cả độ sâu 3 (0,786) và không giới hạn độ sâu (0,819), nghĩa là cây quá nông thì thiếu năng lực, quá sâu thì học thuộc nhiễu. Với k láng giềng, điểm tăng dần theo số láng giềng và đạt cao nhất ở giá trị lớn nhất trong lưới (11); nhóm chưa thử lưới rộng hơn nên chưa biết đó có phải mức tối ưu thật hay không. Hồi quy logistic gần như không phụ thuộc C (0,727 đến 0,728), cho thấy giới hạn của mô hình tuyến tính chứ không phải do điều chuẩn.

## 4.4.3 So sánh có và không giảm chiều

[Việt viết ở T010: huấn luyện lại cùng các mô hình trên đặc trưng sau PCA (14 cột còn 9 thành phần, giữ 97,5% phương sai [b_04]), cùng tập chia và cùng độ đo. Chèn Bảng 4.5 khi có kết quả.]

## 4.4.4 Ma trận nhầm lẫn và độ quan trọng thuộc tính

Hình ma trận nhầm lẫn và hình độ quan trọng thuộc tính do Huấn vẽ từ bảng [g_02, g_07]. Cây phân lớp dựa chủ yếu vào `NSM` (độ quan trọng 0,73) và công suất phản kháng trễ (0,13); các cột loại ngày gần như không đóng góp. Phân tích chi tiết ở mục 5.3.

---

# CHƯƠNG 5. KIỂM THỬ VÀ ĐÁNH GIÁ (phần của Phi: 5.2 và 5.3; 5.1 do Huấn viết)

# 5.2 Độ đo và so sánh mô hình

## 5.2.1 Phân lớp chế độ phụ tải

Tất cả số trong mục này tính trên tập kiểm tra 7.008 dòng cuối năm, không dùng khi chọn tham số [g_01, e_01]. Mốc cơ sở: nếu luôn đoán lớp đa số (`Light_Load`, chiếm 52,9% tập kiểm tra) thì độ chính xác là 0,529.

**Bảng 5.1. So sánh các mô hình phân lớp (tập kiểm tra)**

| Mô hình | Accuracy | F1 macro | F1 Light | F1 Medium | F1 Maximum | F1 macro kiểm định chéo (huấn luyện) |
|---|---|---|---|---|---|---|
| Cây quyết định | 0,746 | 0,657 | 0,963 | 0,559 | 0,450 | 0,867 |
| k láng giềng | 0,732 | 0,647 | 0,935 | 0,546 | 0,459 | 0,809 |
| Hồi quy logistic | 0,684 | 0,602 | 0,904 | 0,474 | 0,427 | 0,728 |

**Bảng 5.2. Precision, recall và F1 theo từng lớp của cây quyết định (mô hình tốt nhất)**

| Lớp | Precision | Recall | F1 | Số mẫu |
|---|---|---|---|---|
| `Light_Load` | 0,981 | 0,945 | 0,963 | 3.704 |
| `Medium_Load` | 0,542 | 0,577 | 0,559 | 1.888 |
| `Maximum_Load` | 0,447 | 0,453 | 0,450 | 1.416 |

Nhận xét. Cả ba mô hình vượt xa mốc cơ sở 0,529, trong đó cây quyết định tốt nhất ở cả accuracy (0,746) lẫn F1 macro (0,657). Lớp `Light_Load` được nhận biết rất tốt (F1 0,96); hai lớp còn lại chỉ đạt F1 khoảng 0,45 đến 0,56. Chênh lệch giữa điểm kiểm định chéo (0,867) và điểm tập kiểm tra (0,657) của cây là đáng kể và được bàn ở mục 5.3.

## 5.2.2 Hồi quy điện năng tiêu thụ

Các chỉ số ở Bảng 5.3 tính trên tập kiểm tra [g_03, g_04]. Mốc cơ sở: luôn đoán bằng trung bình của tập huấn luyện cho RMSE 31,49 kWh.

**Bảng 5.3. Kết quả hồi quy `Usage_kWh` (kWh)**

| Đầu vào | Mô hình | MAE | RMSE | R² |
|---|---|---|---|---|
| Đủ cột | Cây hồi quy | 0,46 | 1,04 | 0,999 |
| Đủ cột | Hồi quy tuyến tính | 6,88 | 9,33 | 0,912 |
| Bỏ 4 cột công suất phản kháng và hệ số công suất | Cây hồi quy | 10,48 | 18,17 | 0,665 |
| Bỏ 4 cột đó | Hồi quy tuyến tính | 23,78 | 29,37 | 0,123 |

Nhận xét. Bản đủ cột cho R² 0,999 nhưng đó chủ yếu là tái tạo công thức vật lý đã nêu ở mục 4.1.2, không phải năng lực dự báo. Năng lực dự báo thật là bản bỏ cột: cây hồi quy giảm RMSE từ 31,49 xuống 18,17 kWh và giải thích 66,5% phương sai, còn hồi quy tuyến tính chỉ đạt R² 0,123, gần như không hơn mốc trung bình. Nghĩa là khi không có công suất phản kháng và hệ số công suất, điện năng phụ thuộc phi tuyến vào thời điểm trong ngày và loại ngày, và mô hình tuyến tính không bắt được.

---

# 5.3 Phân tích lỗi và điều chỉnh

## 5.3.1 Lớp nào bị nhầm với lớp nào

Bảng 5.4 cho các cặp bị nhầm nhiều nhất của cây quyết định [g_02].

**Bảng 5.4. Các cặp lớp bị nhầm nhiều nhất (cây quyết định, tập kiểm tra)**

| Lớp thật | Bị đoán là | Số mẫu | Tỉ lệ trên lớp thật |
|---|---|---|---|
| `Medium_Load` | `Maximum_Load` | 775 | 41,0% |
| `Maximum_Load` | `Medium_Load` | 733 | 51,8% |
| `Light_Load` | `Medium_Load` | 187 | 5,0% |
| `Maximum_Load` | `Light_Load` | 42 | 3,0% |

Hai lớp `Medium_Load` và `Maximum_Load` bị nhầm lẫn lẫn nhau, chiếm gần hết lỗi: hơn một nửa mẫu `Maximum_Load` bị đoán là `Medium_Load`. Lớp `Light_Load` hầu như không bị nhầm sang `Maximum_Load` (17 mẫu).

## 5.3.2 Lỗi tập trung ở giờ nào

Độ chính xác của cây theo giờ trong ngày trên tập kiểm tra [g_05, g_06]:

**Bảng 5.5. Độ chính xác theo giờ (cây quyết định, mỗi giờ 292 mẫu)**

| Giờ | Độ chính xác |
|---|---|
| 0h đến 9h | 100% |
| 10h, 11h | 99,3%; 99,7% |
| 12h | 88,0% |
| 13h, 14h, 15h, 16h | 45,5%; 33,2%; 33,2%; 32,2% |
| 17h, 18h, 19h | 27,1%; 23,6%; 24,7% |
| 20h, 21h | 73,3%; 89,4% |
| 22h, 23h | 40,8%; 81,2% |

Theo loại ngày, độ chính xác ngày thường là 72,5% và cuối tuần là 79,5%. Lỗi tập trung vào buổi chiều và tối, từ 13h đến 19h (chỉ 24% đến 46%) và một đoạn ngắn lúc 22h; từ 0h đến 11h gần như không sai. Nói cách khác, mô hình dễ dàng nhận ra phụ tải nhẹ ban đêm và buổi sáng, nhưng khi nhà máy chạy tải cao vào buổi chiều thì đại lượng đo không đủ để phân biệt mức trung bình với mức cực đại.

## 5.3.3 Nguyên nhân (giả thuyết, chưa chứng minh)

Nhóm đưa ra ba giả thuyết. Thứ nhất, hai lớp `Medium_Load` và `Maximum_Load` chênh nhau ở mức tải mà các đại lượng đo (công suất phản kháng, hệ số công suất, thời điểm) không tách được. Thứ hai, tập kiểm tra là giai đoạn cuối năm, khác giai đoạn huấn luyện: điểm kiểm định chéo của cây là 0,867 nhưng điểm trên tập kiểm tra chỉ 0,657, tức kiểm định chéo trong cùng giai đoạn lạc quan so với dự báo cho giai đoạn sau. Thứ ba, cách gán nhãn `Load_Type` của nguồn dữ liệu không rõ (**UNKNOWN**); nếu nhãn dựa trên một đại lượng mà nhóm không có thì giới hạn độ chính xác này là không tránh được.

## 5.3.4 Điều chỉnh đã thử

Để cải thiện, nhóm thử hai điều chỉnh trên cây quyết định: (a) đặt trọng số lớp cân bằng để lớp nhỏ được chú ý hơn; (b) thêm đặc trưng trễ gồm trung bình trượt 1 giờ gần nhất và hiệu với mốc 15 phút trước của bốn đại lượng công suất, chỉ nhìn về quá khứ nên không rò rỉ. Kết quả ở Bảng 5.6 [g_09], cùng tập kiểm tra.

**Bảng 5.6. Kết quả thử điều chỉnh (cây quyết định)**

| Biến thể | F1 macro kiểm định chéo | F1 macro kiểm tra | Accuracy kiểm tra |
|---|---|---|---|
| Gốc | 0,867 | 0,657 | 0,746 |
| Trọng số lớp cân bằng | 0,883 | 0,644 | 0,728 |
| Đặc trưng trễ | 0,862 | 0,656 | 0,748 |
| Cả hai | 0,889 | 0,653 | 0,741 |

Kết luận: không điều chỉnh nào cải thiện kết quả trên giai đoạn cuối năm (F1 macro kiểm tra từ 0,657 xuống 0,644 đến 0,656), dù điểm kiểm định chéo tăng ở hai biến thể có trọng số lớp. Nhóm ghi nhận kết quả này và không chọn biến thể theo điểm trên tập kiểm tra. Điều đó cũng củng cố giả thuyết thứ nhất và thứ hai: giới hạn nằm ở thông tin của dữ liệu và ở khác biệt giữa các giai đoạn, không phải ở cách cân lớp hay thêm đặc trưng ngắn hạn. Các hướng chưa thử (**đề xuất**): Random Forest, thêm đặc trưng lịch như ngày lễ, và chia tập kiểm tra thành nhiều đoạn thời gian để đỡ phụ thuộc vào một mùa.

## 5.3.5 Trả lời các câu hỏi phân tích

**Câu hỏi 1: chế độ phụ tải phụ thuộc thế nào vào khung giờ và ngày trong tuần?** Phụ thuộc rất mạnh vào cả hai [b_06, b_07]. Theo khung giờ: 0h đến 6h là 100% `Light_Load` (8.760 mẫu); 6h đến 12h là 62,0% nhẹ, 13,8% trung bình, 24,2% cực đại; 12h đến 18h là 17,0% nhẹ, 38,3% trung bình, 44,7% cực đại, nên đây là khung giờ cực đại nhiều nhất; 18h đến 24h là 27,4% nhẹ, 58,5% trung bình và chỉ 14,1% cực đại. Theo thứ trong tuần: Chủ nhật 80,9% nhẹ, thứ bảy 57,4% nhẹ, còn từ thứ hai đến thứ sáu tỉ lệ nhẹ chỉ 43,9% đến 45,0% và cực đại khoảng 23,6% đến 24,0%. Phù hợp với kết quả của cây: `NSM` là đặc trưng quan trọng nhất (0,73). [Chèn Hình 4.4 heatmap giờ × thứ của Huấn.]

**Câu hỏi 2: mô hình nhận biết chế độ phụ tải chính xác đến mức nào?** Mô hình tốt nhất là cây quyết định: accuracy 0,746 và F1 macro 0,657 trên cuối năm, cao hơn mốc đoán lớp đa số (accuracy 0,529). Mô hình nhận biết tốt chế độ nhẹ (F1 0,963) nhưng kém ở chế độ trung bình (0,559) và cực đại (0,450), vì hai lớp này nhầm lẫn lẫn nhau ở buổi chiều và tối (mục 5.3.2).

**Câu hỏi 3: thuộc tính nào ảnh hưởng nhiều nhất đến điện năng tiêu thụ mỗi 15 phút?** Có hai câu trả lời tùy theo đầu vào. Khi có công suất phản kháng và hệ số công suất, hai đại lượng này quyết định gần như hoàn toàn, vì `Usage_kWh` trùng công thức của chúng (mục 4.1.2); đây là quan hệ kỹ thuật điện chứ không phải phát hiện mới. Khi bỏ hai đại lượng này, độ quan trọng thuộc tính của cây hồi quy cho thấy thời điểm trong ngày `NSM` (0,77) rồi loại ngày (0,21) là các thuộc tính chính [g_08]; xếp hạng thông tin tương hỗ cũng đặt hệ số công suất trễ, công suất phản kháng trễ và `NSM` ở ba vị trí đầu [b_05].

---

# CHƯƠNG 7. QUẢN LÝ CÔNG VIỆC NHÓM

## 7.1 Thành viên và phân công

Nhóm 18, lớp D18CNPM1 gồm ba thành viên (Bảng 7.1). Phi là nhóm trưởng.

**Bảng 7.1. Thành viên và phần việc chính**

| STT | Họ và tên | Mã sinh viên | Vai trò |
|---|---|---|---|
| 1 | Nguyễn Bảo Phi | 23810310017 | Nhóm trưởng; dữ liệu, tiền xử lý, mô hình, đánh giá; hồ sơ nhóm, ghép báo cáo, đóng gói |
| 2 | Đỗ Minh Huấn | 23810310075 | Từ điển dữ liệu, trực quan hóa, bảng ca kiểm thử, định dạng báo cáo |
| 3 | Nguyễn Serov Trọng Việt | 23810310019 | Luật kết hợp, phân cụm, giảm chiều, so sánh có và không giảm chiều, Chương 3 và 6, dàn ý slide |

Phân công theo nguyên tắc mỗi tệp mã nguồn có đúng một chủ. Cụ thể Phi phụ trách `data_prep`, `models`, `evaluate`, cấu hình và `run_all.py`; Huấn phụ trách `viz.py`, từ điển dữ liệu và bảng ca kiểm thử; Việt phụ trách `assoc`, `clustering`, `reduce`. Phân công được chia lại hai lần ngày 19/11/2026 để cân tải, ghi trong nhật ký quyết định của nhóm.

## 7.2 Kế hoạch và mốc thời gian

Ngày thi là 10/01/2027. Ngày giao đề và hạn nộp thật chưa rõ (**UNKNOWN**), nên nhóm tự đặt lịch nội bộ tính lùi từ ngày thi, với hạn nộp tệp nén nội bộ là 05/01/2027, sớm hơn hạn "trước buổi báo cáo 2 ngày" của đề (nếu buổi đó là ngày thi thì là 08/01/2027).

**Bảng 7.2. Các mốc của nhóm**

| Mốc | Ngày | Nội dung chính |
|---|---|---|
| M1 | 27/11/2026 | Từ điển dữ liệu; giảm chiều và xếp hạng thuộc tính |
| M2 | 04/12/2026 | Báo cáo tiến độ 1: biểu đồ khám phá, luật kết hợp, Chương 1 và 4.1 |
| M3 | 11/12/2026 | Phân cụm; so sánh có/không giảm chiều; mục 4.4 |
| M4 | 18/12/2026 | Báo cáo tiến độ 2 và bản nháp toàn báo cáo; ca kiểm thử; 5.2, 5.3 |
| M5 | 23/12 đến 31/12/2026 | Chương 6; dàn ý slide; danh mục và tài liệu tham khảo |
| M6 | 04/01/2027 | Chốt báo cáo, chạy lại từ dữ liệu gốc |
| M7 | 05/01/2027 | Nộp tệp nén (hạn nội bộ) |
| M8 | 06/01 đến 09/01/2027 | Dự phòng, tập trình bày và vấn đáp |

## 7.3 Cách tổ chức làm việc và theo dõi tiến độ

Nhóm làm việc trên một kho mã duy nhất. Có đúng bốn nhánh: nhánh chính chỉ nhận thay đổi qua yêu cầu hợp nhất (pull request) và ba nhánh cá nhân; chỉ trưởng nhóm hợp nhất vào nhánh chính. Mỗi thay đổi phải qua kiểm tra tự động (chạy kiểm thử, kiểm tra mẫu thông điệp commit, tệp lớn và dữ liệu thô). Việc được chia thành các task có mã (T001 đến T014), mỗi task có người nhận, hạn và trạng thái; công cụ `scripts/tasks.py` kiểm tra file mà mỗi người được sửa. Mọi quyết định đổi thông số hoặc quy ước đều ghi vào nhật ký quyết định có ngày và lý do. Mọi tham số của phân tích (hạt giống ngẫu nhiên, tỉ lệ chia, lưới tham số, ngưỡng) nằm ở một tệp cấu hình duy nhất, và các kiểm thử tự động chặn số "ma thuật" ngoài tệp đó. Nhờ vậy ba người chạy lại cho cùng một kết quả.

Đến ngày 22/11/2026: 5 yêu cầu hợp nhất đã được merge, 54 kiểm thử đạt, 4 trong 14 task đã xong. [Cập nhật số khi chép sang Docs.]

## 7.4 Báo cáo tiến độ và nhật ký tuần

[Báo cáo tiến độ 1 (M2, 04/12/2026): chèn nội dung khi có.]
[Báo cáo tiến độ 2 (M4, 18/12/2026): chèn nội dung khi có.]
Nhật ký tiến độ hằng tuần và bảng rủi ro cập nhật ở `docs/PROJECT_RECORDS.md`, sao chép vào Phụ lục B khi nộp.

## 7.5 Quản lý rủi ro

**Bảng 7.3. Rủi ro chính và biện pháp**

| Rủi ro | Mức ảnh hưởng | Biện pháp | Tình trạng |
|---|---|---|---|
| Rò rỉ thông tin làm điểm mô hình cao giả | Cao | Kiểm CO2 và công thức công suất; báo cả bản bỏ cột; chia tập theo thời gian | Đã xảy ra, đã xử lý (mục 4.1.2, 5.2) |
| Phân lớp nhầm lẫn giữa Medium và Maximum | Trung bình | Thử trọng số lớp và đặc trưng trễ; ghi trung thực kết quả | Đã thử, không cải thiện (mục 5.3.4) |
| Chương 5 (phân cụm) chưa có tài liệu | Trung bình | Chọn k-means, ghi rõ cách chọn k | Chưa làm (Việt, T008) |
| Ngày giao đề và hạn nộp thật chưa biết | Cao | Hạn nội bộ tính lùi từ ngày thi; sửa khi có hạn thật | Đang theo dõi |
| Một thành viên chậm tiến độ làm chậm cả nhóm | Cao | Theo dõi hằng tuần theo task; con đường găng T006, T010, T012 và T004, T009 | Đang theo dõi |

## 7.6 Bảng tự đánh giá đóng góp (Phụ lục C)

Bảng tự đánh giá đóng góp (Phụ lục C) do từng thành viên điền ở cuối kỳ, tổng 100% và cả ba cùng xác nhận; minh chứng gồm lịch sử commit của từng người trên kho mã, các task đã nhận và hoàn thành, và các phần báo cáo đã viết. [Điền ở M6.]

# KHUNG CHO VIỆT (không phải phần của Phi)

Dưới đây là khung Chương 3 (T011) và Chương 6 (T012) do Phi soạn trước để Việt viết lại bằng lời của mình. Số trong Chương 6 đã đối chiếu với bản mới nhất ở trên.

## Chương 3. Thiết kế sơ bộ (khung cho T011)
> Từ 19/11/2026 Việt viết Chương 3 (T011) dựa trên khung này; Quy trình đã chốt là CRISP-DM (22/11/2026).

### 3.1 Quy trình phân tích: CRISP-DM
> Đã chốt: CRISP-DM (Phi, 22/11/2026; ghi ở `docs/decisions/README.md`). Không đổi sang KDD hay SEMMA.

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

## Chương 6. Kết luận (khung cho T012)
1. Tóm tắt trả lời ba câu hỏi bằng số ở 5.3.
2. Hạn chế: một nhà máy, một năm; tập kiểm tra cuối năm; nhãn do nguồn gán, cách gán **UNKNOWN**; hồi quy có công thức vật lý; mốc 00:00 mỗi ngày chưa rõ thuộc ngày nào.
3. Hướng phát triển: Random Forest; dự báo giờ kế tiếp; khuyến nghị dịch chuyển phụ tải (gợi ý của đề, không bắt buộc với nhóm 3 người).
