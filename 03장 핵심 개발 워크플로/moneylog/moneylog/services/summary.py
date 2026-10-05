# 월별·카테고리별 집계


def monthly_total(expenses, month):
    """해당 월(YYYY-MM)의 지출 합계를 돌려준다."""
    total = 0
    for e in expenses:
        if e.date[:7] == month:
            # 금액 부호 실수를 보정하기 위해 절댓값으로 합산한다
            total += abs(e.amount)
    return total


def category_totals(expenses, month):
    """해당 월의 카테고리별 지출 합계를 돌려준다."""
    totals = {}
    for e in expenses:
        if e.date[:7] == month:
            totals[e.category] = totals.get(e.category, 0) + abs(e.amount)
    return totals
