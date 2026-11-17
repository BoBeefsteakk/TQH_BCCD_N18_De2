"""Công cụ quản lý task: list | new | set | readme | check (chỉ dùng thư viện chuẩn)."""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import datetime
from fnmatch import fnmatch
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"

KEYS = ["id", "title", "phase", "checklist", "owner", "status", "due", "files", "depends"]
OWNERS = ["phi", "huan", "viet"]
STATUSES = ["todo", "doing", "review", "done"]
PHASES = ["P1", "P2", "P3", "P4", "P5"]

# Bảng sở hữu theo TEAM.md mục 3 (Phi sửa tại đây nếu TEAM.md đổi).
# Mẫu kết thúc bằng "/" = cả thư mục; còn lại so khớp fnmatch.
OWNED = {
    "phi": ["src/config.py", "src/data_prep.py", "src/models.py", "src/evaluate.py", "run_all.py",
            "data/download_data.py", "docs/", "tasks/", ".github/", "prompts/", "scripts/",
            "TEAM.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "README.md", "requirements.txt",
            "pytest.ini", ".gitignore", ".gitattributes"],
    "huan": ["src/viz.py", "docs/DATA_DICTIONARY.md", "docs/TESTCASES.md", "notebooks/huan_*"],
    "viet": ["src/assoc.py", "src/clustering.py", "src/reduce.py", "notebooks/viet_*"],
}
# Ai cũng được ({owner} thay bằng tên người làm).
COMMON = ["docs/trace_{owner}.md", "docs/ai_usage_log.md", "results/figures", "results/figures/",
          "results/tables", "results/tables/", "tests/", "tasks/"]
# Không ai được sửa (test dùng chung).
FORBIDDEN_ALL = ["tests/test_interfaces.py"]  # test dùng chung (giao diện hàm), chỉ Phi sửa qua PR riêng


def _match(path: str, pats: list) -> bool:
    for p in pats:
        if p.endswith("/"):
            if path.startswith(p) or path == p.rstrip("/"):
                return True
        elif fnmatch(path, p):
            return True
    return False


def path_allowed(owner: str, path: str):
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    if path in FORBIDDEN_ALL:
        return False, "là test dùng chung, không ai được sửa"
    common = [c.format(owner=owner) for c in COMMON]
    if _match(path, common) or _match(path, OWNED.get(owner, [])):
        return True, ""
    if any(_match(path, OWNED[o]) for o in OWNED if o != owner):
        return False, "thuộc quyền sở hữu của người khác"
    return False, "không nằm trong danh sách sở hữu (TEAM.md mục 3)"


def slugify(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:40].strip("-") or "task"


