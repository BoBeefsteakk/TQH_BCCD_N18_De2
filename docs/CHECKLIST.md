# CHECKLIST — việc cố định theo phase (chỉ Phi sửa; Phi đổi ☐ → ☑ khi có bằng chứng)

Mã khớp mã chấm Rubric R3 của đề (tổng 10,0: nhóm 8,5, cá nhân 1,5). Việc linh động nằm ở `tasks/`. Hạn: ngày giao đề và ngày thi chưa biết (`UNKNOWN`), nên hạn ghi theo mốc tuần của đề; Phi điền ngày thật khi có.

## P1 — hết tuần 1: lập nhóm, chọn đề, khảo sát dữ liệu (khối A)
| Mã | Việc | Điểm | Người chính | |
|---|---|---|---|---|
| 1.1 | Bối cảnh, người dùng, ≥ 3 câu hỏi phân tích (Phi, Chương 1); chọn CRISP-DM/KDD/SEMMA và giải thích áp dụng (Việt viết Chương 3, Phi chốt) | 0,5 | Phi, Việt | ☐ |
| — | Phiếu đăng ký (Phụ lục A), kế hoạch và rủi ro (Phụ lục B) vào `docs/PROJECT_RECORDS.md` | (6.1) | Phi | ☐ |
| — | Tải dữ liệu, điền size và SHA-256 vào `src/config.py`, đối chiếu tên cột thật | — | Phi | ☐ |

## P2 — hết tuần 2: khối B, C, D (nộp báo cáo tiến độ 1 kèm notebook)
| Mã | Việc | Điểm | Người chính | |
|---|---|---|---|---|
| 2.1 | Từ điển dữ liệu, thống kê mô tả, phân loại thuộc tính | 0,25 | Huấn | ☐ |
| 2.2 | Làm sạch (thiếu, ngoại lai 1,5×IQR, trùng, vô lý), có số liệu trước và sau; kiểm CO2 và Load_Type có gần suy ra từ Usage_kWh không | 0,5 | Phi | ☐ |
| 2.3 | Chuẩn hóa/mã hóa, giảm chiều (PCA hoặc chọn thuộc tính), lưu `data/clean/steel_clean.csv` | 0,25 | Phi, Việt | ☐ |
| 3.1 | Biểu đồ phân bố và so sánh theo nhóm, theo thời gian (Usage_kWh theo Load_Type; heatmap giờ × thứ) | 0,5 | Huấn | ☐ |
| 3.2 | Biểu đồ quan hệ, tương quan (tán xạ công suất phản kháng – điện năng; ma trận tương quan); trực quan luật kết hợp | 0,5 | Huấn, Việt | ☐ |
| 4.1 | Khối D: Apriori hoặc FP-growth, luật vế phải Load_Type, support/confidence/lift, diễn giải ≥ 5 luật | 0,5 | Việt | ☐ |

## P3 — hết tuần 3: khối E, F, G (nộp báo cáo tiến độ 2 kèm bản nháp)
| Mã | Việc | Điểm | Người chính | |
|---|---|---|---|---|
| 4.2 | Khối E: phân lớp Load_Type ≥ 3 mô hình; hồi quy Usage_kWh; kiểm định chéo; so sánh có và không giảm chiều (Phi: mô hình; Việt: so sánh giảm chiều, T010) | 0,5 | Phi, Việt | ☐ |
| 4.3 | Khối F: k-means, chọn k bằng khuỷu tay và silhouette, đối chiếu cụm với Load_Type | 0,5 | Việt | ☐ |
| 4.4 | Chia tập hợp lý (theo thời gian), tránh rò rỉ, chỉnh tham số | 0,5 | Phi | ☐ |
| 3.3 | Trực quan hóa kết quả mô hình: ma trận nhầm lẫn, cụm, độ quan trọng thuộc tính hoặc hình cây | 0,5 | Huấn | ☐ |
| 5.1 | Bảng ca kiểm thử (Phụ lục D: mã ca, mục tiêu, dữ liệu, kết quả mong đợi, thực tế, nhận xét) | 0,5 | Huấn | ☐ |
| 5.2 | Độ đo phù hợp (accuracy, precision/recall/F1 từng lớp; MAE, RMSE, R²) và bảng so sánh mô hình | 0,5 | Phi | ☐ |
| 5.3 | Phân tích lỗi (cặp lớp bị nhầm nhiều nhất), đề xuất và thử cải thiện, trả lời các câu hỏi phân tích | 0,5 | Phi | ☐ |

## P4 — tuần 4, trước buổi báo cáo 2 ngày: hoàn thiện, nộp
| Mã | Việc | Điểm | Người chính | |
|---|---|---|---|---|
| 3.4 | Mọi biểu đồ (≥ 8, ≥ 4 loại) đủ tiêu đề, nhãn trục, đơn vị, một nhận xét | 0,5 | Huấn | ☐ |
| 6.1 | Kế hoạch, phân công, nhật ký tuần, bảng rủi ro cập nhật | 0,75 | Phi | ☐ |
| 6.2 | Bảng tự đánh giá đóng góp (Phụ lục C), cả nhóm xác nhận; lịch sử git đúng người | 0,75 (cá nhân) | Cả nhóm | ☐ |
| 7.1 | Báo cáo 20–30 trang (Times New Roman 13, giãn 1,3), có trích dẫn; PDF và DOCX | 0,5 | Cả nhóm | ☐ |
| 7.2 | Slide 10–12 trang; demo chạy được (`python run_all.py` từ dữ liệu gốc) | 0,25 | Cả nhóm | ☐ |
| — | Tệp nén `D18CNPM1_Nhom18_De2.zip`: báo cáo, mã + README + thư viện, dữ liệu sạch + từ điển, slide, hồ sơ nhóm | — | Phi | ☐ |

## P5 — buổi thi
| Mã | Việc | Điểm | |
|---|---|---|---|
| 7.3 | Vấn đáp: mỗi người ≥ 2 câu (phần mình, phần chung); trình bày 10 phút | 0,75 (cá nhân) | ☐ |

Mọi số liệu và hình trong báo cáo phải sinh ra từ mã đã nộp (đề, mục "Yêu cầu chung").
