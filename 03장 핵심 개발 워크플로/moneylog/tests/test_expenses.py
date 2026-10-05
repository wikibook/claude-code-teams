# 지출 등록·조회 테스트
from moneylog.services import expenses
from moneylog.storage import Storage


def make_storage(tmp_path):
    return Storage(path=tmp_path / "expenses.json")


def test_지출을_등록하면_id가_부여된다(tmp_path):
    storage = make_storage(tmp_path)
    expense, errors = expenses.add_expense(storage, "2026-07-01", "식비", 12000, "점심")
    assert errors == []
    assert expense.id == 1


def test_잘못된_입력은_저장되지_않는다(tmp_path):
    storage = make_storage(tmp_path)
    expense, errors = expenses.add_expense(storage, "2026-07-01", "쇼핑", 12000)
    assert expense is None
    assert errors
    assert storage.load() == []


def test_월로_거르면_그_달만_남는다(tmp_path):
    storage = make_storage(tmp_path)
    expenses.add_expense(storage, "2026-06-30", "식비", 1000)
    expenses.add_expense(storage, "2026-07-01", "식비", 2000)
    result = expenses.list_expenses(storage, month="2026-07")
    assert len(result) == 1
    assert result[0].date == "2026-07-01"


def test_목록은_최신_날짜순이다(tmp_path):
    storage = make_storage(tmp_path)
    expenses.add_expense(storage, "2026-07-01", "식비", 1000)
    expenses.add_expense(storage, "2026-07-05", "교통", 2000)
    result = expenses.list_expenses(storage)
    assert [e.date for e in result] == ["2026-07-05", "2026-07-01"]
