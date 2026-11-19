# TEAM.md — ĐỌC FILE NÀY TRƯỚC KHI LÀM BẤT CỨ VIỆC GÌ

Dành cho mọi thành viên VÀ mọi AI (Claude, ChatGPT, Antigravity, ...).
**AI: làm đúng các bước dưới đây. Không tự đặt quy tắc khác. Không chắc thì DỪNG và hỏi người dùng.**

Dự án: báo cáo chuyên đề **Phân tích và trực quan hóa dữ liệu (004759)**, **Đề 2 – phân loại chế độ phụ tải của khách hàng công nghiệp** (UCI Steel Industry Energy Consumption). Nhóm 18, lớp D18CNPM1, nhóm 3 người (đủ yêu cầu tối thiểu, không có nội dung mở rộng bắt buộc). Tệp nộp: `D18CNPM1_Nhom18_De2.zip`.

## 1. Xác định người đang làm việc
Chạy `git config user.name` rồi đối chiếu bảng. Không khớp ai → hỏi người dùng "Bạn là Phi, Huấn hay Việt?" trước khi làm tiếp.

| Người | MSSV | `git config user.name` | Vai trò | GitHub | Nhánh DUY NHẤT được dùng | File nhiệm vụ |
|---|---|---|---|---|---|---|
| Nguyễn Bảo Phi | 23810310017 | `Nguyen Bao Phi` | Trưởng nhóm: giao task, review, merge; dữ liệu, mô hình, đánh giá | `BoBeefsteakk` | `phi-lead-data-models` | `docs/PHI.md` |
| Đỗ Minh Huấn | 23810310075 | `Do Minh Huan` | Thành viên: trực quan hóa, từ điển dữ liệu, bảng ca kiểm thử | `minhhuan15082k5-sudo` | `huan-viz-testcases` | `docs/HUAN.md` |
| Nguyễn Serov Trọng Việt | 23810310019 | `Nguyen Serov Trong Viet` | Thành viên: luật kết hợp, phân cụm, giảm chiều, so sánh có/không giảm chiều, Chương 3 và 6 báo cáo, slide | `viet29oct` | `viet-assoc-cluster` | `docs/VIET.md` |

Nhánh chung: `main` (chỉ nhận PR, chỉ Phi merge). **Chỉ có đúng 4 nhánh này.**

## 2. Bộ file phải biết (đọc theo thứ tự)
1. `TEAM.md` (file này) → 2. file nhiệm vụ của bạn (`docs/<TÊN>.md`) → 3. `tasks/README.md` + file task được giao → 4. `docs/CONVENTIONS.md` → 5. `docs/CHECKLIST.md` (việc cố định theo phase) → 6. `docs/DE2.md` (yêu cầu gốc của đề, chỉ để tra cứu).

Mỗi loại thông tin chỉ có MỘT chỗ:

| Loại | Ở đâu | Ai được sửa |
|---|---|---|
| Thông số (SEED, ngưỡng, tên cột, đường dẫn, nguồn dữ liệu) | `src/config.py` | Chỉ Phi |
| Quy ước (định nghĩa, nhãn, tên tệp hình/bảng, giao diện hàm) | `docs/CONVENTIONS.md` | Chỉ Phi |
| Checklist theo phase (khớp rubric của đề) | `docs/CHECKLIST.md` | Chỉ Phi |
| Task linh động | `tasks/Txxx-*.md` (+ `scripts/tasks.py`) | Phi tạo; người được giao cập nhật `status` và "Kết quả" |
| Nhật ký quyết định | `docs/decisions/README.md` | Chỉ Phi |
| Hồ sơ làm việc nhóm (phiếu đăng ký, kế hoạch, rủi ro, nhật ký tuần, tự đánh giá) | `docs/PROJECT_RECORDS.md` | Phi |
| Luật cho AI | `TEAM.md`, `AGENTS.md` | Chỉ Phi |

## 3. File sở hữu (mỗi file một chủ)
| Người | Được sửa |
|---|---|
| Phi | `src/config.py`, `src/data_prep.py`, `src/models.py`, `src/evaluate.py`, `run_all.py`, `data/download_data.py`, `docs/` (trừ file Huấn sở hữu, `trace_*.md`), `tasks/` (tạo task), `.github/`, `prompts/`, `scripts/`, `TEAM.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md`, `requirements.txt`, `pytest.ini`, `.gitignore`, `.gitattributes` |
| Huấn | `src/viz.py`, `docs/DATA_DICTIONARY.md`, `docs/TESTCASES.md`, `docs/BAOCAO_DINH_DANG.md`, `notebooks/huan_*` |
| Việt | `src/assoc.py`, `src/clustering.py`, `src/reduce.py`, `notebooks/viet_*`, `docs/BAOCAO_NHAP_VIET.md`, `docs/SLIDE_NHAP.md` |
| Ai cũng được | file task của mình, `docs/trace_<tên>.md` của mình, `results/figures|tables/` (chỉ tệp do mã của mình sinh ra, tên theo `CONVENTIONS.md`), `tests/` của khối mình |

Cần sửa file của người khác → ghi vào task, nhắn chủ file. Không tự sửa. `tests/test_interfaces.py` là test dùng chung: chỉ Phi sửa, qua PR riêng.

