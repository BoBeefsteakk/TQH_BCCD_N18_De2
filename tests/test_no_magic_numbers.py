"""Kiểm tra không có hằng số "ma thuật" trong src/ (đề 2, nhóm 18).

Quét AST của các file Python trong src/ (trừ src/config.py và src/guards.py), báo lỗi nếu
trong MÃ (không tính docstring của module/class/hàm, không tính f-string chỉ để in)
có hằng số số học thuộc {4759, 35040, 1.5, 0.2}
hoặc hằng chuỗi khớp regex ngày ^\\d{4}-\\d{2}-\\d{2}.
"""
from __future__ import annotations

import ast
from pathlib import Path
import re
import pytest

MAGIC_NUMBERS = {4759, 35040, 1.5, 0.2}
DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}")

ROOT = Path(__file__).resolve().parents[1]


def find_magic(source: str) -> list[tuple[int, str]]:
    """Quét chuỗi mã nguồn Python và trả về danh sách (dòng, thông điệp) các hằng số ma thuật vi phạm.

    Bỏ qua:
    - Docstring của module, class, hàm (FunctionDef, AsyncFunctionDef).
    - F-string chỉ dùng để in (trong print hoặc lệnh ghi log/stdout).
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Gán thuộc tính parent cho mọi nút trong cây AST
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            child.parent = parent

    # Thu thập id của tất cả các nút Constant là docstring
    docstring_node_ids = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.body and isinstance(node.body[0], ast.Expr):
                expr = node.body[0]
                if isinstance(expr.value, ast.Constant) and isinstance(expr.value.value, str):
                    docstring_node_ids.add(id(expr.value))

    def is_in_print_fstring(node: ast.AST) -> bool:
        """Kiểm tra xem một nút có nằm trong f-string (JoinedStr) được truyền vào lệnh in (print) hay không."""
        curr = node
        in_joined_str = False
        while hasattr(curr, "parent"):
            curr = curr.parent
            if isinstance(curr, ast.JoinedStr):
                in_joined_str = True
            elif in_joined_str and isinstance(curr, ast.Call):
                func = curr.func
                if isinstance(func, ast.Name) and func.id == "print":
                    return True
                if isinstance(func, ast.Attribute) and func.attr in (
                    "write", "debug", "info", "warning", "error", "critical", "log"
                ):
                    return True
        return False

    violations: list[tuple[int, str]] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue

        # Bỏ qua docstring
        if id(node) in docstring_node_ids:
            continue

        # Bỏ qua f-string chỉ để in
        if is_in_print_fstring(node):
            continue

        val = node.value

        # 1. Kiểm tra hằng số số học (loại trừ bool vì bool kế thừa int trong Python)
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            is_magic = False
            if val in MAGIC_NUMBERS:
                is_magic = True
            elif isinstance(val, float) and any(abs(val - m) < 1e-9 for m in (0.2, 1.5)):
                is_magic = True

            if is_magic:
                violations.append((
                    node.lineno,
                    f"Phát hiện hằng số ma thuật {val} tại dòng {node.lineno}: lấy từ src/config.py"
                ))
                continue

        # 2. Kiểm tra hằng chuỗi định dạng ngày YYYY-MM-DD
        if isinstance(val, str) and DATE_REGEX.match(val):
            violations.append((
                node.lineno,
                f"Phát hiện hằng chuỗi ngày '{val}' tại dòng {node.lineno}: lấy từ src/config.py"
            ))

    violations.sort(key=lambda x: (x[0], x[1]))
    return violations


def test_find_magic_catches_fake_code_with_number_and_date():
    """Tự kiểm: chuỗi nguồn giả có x = 4759 và d = "2019-01-05" phải bị bắt."""
    fake_source = 'x = 4759\nd = "2019-01-05"\n'
    violations = find_magic(fake_source)
    assert len(violations) == 2, f"Kỳ vọng 2 vi phạm nhưng nhận được {len(violations)}"

    lines = [v[0] for v in violations]
    messages = [v[1] for v in violations]

    assert lines[0] == 1
    assert "4759" in messages[0]
    assert "lấy từ src/config.py" in messages[0]

    assert lines[1] == 2
    assert "2019-01-05" in messages[1]
    assert "lấy từ src/config.py" in messages[1]


def test_find_magic_ignores_docstrings():
    """Tự kiểm: chuỗi nguồn chỉ có hằng số trong docstring thì không bị bắt."""
    source_with_docstrings = '''"""Module docstring chứa 2026, 2044 và 2019-01-05."""

class SampleModel:
    """Class docstring chứa 4759, 35040, 1.5."""

    def predict(self):
        """Method docstring chứa 0.2 và 1.5."""
        return None


def sample_function():
    """Function docstring chứa mốc thời gian 2020-03-21."""
    pass
'''
    violations = find_magic(source_with_docstrings)
    assert violations == [], f"Kỳ vọng không có vi phạm trong docstrings, nhưng phát hiện: {violations}"


def test_find_magic_ignores_fstring_in_print():
    """Tự kiểm: f-string dùng cho lệnh in (print) không bị bắt."""
    source_with_print = '''
def log_progress(epoch, loss):
    print(f"Epoch {epoch}: lag=4759, date=2019-01-05, loss={loss}")
'''
    violations = find_magic(source_with_print)
    assert violations == [], f"Kỳ vọng bỏ qua f-string trong print, nhưng phát hiện: {violations}"


def test_find_magic_catches_fstring_outside_print():
    """Tự kiểm: f-string gán vào biến hoặc logic ngoài lệnh in vẫn bị bắt."""
    source = '''
date_str = f"2019-01-05"
lag_str = f"{4759}"
'''
    violations = find_magic(source)
    assert len(violations) == 2, f"Kỳ vọng 2 vi phạm nhưng nhận được: {violations}"
    assert any("2019-01-05" in v[1] for v in violations)
    assert any("4759" in v[1] for v in violations)


@pytest.mark.parametrize(
    "magic_val",
    [4759, 35040, 1.5, 0.2],
)
def test_find_magic_catches_all_magic_numbers(magic_val):
    """Tự kiểm: tất cả các số trong tập quy định đều bị phát hiện."""
    source = f"param = {magic_val}\n"
    violations = find_magic(source)
    assert len(violations) == 1
    assert "lấy từ src/config.py" in violations[0][1]


@pytest.mark.parametrize(
    "date_val",
    ["2018-01-01", "2018-06-30", "2018-12-31"],
)
def test_find_magic_catches_date_strings(date_val):
    """Tự kiểm: các chuỗi định dạng ngày đều bị phát hiện."""
    source = f'target_date = "{date_val}"\n'
    violations = find_magic(source)
    assert len(violations) == 1
    assert date_val in violations[0][1]
    assert "lấy từ src/config.py" in violations[0][1]


def test_no_magic_numbers_in_src():
    """Quét tất cả các file trong src/ (trừ src/config.py và src/guards.py).

    Test thật trên src/ hiện tại phải PASS (các stub hiện chỉ chứa số trong docstring).
    """
    src_dir = ROOT / "src"
    excluded_files = {"config.py", "guards.py"}
    all_violations = []

    py_files = sorted(src_dir.glob("*.py"))
    assert len(py_files) > 0, "Không tìm thấy file .py nào trong src/"

    for py_file in py_files:
        if py_file.name in excluded_files:
            continue
        source = py_file.read_text(encoding="utf-8")
        violations = find_magic(source)
        for lineno, msg in violations:
            all_violations.append(f"{py_file.name}:{lineno}: {msg}")

    assert not all_violations, (
        "Phát hiện vi phạm hằng số ma thuật trong src/:\n" + "\n".join(all_violations)
    )
