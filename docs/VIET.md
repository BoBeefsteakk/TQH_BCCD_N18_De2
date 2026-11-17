# VIỆT — Nguyễn Serov Trọng Việt

Nhánh: `viet-assoc-cluster`. Đọc `TEAM.md` trước.

## Phần của bạn
- **Khối D** (`src/assoc.py`): rời rạc hóa khung giờ, mức tiêu thụ, mức hệ số công suất; Apriori hoặc FP-growth; luật có vế phải là `Load_Type`; diễn giải ≥ 5 luật; tương quan giữa các thuộc tính.
- **Khối F** (`src/clustering.py`): k-means, chọn k bằng khuỷu tay và silhouette, đối chiếu cụm với `Load_Type`. Chương 5 chưa có tài liệu (`UNKNOWN`), nên ghi rõ cách chọn tham số.
- **Giảm chiều** (`src/reduce.py`): PCA hoặc chọn thuộc tính, khớp trên tập huấn luyện.

## Mã chấm chính
2.3 (cùng Phi), 3.2 (cùng Huấn, trực quan luật kết hợp), 4.1, 4.3.
