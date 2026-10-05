# 집계 테스트
from moneylog import models
from moneylog.services import summary


def make_expense(id, date, category, amount):
    return models.Expense(id=id, date=date, category=category, amount=amount)


def test_해당_월의_지출만_합산한다():
    expenses = [
        make_expense(1, "2026-07-01", "식비", 10000),
        make_expense(2, "2026-07-15", "교통", 5000),
        make_expense(3, "2026-06-30", "식비", 99999),
    ]
    assert summary.monthly_total(expenses, "2026-07") == 15000


def test_카테고리별로_합산한다():
    expenses = [
        make_expense(1, "2026-07-01", "식비", 10000),
        make_expense(2, "2026-07-02", "식비", 20000),
        make_expense(3, "2026-07-03", "교통", 5000),
    ]
    totals = summary.category_totals(expenses, "2026-07")
    assert totals == {"식비": 30000, "교통": 5000}


def test_지출이_없는_달은_0이다():
    assert summary.monthly_total([], "2026-07") == 0
