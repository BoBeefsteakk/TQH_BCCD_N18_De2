"""Tải bộ UCI Steel Industry Energy Consumption vào data/raw/ (chủ: Phi). Chỉ dùng thư viện chuẩn.

Chạy: python data/download_data.py
URL, kích thước, SHA-256 trong src/config.py là NOT VERIFIED. Lần tải đầu script in kích thước và SHA-256
để điền vào config. Nếu tải tự động lỗi, tải tay bằng trình duyệt rồi đặt tệp CSV vào data/raw/.
"""
from __future__ import annotations

import hashlib
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import config  # noqa: E402


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    config.RAW_DIR.mkdir(parents=True, exist_ok=True)
    dest = config.RAW_DIR / config.DATA_LOCAL_NAME
    if not dest.exists():
        try:
            with urllib.request.urlopen(config.DATA_URL, timeout=60) as r:
                payload = r.read()
            with zipfile.ZipFile(io.BytesIO(payload)) as z:
                names = [n for n in z.namelist() if n.lower().endswith(".csv")]
                if not names:
                    print("Không thấy tệp .csv trong gói tải:", z.namelist())
                    return 1
                dest.write_bytes(z.read(names[0]))
        except Exception as exc:  # noqa: BLE001
            print(f"Tải tự động lỗi: {exc}\nTải tay từ {config.DATA_URL} rồi đặt CSV vào {dest}")
            return 1
    size, digest = dest.stat().st_size, sha256_of(dest)
    print(f"{dest.name}: {size} byte, sha256 = {digest}")
    if config.DATA_SHA256 is None:
        print("config.DATA_SHA256 chưa điền (UNKNOWN): Phi điền size và sha256 ở trên vào src/config.py.")
        return 0
    if digest != config.DATA_SHA256 or size != config.DATA_SIZE_BYTES:
        print("SAI kích thước hoặc SHA-256 so với src/config.py")
        return 1
    print("Đúng kích thước và SHA-256.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
