"""Kiểm công cụ scripts/tasks.py trên thư mục tạm (không chạm tasks/ thật)."""
import importlib.util
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("tasks_tool", ROOT / "scripts" / "tasks.py")
tt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tt)


def _setup(tmp_path):
    shutil.copy(ROOT / "tasks" / "_TEMPLATE.md", tmp_path / "_TEMPLATE.md")
    return str(tmp_path)


def _new(d, who, files, title="Cài đặt thử", depends="-"):
    return tt.main(["--dir", d, "new", "--who", who, "--phase", "P2", "--check", "B3.1",
                    "--due", "25/11/2026", "--files", files, "--depends", depends, title])


def test_new_and_ids(tmp_path):
    d = _setup(tmp_path)
    assert _new(d, "huan", "src/viz.py") == 0
    assert _new(d, "viet", "src/assoc.py") == 0
    names = sorted(p.name for p in tmp_path.glob("T*.md"))
    assert names == ["T001-huan-cai-dat-thu.md", "T002-viet-cai-dat-thu.md"]
    assert tt.main(["--dir", d, "check"]) == 0


def test_set_status_and_list(tmp_path, capsys):
    d = _setup(tmp_path)
    _new(d, "huan", "src/viz.py")
    assert tt.main(["--dir", d, "set", "T001", "status", "doing"]) == 0
    assert "status: doing" in (tmp_path / "T001-huan-cai-dat-thu.md").read_text(encoding="utf-8")
    assert tt.main(["--dir", d, "set", "T001", "status", "xong"]) == 1
    capsys.readouterr()
    tt.main(["--dir", d, "list", "--status", "doing"])
    assert "T001" in capsys.readouterr().out
    tt.main(["--dir", d, "list", "--owner", "viet"])
    assert "T001" not in capsys.readouterr().out


def test_check_rejects_foreign_file(tmp_path, capsys):
    d = _setup(tmp_path)
    _new(d, "huan", "src/assoc.py")
    assert tt.main(["--dir", d, "check"]) == 1
    assert "assoc.py" in capsys.readouterr().out


def test_check_rejects_shared_test_and_bad_depends(tmp_path):
    d = _setup(tmp_path)
    _new(d, "phi", "tests/test_interfaces.py", depends="T009")
    assert tt.main(["--dir", d, "check"]) == 1


def test_readme(tmp_path):
    d = _setup(tmp_path)
    _new(d, "phi", "src/data_prep.py")
    assert tt.main(["--dir", d, "readme"]) == 0
    assert "T001" in (tmp_path / "README.md").read_text(encoding="utf-8")


def test_due_tbd_is_accepted(tmp_path):
    d = _setup(tmp_path)
    tt.main(["--dir", d, "new", "--who", "phi", "--phase", "P1", "--check", "A1", "--due", "TBD",
             "--files", "src/config.py", "Việc chưa có hạn"])
    assert tt.main(["--dir", d, "check"]) == 0
