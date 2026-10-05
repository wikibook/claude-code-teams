# 지출 데이터 모델과 입력 검증
import re
from dataclasses import dataclass, asdict

# 지출 분류에 사용하는 카테고리 목록
CATEGORIES = ["식비", "교통", "주거", "여가", "기타"]

_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass
class Expense:
    """지출 한 건. amount는 원 단위 정수이며 음수는 환불을 뜻한다."""

    id: int
    date: str  # YYYY-MM-DD
    category: str
    amount: int
    memo: str = ""

    def to_dict(self):
        return asdict(self)


def from_dict(row):
    """저장소의 딕셔너리 한 건을 Expense로 변환한다."""
    return Expense(
        id=row["id"],
        date=row["date"],
        category=row["category"],
        amount=row["amount"],
        memo=row.get("memo", ""),
    )


def validate(date, category, amount, memo=""):
    """입력값을 검증하고 오류 메시지 목록을 돌려준다. 비어 있으면 통과다."""
    errors = []
    if not _DATE_PATTERN.match(date or ""):
        errors.append("날짜는 YYYY-MM-DD 형식이어야 한다")
    if category not in CATEGORIES:
        errors.append("카테고리는 다음 중 하나여야 한다: " + ", ".join(CATEGORIES))
    if not isinstance(amount, int) or isinstance(amount, bool) or amount == 0:
        errors.append("금액은 0이 아닌 정수여야 한다")
    if len(memo or "") > 100:
        errors.append("메모는 100자 이하여야 한다")
    return errors
