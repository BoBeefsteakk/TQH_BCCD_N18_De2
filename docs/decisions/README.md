# Nhật ký quyết định (chỉ Phi thêm dòng)

Đổi một hằng số trong `src/config.py` hoặc một quy ước trong `docs/CONVENTIONS.md` thì thêm một dòng ở đây trước khi merge.

| Ngày | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| 17/11/2026 | Nhóm 18 (lớp D18CNPM1) chọn Đề 2, nhóm 3 người | Phi quyết | Làm đủ yêu cầu tối thiểu, không có nội dung mở rộng bắt buộc |
| 17/11/2026 | `SEED = 4759` (mã học phần) | Đề không quy định công thức hạt giống; cần giá trị cố định để chạy lại được | Mọi `random_state` lấy từ `config.SEED` |
| 17/11/2026 | Cho phép AI viết code; không ép khai báo AI qua repo | Phi quyết; đề chỉ nói "tra cứu, giải thích, gỡ lỗi" nên rủi ro do nhóm tự chịu | `TEAM.md` mục 8 |
| 17/11/2026 | ĐỀ XUẤT, chờ Phi chốt: chia tập theo thời gian (`TEST_FRACTION` = 0,2 cuối năm) | Mẫu 15 phút liền kề tương quan mạnh; chia ngẫu nhiên gây rò rỉ | `config.SPLIT_MODE`, `docs/CONVENTIONS.md` mục 2 |
