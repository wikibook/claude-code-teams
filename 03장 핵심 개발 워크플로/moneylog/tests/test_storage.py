# 저장소 테스트
from moneylog import models
from moneylog.storage import Storage


def make_storage(tmp_path):
    return Storage(path=tmp_path / "expenses.json")


def test_비어_있으면_빈_목록을_돌려준다(tmp_path):
    storage = make_storage(tmp_path)
    assert storage.load() == []


def test_저장한_지출을_다시_읽는다(tmp_path):
    storage = make_storage(tmp_path)
    expense = models.Expense(id=1, date="2026-07-01", category="식비", amount=12000)
    storage.save([expense])
    loaded = storage.load()
    assert len(loaded) == 1
    assert loaded[0] == expense


def test_next_id는_최대_id_다음_값이다(tmp_path):
    storage = make_storage(tmp_path)
    assert storage.next_id() == 1
    storage.save([models.Expense(id=7, date="2026-07-01", category="식비", amount=1000)])
    assert storage.next_id() == 8
