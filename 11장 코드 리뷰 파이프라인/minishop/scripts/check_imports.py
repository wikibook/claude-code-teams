"""의존성 방향 검사 (9.3.2).

규칙: 기능 계층(orders, coupons, refunds)은 서로를 참조할 수 없고,
공유 계층(models, pricing)은 기능 계층을 참조할 수 없다.

실행: python scripts/check_imports.py
"""
import ast
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src" / "minishop"

# 계층 정의: 숫자가 작을수록 아래(공유) 계층
LAYER = {"models": 0, "pricing": 1, "orders": 2, "coupons": 2, "refunds": 2}
FEATURE = [m for m, lv in LAYER.items() if lv == 2]
# 같은 계층 안에서 서로 참조를 금지할 모듈 쌍
FORBIDDEN_PEERS = {(a, b) for a in FEATURE for b in FEATURE if a != b}


def imports_of(path: Path) -> list[str]:
    """파일이 참조하는 minishop 내부 모듈 이름을 수집한다."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            # import minishop.refunds 형태
            names = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            # from minishop.pricing import x / from minishop import refunds /
            # from . import refunds 형태를 모두 수집한다
            base = node.module or ""
            names = [base] + [f"{base}.{alias.name}" for alias in node.names]
        else:
            continue
        for name in names:
            last = name.split(".")[-1]
            if last in LAYER:
                found.append(last)
    return found


def main() -> int:
    errors = []
    for path in SRC.glob("*.py"):
        me = path.stem
        if me not in LAYER:
            continue
        for target in imports_of(path):
            if (me, target) in FORBIDDEN_PEERS:
                errors.append(f"{me} → {target}: 기능 계층끼리는 참조할 수 없다")
            elif LAYER[target] > LAYER[me]:
                errors.append(f"{me} → {target}: 참조는 아래 계층으로만 흐른다")
    for e in errors:
        print(f"[위반] {e}")
    if not errors:
        print("의존성 방향: 위반 없음")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
