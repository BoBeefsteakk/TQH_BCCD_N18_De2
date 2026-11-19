# TQH_BCCD_N18_De2 — Đề 2: Phân loại chế độ phụ tải của khách hàng công nghiệp

Báo cáo chuyên đề học phần **Phân tích và trực quan hóa dữ liệu (004759)**, Trường Đại học Điện lực. Lớp D18CNPM1, Nhóm 18, 3 thành viên. Dữ liệu: UCI Steel Industry Energy Consumption (35.040 bản ghi 15 phút, năm 2018).

> **Làm việc nhóm: đọc [`TEAM.md`](TEAM.md) trước.** Trạng thái: T001, T002 xong; `data_prep`, `models`, `evaluate`, `run_all` đã cài; `viz`, `assoc`, `clustering`, `reduce` còn là stub. Thông số ở [`src/config.py`](src/config.py).

## Môi trường
Python 3.12, trong `.venv`, thư viện ở `requirements.txt` (ghim `==`).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
$env:PYTHONUTF8=1
pip install -r requirements.txt
python scripts\doctor.py
```

## Tải dữ liệu
Nguồn: UCI Machine Learning Repository, Steel Industry Energy Consumption. Dữ liệu không nằm trong git (`data/raw/`); chỉ có script tải.

```powershell
python data\download_data.py
```

URL, kích thước và SHA-256 trong `src/config.py` **chưa kiểm chứng** (`UNKNOWN`) cho đến khi tải lần đầu (task T001). Nếu tải tự động lỗi, tải tay bằng trình duyệt và đặt CSV vào `data/raw/steel.csv`.

## Chạy lại kết quả
```powershell
python run_all.py          # dữ liệu (khối B) + mô hình, đánh giá (E, G); ~13 giây
python -m pytest           # cấu trúc, cấu hình, giao diện, số ma thuật, công cụ task
```

## Thống nhất cách làm việc, cấu hình, môi trường
Mục tiêu: ba người, ba AI vẫn cho ra cùng một con số. Quy tắc đầy đủ: [`TEAM.md`](TEAM.md), [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md).

### Mỗi loại thông tin chỉ có một chỗ
| Loại | Nơi duy nhất | Ai sửa |
|---|---|---|
| Thông số (SEED, ngưỡng, tên cột, nguồn dữ liệu) | [`src/config.py`](src/config.py) | Chỉ Phi |
| Quy ước, định nghĩa, tên tệp hình/bảng | [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md) | Chỉ Phi |
| Quyết định đổi thông số hoặc quy ước | [`docs/decisions/`](docs/decisions/README.md) | Chỉ Phi |
| Checklist theo phase (khớp rubric của đề) | [`docs/CHECKLIST.md`](docs/CHECKLIST.md) | Chỉ Phi |
| Task linh động | [`tasks/`](tasks/README.md) | Phi tạo; người nhận cập nhật trạng thái |
| Hồ sơ nhóm (phiếu đăng ký, kế hoạch, rủi ro, tự đánh giá) | [`docs/PROJECT_RECORDS.md`](docs/PROJECT_RECORDS.md) | Phi |
| Luật cho AI | `TEAM.md`, `AGENTS.md` | Chỉ Phi |

### Môi trường
- **Hệ điều hành, shell:** Windows, PowerShell. CI chạy Ubuntu nên đường dẫn trong mã dùng `pathlib`.
- **Python 3.12** trong `.venv`; đặt `$env:PYTHONUTF8=1` để in tiếng Việt không lỗi.
- **Thư viện:** theo `requirements.txt`, đã ghim đúng phiên bản. Muốn thêm thư viện, báo Phi; đề chỉ cho phép NumPy, Pandas, Matplotlib, scikit-learn, mlxtend, statsmodels, NetworkX.
- **Kiểm môi trường:** `python scripts\doctor.py` kiểm Python, thư viện, venv, nhánh, `git config user.name` khớp nhánh, dữ liệu, tệp lớn.

### Nhánh, commit, PR
- Chỉ **4 nhánh**: `main` (chỉ nhận PR, chỉ Phi merge, merge commit) và 3 nhánh cá nhân. Không tạo nhánh theo task.

| Người | `git config user.name` | Nhánh duy nhất |
|---|---|---|
| Nguyễn Bảo Phi (trưởng nhóm) | `Nguyen Bao Phi` | `phi-lead-data-models` |
| Đỗ Minh Huấn | `Do Minh Huan` | `huan-viz-testcases` |
| Nguyễn Serov Trọng Việt | `Nguyen Serov Trong Viet` | `viet-assoc-cluster` |

- Mỗi người một PR thường trực `<nhánh> → main`; đã có thì chỉ push thêm.
- Commit: `T004 feat(c): them bieu do phan bo` (mã task; Phi dùng `LEAD`; loại `feat|fix|test|docs|chore`). CI từ chối commit sai mẫu.
- Cấm: `push --force`, `reset --hard`, `rebase`, `add .`, push lên nhánh người khác, tạo nhánh thứ năm.
- Mỗi buổi làm bắt đầu bằng: `checkout` nhánh mình → `pull` → `merge origin/main` → `doctor.py`. Xung đột thì dừng và báo Phi.

### File sở hữu (mỗi file một chủ)
| Người | Được sửa |
|---|---|
| Phi | `src/config.py`, `data_prep`, `models`, `evaluate`, `run_all.py`, `data/download_data.py`, `docs/`, `tasks/`, `scripts/`, `.github/`, `prompts/`, `TEAM.md`, `AGENTS.md` |
| Huấn | `src/viz.py`, `docs/DATA_DICTIONARY.md`, `docs/TESTCASES.md`, `docs/BAOCAO_DINH_DANG.md`, `notebooks/huan_*` |
| Việt | `src/assoc.py`, `clustering.py`, `reduce.py`, `notebooks/viet_*`, `docs/BAOCAO_NHAP_VIET.md`, `docs/SLIDE_NHAP.md` |

Cần sửa file người khác: ghi vào task, nhắn chủ file.

### Dùng AI
Xem `TEAM.md` mục 8. Trưởng nhóm đã bỏ tối đa ràng buộc AI: AI được viết mã và hỗ trợ báo cáo, repo không giữ nhật ký AI. Đề vẫn yêu cầu khai báo công cụ AI ở phụ lục (mỗi người tự khai đúng thực tế) và không nói rõ AI có được viết mã, báo cáo không; rủi ro nhóm tự chịu.

### Máy chặn, và quy ước thuần túy
| Có test hoặc CI chặn | Chỉ là quy ước (cần người kiểm) |
|---|---|
| Số "ma thuật" trong `src/` (`test_no_magic_numbers`) | Số trong báo cáo Google Docs phải lấy từ `results/` |
| Chữ ký hàm trong `src/` (`test_interfaces`) | Notebook không chứa hằng số tự đặt, đã xóa output |
| Cấu hình khớp đề (`test_config`) | Mỗi hình có tiêu đề, nhãn trục, đơn vị, nhận xét |
| Mẫu commit, tệp > 1 MB, dữ liệu thô bị track, file task | Công thức và nhãn trong `CONVENTIONS.md` |
| Nhánh và `user.name` khớp nhau (`doctor.py`, chạy tay) | Không push lên nhánh người khác (đã bảo vệ `main`) |

### Còn mở (chưa kết luận)
- Ngày thi: 10/01/2027 (Phi báo). **UNKNOWN:** ngày giao đề, hạn nộp thật, kênh nộp. Nhóm đã đăng ký Đề 2 (Phi xác nhận trên sheet).
- Dữ liệu đã kiểm (T001, T002): URL, SHA-256, tên cột, 35.040 dòng; CO2 gần suy ra từ `Usage_kWh` (loại); `Load_Type` không suy ra trực tiếp từ `Usage_kWh`.
- **UNKNOWN:** mốc 00:00 mỗi ngày thuộc ngày D hay D+1 (365 dòng). **Đã quyết:** hồi quy Usage_kWh giữ công suất phản kháng và hệ số công suất làm đầu vào; đã kiểm Usage_kWh = Q·PF/√(1−PF²), nên R² 0,999 là tái tạo công thức và báo cáo phải nói rõ.
- **UNKNOWN:** Chương 5 (phân cụm) có tài liệu không; seaborn/plotly có được dùng không; giảng viên có chấp nhận AI viết mã và báo cáo không.

## Checklist theo phase
Tóm tắt từ [`docs/CHECKLIST.md`](docs/CHECKLIST.md) (mã khớp Rubric R3, tổng 10,0). Task hằng ngày ở [`tasks/`](tasks/README.md).

| Phase | Mốc của đề | Việc chính (mã chấm) |
|---|---|---|
| P1 | Hết tuần 1 | Khối A (1.1), phiếu đăng ký và kế hoạch, tải dữ liệu |
| P2 | Hết tuần 2 | Khối B, C, D: 2.1, 2.2, 2.3, 3.1, 3.2, 4.1 |
| P3 | Hết tuần 3 | Khối E, F, G: 4.2, 4.3, 4.4, 3.3, 5.1, 5.2, 5.3 |
| P4 | Tuần 4, trước buổi báo cáo 2 ngày | Hoàn thiện: 3.4, 6.1, 6.2, 7.1, 7.2; tệp nén `D18CNPM1_Nhom18_De2.zip` |
| P5 | Buổi thi | Vấn đáp 7.3, trình bày 10 phút |

## Cấu trúc
```
TEAM.md  README.md  AGENTS.md  CLAUDE.md  GEMINI.md
src/        config, data_prep, reduce, viz, assoc, models, clustering, evaluate
data/       download_data.py (data/raw/ không vào git; data/clean/ là dữ liệu sạch nộp kèm)
notebooks/  huan_*, viet_*, phi_*  (xóa output trước khi commit)
results/    figures/, tables/  (do mã sinh ra)
docs/       CHECKLIST, CONVENTIONS, DE2, BAOCAO_DAN_Y, BAOCAO_NHAP_PHI, PHI/HUAN/VIET, PROJECT_RECORDS, TESTCASES, DATA_DICTIONARY, decisions/
tasks/      Txxx-*.md  (scripts/tasks.py)
scripts/    doctor.py, tasks.py
tests/      pytest
```