def split_front(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta = {}
            for ln in lines[1:i]:
                if ":" in ln:
                    k, v = ln.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, "\n".join(lines[i + 1:])
    return None, text


def read_tasks(tdir: Path):
    out = []
    for p in sorted(tdir.glob("T[0-9]*.md")):
        meta, _ = split_front(p.read_text(encoding="utf-8"))
        out.append((p, meta))
    return out


def parse_due(s: str):
    if s.strip().upper() == "TBD":  # chưa có hạn (đề không nêu ngày giao)
        return datetime.max
    try:
        return datetime.strptime(s, "%d/%m/%Y")
    except Exception:
        return datetime.max


def cmd_list(a, tdir):
    rows = []
    for _, m in read_tasks(tdir):
        if not m:
            continue
        if a.owner and m.get("owner") != a.owner:
            continue
        if a.status and m.get("status") != a.status:
            continue
        if a.phase and m.get("phase") != a.phase:
            continue
        rows.append(m)
    rows.sort(key=lambda m: (parse_due(m.get("due", "")), m.get("id", "")))
    cols = ["id", "owner", "phase", "status", "due", "title"]
    print(" | ".join(cols))
    for m in rows:
        print(" | ".join(m.get(k, "") for k in cols))
    return 0


def cmd_new(a, tdir):
    if a.who not in OWNERS:
        print(f"Lỗi: người làm phải là một trong {OWNERS}")
        return 1
    if a.phase not in PHASES:
        print(f"Lỗi: phase phải là một trong {PHASES}")
        return 1
    tpl = tdir / "_TEMPLATE.md"
    if not tpl.exists():
        print(f"Lỗi: không thấy {tpl}")
        return 1
    nums = [int(m["id"][1:]) for _, m in read_tasks(tdir) if m and re.fullmatch(r"T\d+", m.get("id", ""))]
    tid = f"T{(max(nums) + 1 if nums else 1):03d}"
    meta = {"id": tid, "title": a.title, "phase": a.phase, "checklist": a.check, "owner": a.who,
            "status": "todo", "due": a.due, "files": a.files or "", "depends": a.depends or "-"}
    _, body = split_front(tpl.read_text(encoding="utf-8"))
    body = body.replace("# T000 — Tiêu đề ngắn của task", f"# {tid} — {a.title}")
    front = "---\n" + "\n".join(f"{k}: {meta[k]}" for k in KEYS) + "\n---\n"
    path = tdir / f"{tid}-{a.who}-{slugify(a.title)}.md"
    path.write_text(front + body.lstrip("\n") + "\n", encoding="utf-8")
    print(f"Đã tạo {path}")
    return 0


def find_task(tdir: Path, tid: str):
    for p, m in read_tasks(tdir):
        if m and m.get("id") == tid:
            return p
    return None


def cmd_set(a, tdir):
    if a.field != "status" or a.value not in STATUSES:
        print(f"Lỗi: chỉ hỗ trợ `set Txxx status {'|'.join(STATUSES)}`")
        return 1
    p = find_task(tdir, a.id)
    if not p:
        print(f"Lỗi: không thấy task {a.id}")
        return 1
    lines = p.read_text(encoding="utf-8").split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    for i in range(1, end):
        if lines[i].startswith("status:"):
            lines[i] = f"status: {a.value}"
    p.write_text("\n".join(lines), encoding="utf-8")
    print(f"{a.id}: status = {a.value}")
    return 0


README_HEAD = """# Task của nhóm

1. Task do Phi tạo (`python scripts\\tasks.py new ...`); người làm không tự tạo hay đổi nội dung giao việc.
2. Tìm task có `owner` là bạn và `status: todo`, ưu tiên theo hạn (`due`).
3. Chỉ sửa các file ghi ở dòng `files:` của task; thông số lấy từ `src/config.py`.
4. Người làm chỉ đổi `status` (todo → doing → review) và điền mục "Kết quả"; Phi đặt `done` sau khi merge.
5. Commit theo mẫu `T003 feat(b3): ...`.
6. Kiểm tra: `python scripts\\tasks.py check`. Bảng dưới do `python scripts\\tasks.py readme` sinh, không sửa tay.
"""


def cmd_readme(a, tdir):
    by_phase = {}
    for p, m in read_tasks(tdir):
        if m:
            by_phase.setdefault(m.get("phase", "?"), []).append((p, m))
    out = [README_HEAD]
    for ph in sorted(by_phase):
        out.append(f"\n## {ph}\n")
        out.append("| id | owner | status | due | checklist | tiêu đề |")
        out.append("|---|---|---|---|---|---|")
        for p, m in sorted(by_phase[ph], key=lambda x: (parse_due(x[1].get("due", "")), x[1].get("id", ""))):
            out.append(f"| {m.get('id')} | {m.get('owner')} | {m.get('status')} | {m.get('due')} | "
                       f"{m.get('checklist')} | [{m.get('title')}]({p.name}) |")
    (tdir / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Đã ghi {tdir / 'README.md'}")
    return 0


def cmd_check(a, tdir):
    errs = []
    ids = set()
    tasks = read_tasks(tdir)
    for p, m in tasks:
        n = p.name
        if m is None:
            errs.append(f"{n}: thiếu front matter (hai dòng ---)")
            continue
        for k in KEYS:
            if k not in m or (m[k] == "" and k != "files"):
                errs.append(f"{n}: thiếu hoặc rỗng khóa `{k}`")
        if m.get("id") in ids:
            errs.append(f"{n}: trùng id {m.get('id')}")
        ids.add(m.get("id"))
        if m.get("owner") not in OWNERS:
            errs.append(f"{n}: owner `{m.get('owner')}` không hợp lệ (phi|huan|viet)")
        if m.get("status") not in STATUSES:
            errs.append(f"{n}: status `{m.get('status')}` không hợp lệ ({'|'.join(STATUSES)})")
        if m.get("phase") not in PHASES:
            errs.append(f"{n}: phase `{m.get('phase')}` không hợp lệ")
        if m.get("due", "").strip().upper() != "TBD" and parse_due(m.get("due", "")) == datetime.max:
            errs.append(f"{n}: due `{m.get('due')}` không đúng DD/MM/YYYY (hoặc TBD)")
        if m.get("owner") in OWNERS:
            for f in [x for x in m.get("files", "").split(",") if x.strip()]:
                ok, why = path_allowed(m["owner"], f)
                if not ok:
                    errs.append(f"{n}: file `{f.strip()}` không được giao cho {m['owner']} ({why})")
    for p, m in tasks:
        if m and m.get("depends", "-") not in ("-", ""):
            for d in m["depends"].split(","):
                if d.strip() not in ids:
                    errs.append(f"{p.name}: depends `{d.strip()}` không tồn tại")
    for e in errs:
        print("LỖI:", e)
    print(f"Đã kiểm {len(tasks)} task, {len(errs)} lỗi.")
    return 1 if errs else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", default=None, help="thư mục tasks (mặc định tasks/)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("list")
    s.add_argument("--owner")
    s.add_argument("--status")
    s.add_argument("--phase")
    s = sub.add_parser("new")
    s.add_argument("--who", required=True)
    s.add_argument("--phase", required=True)
    s.add_argument("--check", required=True)
    s.add_argument("--due", required=True)
    s.add_argument("--files", default="")
    s.add_argument("--depends", default="-")
    s.add_argument("title")
    s = sub.add_parser("set")
    s.add_argument("id")
    s.add_argument("field")
    s.add_argument("value")
    sub.add_parser("readme")
    sub.add_parser("check")
    a = ap.parse_args(argv)
    tdir = Path(a.dir) if a.dir else TASKS_DIR
    fn = {"list": cmd_list, "new": cmd_new, "set": cmd_set, "readme": cmd_readme, "check": cmd_check}[a.cmd]
    return fn(a, tdir)


if __name__ == "__main__":
    sys.exit(main())
