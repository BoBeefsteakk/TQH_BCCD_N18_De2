# VIỆT — Nguyễn Serov Trọng Việt

Nhánh: `viet-assoc-cluster`. Đọc `TEAM.md` trước.

## Phần của bạn
- **Khối D** (`src/assoc.py`): rời rạc hóa khung giờ, mức tiêu thụ, mức hệ số công suất; Apriori hoặc FP-growth; luật có vế phải là `Load_Type`; diễn giải ≥ 5 luật; tương quan giữa các thuộc tính.
- **Khối F** (`src/clustering.py`): k-means, chọn k bằng khuỷu tay và silhouette, đối chiếu cụm với `Load_Type`. Chương 5 chưa có tài liệu (`UNKNOWN`), nên ghi rõ cách chọn tham số.
- **Giảm chiều** (`src/reduce.py`): PCA hoặc chọn thuộc tính, khớp trên tập huấn luyện. Thêm (T010, chuyển từ Phi 19/11/2026): so sánh có và không giảm chiều cho phân lớp và hồi quy, viết trong `reduce.py`.
- **Chương 6 báo cáo** (T012) và **dàn ý slide, kịch bản demo** (T013, `docs/SLIDE_NHAP.md`): chuyển từ Phi 19/11/2026.
- **Chương 3 báo cáo** (T011, chuyển từ Phi 19/11/2026): thiết kế sơ bộ, viết ở `docs/BAOCAO_NHAP_VIET.md` từ khung trong `docs/BAOCAO_NHAP_PHI.md`.

## Mã chấm chính
1.1 (cùng Phi: Chương 3), 5.3 (Chương 6), 7.2 (slide, cùng cả nhóm), 2.3 (cùng Phi), 3.2 (cùng Huấn, trực quan luật kết hợp), 4.1, 4.2 (cùng Phi: so sánh giảm chiều), 4.3.
