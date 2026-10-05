# API 요청 처리
import json

from .services import expenses as expense_service
from .services import summary as summary_service


def handle_get_expenses(storage, query):
    """GET /api/expenses — 지출 목록을 돌려준다."""
    month = query.get("month")
    result = expense_service.list_expenses(storage, month=month)
    return 200, [e.to_dict() for e in result]


def handle_post_expense(storage, body):
    """POST /api/expenses — 지출 한 건을 등록한다."""
    try:
        data = json.loads(body)
    except (json.JSONDecodeError, TypeError):
        return 400, {"errors": ["본문이 올바른 JSON이 아니다"]}
    expense, errors = expense_service.add_expense(
        storage,
        date=data.get("date", ""),
        category=data.get("category", ""),
        amount=data.get("amount"),
        memo=data.get("memo", ""),
    )
    if errors:
        return 400, {"errors": errors}
    return 201, expense.to_dict()


def handle_get_summary(storage, query):
    """GET /api/summary — 월 합계와 카테고리별 합계를 돌려준다."""
    month = query.get("month")
    if not month:
        return 400, {"errors": ["month(YYYY-MM) 파라미터가 필요하다"]}
    all_expenses = storage.load()
    return 200, {
        "month": month,
        "total": summary_service.monthly_total(all_expenses, month),
        "by_category": summary_service.category_totals(all_expenses, month),
    }
