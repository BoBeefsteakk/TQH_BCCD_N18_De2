"""Kiểm tra môi trường làm việc (Đề 2, Nhóm 18). Chạy: python scripts\\doctor.py

Mức import đầu file chỉ dùng thư viện chuẩn. Thoát mã 1 nếu có LỖI; CẢNH BÁO không làm thoát lỗi.
"""
from __future__ import annotations

import hashlib
import importlib
import os
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Bảng người, nhánh (TEAM.md mục 1). Sửa ở đây khi TEAM.md đổi.
BRANCH_USER = {
    "phi-lead-data-models": "Nguyen Bao Phi",
    "huan-viz-testcases": "Do Minh Huan",
    "viet-assoc-cluster": "Nguyen Serov Trong Viet",
}
# Thư viện bắt buộc: tên import theo tên gói trong requirements.txt.
IMPORT_NAMES = {"numpy": "numpy", "pandas": "pandas", "matplotlib": "matplotlib",
                "scikit-learn": "sklearn", "mlxtend": "mlxtend", "statsmodels": "statsmodels",
                "networkx": "networkx", "pytest": "pytest"}


class Doctor:
    def __init__(self) -> None:
        self.passes = self.warnings = self.errors = 0

    def ok(self, msg: str) -> None:
        self.passes += 1
        print(f"[ĐẠT] {msg}")

    def warn(self, msg: str, hint: str) -> None:
        self.warnings += 1
        print(f"[CẢNH BÁO] {msg} -> {hint}")

    def error(self, msg: str, hint: str) -> None:
        self.errors += 1
        print(f"[LỖI] {msg} -> {hint}")


def git(*args: str) -> str | None:
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:  # noqa: BLE001
        return None


def check_python(d: Doctor) -> None:
    v = sys.version_info
    if (v.major, v.minor) == (3, 12):
        d.ok(f"Python {v.major}.{v.minor}.{v.micro}")
    else:
        d.error(f"Python {v.major}.{v.minor}.{v.micro}, nhóm dùng 3.12", "cài Python 3.12 rồi tạo lại .venv")


def check_venv(d: Doctor) -> None:
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        d.ok("Đang chạy trong môi trường ảo")
    else:
        d.warn("Không ở trong .venv", r"chạy .\.venv\Scripts\Activate.ps1")
    if os.environ.get("PYTHONUTF8") == "1":
        d.ok("PYTHONUTF8=1")
    else:
        d.warn("PYTHONUTF8 chưa đặt", r"PowerShell: $env:PYTHONUTF8=1")


def check_dependencies(d: Doctor) -> None:
    req = ROOT / "requirements.txt"
    pinned: dict[str, str] = {}
    for line in req.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "==" in line:
            name, ver = line.split("==", 1)
            pinned[name.strip().lower()] = ver.strip()
    if not pinned:
        d.warn("requirements.txt chưa ghim thư viện nào", "Phi ghim bằng == sau khi cài sạch và chạy test")
    for pkg, ver in pinned.items():
        mod = IMPORT_NAMES.get(pkg, pkg.replace("-", "_"))
        try:
            m = importlib.import_module(mod)
            got = getattr(m, "__version__", "?")
            if got == ver:
                d.ok(f"{pkg} {got}")
            else:
                d.error(f"{pkg} {got}, requirements.txt ghim {ver}", "pip install -r requirements.txt")
        except ImportError:
            d.error(f"Thiếu thư viện {pkg}", "pip install -r requirements.txt")


def check_git(d: Doctor) -> None:
    branch = git("branch", "--show-current")
    user = git("config", "user.name")
    if branch is None:
        d.warn("Không đọc được nhánh git", "kiểm tra thư mục đã clone đúng chưa")
        return
    if branch == "main":
        d.warn("Đang ở nhánh main", "main chỉ nhận PR; checkout nhánh cá nhân của bạn")
    elif branch in BRANCH_USER:
        d.ok(f"Nhánh hợp lệ: {branch}")
    else:
        d.error(f"Nhánh '{branch}' không thuộc 4 nhánh được phép", "chỉ dùng main và 3 nhánh cá nhân (TEAM.md mục 1)")
    if user not in BRANCH_USER.values():
        d.error(f"git config user.name = '{user}' không khớp bảng TEAM.md",
                'git config user.name "<tên ở bảng mục 1 của TEAM.md>"')
    elif branch in BRANCH_USER and BRANCH_USER[branch] != user:
        d.error(f"user.name '{user}' không khớp nhánh '{branch}' (kỳ vọng '{BRANCH_USER[branch]}')",
                "chuyển đúng nhánh hoặc sửa user.name")
    else:
        d.ok(f"user.name = {user}")


def check_data(d: Doctor) -> None:
    from src import config
    dest = config.RAW_DIR / config.DATA_LOCAL_NAME
    if not dest.exists():
        d.warn(f"Chưa có {dest.relative_to(ROOT)}", "python data/download_data.py")
        return
    size = dest.stat().st_size
    if config.DATA_SHA256 is None:
        d.warn(f"Có dữ liệu ({size} byte) nhưng config.DATA_SHA256 chưa điền (UNKNOWN)",
               "Phi điền size và sha256 do download_data.py in ra")
        return
    h = hashlib.sha256()
    with open(dest, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    if size == config.DATA_SIZE_BYTES and h.hexdigest() == config.DATA_SHA256:
        d.ok("Dữ liệu đúng kích thước và SHA-256")
    else:
        d.error("Dữ liệu sai kích thước hoặc SHA-256", "xóa tệp trong data/raw/ rồi tải lại")


def check_large_files(d: Doctor) -> None:
    out = git("ls-files")
    if out is None:
        return
    big = [p for p in out.splitlines() if (ROOT / p).is_file() and (ROOT / p).stat().st_size > 1_048_576]
    raw = [p for p in out.splitlines() if p.startswith(("data/raw/", ".venv/"))]
    if big or raw:
        d.error(f"Tệp > 1 MB hoặc dữ liệu thô bị track: {big + raw}", "git rm --cached <tệp> rồi thêm vào .gitignore")
    else:
        d.ok("Không có tệp lớn hay dữ liệu thô trong git")


def main() -> int:
    d = Doctor()
    for fn in (check_python, check_venv, check_dependencies, check_git, check_data, check_large_files):
        fn(d)
    print(f"\nĐạt {d.passes}, cảnh báo {d.warnings}, lỗi {d.errors}")
    return 1 if d.errors else 0


if __name__ == "__main__":
    sys.exit(main())
