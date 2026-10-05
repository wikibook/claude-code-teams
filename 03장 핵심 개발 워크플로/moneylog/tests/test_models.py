# 입력 검증 테스트
from moneylog import models


def test_올바른_입력은_통과한다():
    errors = models.validate("2026-07-01", "식비", 12000, "점심")
    assert errors == []


def test_잘못된_날짜_형식을_거른다():
    errors = models.validate("2026/07/01", "식비", 12000)
    assert any("날짜" in e for e in errors)


def test_없는_카테고리를_거른다():
    errors = models.validate("2026-07-01", "쇼핑", 12000)
    assert any("카테고리" in e for e in errors)


def test_금액_0을_거른다():
    errors = models.validate("2026-07-01", "식비", 0)
    assert any("금액" in e for e in errors)


def test_긴_메모를_거른다():
    errors = models.validate("2026-07-01", "식비", 12000, "가" * 101)
    assert any("메모" in e for e in errors)
