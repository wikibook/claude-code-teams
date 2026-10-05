# 지출 등록과 조회
from .. import models


def add_expense(storage, date, category, amount, memo=""):
    """지출 한 건을 검증해 저장한다. (Expense, 오류 목록)을 돌려준다."""
    errors = models.validate(date, category, amount, memo)
    if errors:
        return None, errors
    expense = models.Expense(
        id=storage.next_id(),
        date=date,
        category=category,
        amount=amount,
        memo=memo,
    )
    all_expenses = storage.load()
    all_expenses.append(expense)
    storage.save(all_expenses)
    return expense, []


def list_expenses(storage, month=None):
    """지출 목록을 최신 날짜순으로 돌려준다. month(YYYY-MM)를 주면 그 달만 남긴다."""
    expenses = storage.load()
    if month:
        expenses = [e for e in expenses if e.date[:7] == month]
    return sorted(expenses, key=lambda e: (e.date, e.id), reverse=True)