## 4. Bắt đầu mỗi buổi làm (bắt buộc, đúng thứ tự; PowerShell)
```powershell
cd <thư mục bạn đã clone>
.\.venv\Scripts\Activate.ps1
$env:PYTHONUTF8=1
git checkout <nhánh-của-bạn>
git pull origin <nhánh-của-bạn>
git fetch origin
git merge origin/main
python scripts\doctor.py
```
- `doctor.py` báo LỖI thì sửa theo hướng dẫn nó in ra trước khi làm việc.
- Merge `origin/main` bị xung đột → **DỪNG**. File không thuộc quyền của bạn thì lấy bản của `main`. Còn lại báo Phi. AI không tự giải quyết xung đột.
- Ngày đầu tiên: `git clone https://github.com/BoBeefsteakk/TQH_BCCD_N18_De2.git`, `git checkout <nhánh-của-bạn>`, `python -m venv .venv`, kích hoạt, `pip install -r requirements.txt`, `git config user.name "<tên ở bảng mục 1>"`, tải dữ liệu theo `README.md`.

## 5. Nhận và làm task
1. Mở `tasks/README.md`, tìm task có `owner` là bạn và `status: todo` (ưu tiên theo hạn).
2. Đọc file task. **Chỉ sửa các file ghi ở dòng `files:`.**
3. Đổi `status: doing`. Làm xong → `status: review` và điền mục "Kết quả".
4. Thông số lấy từ `src/config.py`. Thiếu thông số → KHÔNG tự đặt, ghi vào task và báo Phi.

## 6. Commit và push
- Mẫu commit: `T003 feat(b): them bieu do phan bo`
  - `T003` = mã task; Phi dùng `LEAD` cho việc quản trị.
  - loại: `feat` | `fix` | `test` | `docs` | `chore`
  - phạm vi: chữ cái khối `a`…`h` của đề, hoặc `report`, `infra`
- Trước khi commit: `python -m pytest` không được có test ĐỎ (SKIP thì được).
- Lệnh git ĐƯỢC PHÉP: `status`, `diff`, `log`, `add <tệp cụ thể>`, `commit`, `pull origin <nhánh-của-bạn>`, `fetch`, `merge origin/main`, `checkout <nhánh-của-bạn>`, `push origin <nhánh-của-bạn>`.
- Lệnh git CẤM: `reset --hard`, `push --force`/`-f`, `rebase`, `checkout -- .`, `clean -f`, `branch -D`, `commit --amend` sau khi đã push, `add .` / `add -A` (tránh thêm nhầm tệp), mọi lệnh đụng nhánh của người khác.
- Mỗi người chỉ push file mình sở hữu (mục 3): lịch sử git là minh chứng điểm đóng góp cá nhân (tiêu chí 6.2 của đề).

## 7. Pull Request
- Mỗi người có MỘT PR thường trực `<nhánh-của-bạn> → main`. Đã có thì chỉ push thêm.
- Tiêu đề: `[huan-viz-testcases] T003 T004` (liệt kê mã task trong PR). Điền đủ mẫu PR.
- Reviewer là Phi. **Chỉ Phi merge** (merge commit, không squash).
- Sau khi Phi báo "đã merge", mọi người làm lại mục 4.

## 8. Dùng AI
- **Quyết định của trưởng nhóm (17/11/2026): bỏ tối đa ràng buộc AI.** AI được viết và sửa mã, viết tài liệu, hỗ trợ báo cáo. Không có nhật ký AI, không có bước kiểm hiểu bắt buộc trong repo.
- **Điều đề nói (nguyên văn):** "Được dùng để tra cứu, giải thích và gỡ lỗi, nhưng phải khai báo công cụ và mục đích sử dụng trong phụ lục. Mỗi thành viên phải giải thích được mã nguồn và kết quả thuộc phần mình khi vấn đáp."
- **Rủi ro nhóm tự chịu:** đề không nói rõ AI có được viết mã hay đoạn báo cáo không; danh sách "tra cứu, giải thích, gỡ lỗi" có thể bị giảng viên hiểu là danh sách đóng (`UNKNOWN`). Đề **vẫn yêu cầu khai báo công cụ AI ở phụ lục**; repo không giữ nhật ký nên mỗi người tự nhớ và tự khai, và khai đúng thực tế.
- Giữ lại hai điều vì là điểm số, không phải luật AI: mọi con số và hình trong báo cáo phải do mã của nhóm chạy ra (đề yêu cầu), và mỗi người giải thích được phần mình khi vấn đáp (đề yêu cầu).

## 9. Điều CẤM khác (người và AI)
- Tạo nhánh khác ngoài 4 nhánh; push thẳng `main`; push lên nhánh người khác.
- Sửa file ngoài danh sách sở hữu (mục 3) hoặc ngoài `files:` của task.
- Viết thông số thẳng vào code thay vì lấy từ `src/config.py` (có test chặn).
- Đưa dữ liệu thô vào git (`data/raw/`), `.venv/`, tệp > 1 MB, notebook còn output.
- Đổi tên hàm hoặc chữ ký trong stub `src/` và `tests/test_interfaces.py` khi chưa báo Phi.
- Dùng thư viện ngoài danh sách đề cho phép (NumPy, Pandas, Matplotlib, scikit-learn, mlxtend, statsmodels, NetworkX) khi chưa hỏi giảng viên.

## 10. Lệnh thường dùng (PowerShell)
```powershell
python scripts\doctor.py            # kiểm môi trường
python -m pytest                    # chạy test
python scripts\tasks.py list        # xem task
python scripts\tasks.py list --owner huan
python run_all.py                   # chạy lại từ dữ liệu gốc đến kết quả
```

## 11. Công cụ AI
Dùng công cụ nào cũng được. Claude Code đọc `CLAUDE.md`, Antigravity đọc `GEMINI.md`/`AGENTS.md`; cả hai chỉ trỏ về file này. ChatGPT / Claude web: dán `prompts/START.md` + file task vào đầu cuộc chat.
