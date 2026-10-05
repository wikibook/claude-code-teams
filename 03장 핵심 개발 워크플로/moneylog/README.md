# moneylog

3장 실습용 예제. 브라우저에서 쓰는 간단한 지출 가계부 웹 애플리케이션이다.

## 구성

- `run.py` — 서버 실행 진입점. `python run.py`로 실행하고 브라우저에서 `http://localhost:8000`을 연다.
- `moneylog/` — 백엔드 패키지 (파이썬 표준 라이브러리만 사용)
  - `server.py` — HTTP 서버와 라우팅
  - `api.py` — API 요청 처리
  - `models.py` — 지출 데이터 모델과 입력 검증
  - `storage.py` — JSON 파일 저장소
  - `services/` — 지출 등록·조회(`expenses.py`), 집계(`summary.py`)
- `static/` — 화면 (`index.html`, `app.js`, `style.css`)
- `tests/` — pytest 테스트
- `data/` — 지출 데이터 파일 (샘플: `sample_expenses.json`)

## 사용법

```
python run.py                 # 서버 실행 (기본 포트 8000)
python -m pytest tests/       # 테스트 실행
```

지출 데이터는 `data/expenses.json`에 저장된다. 처음 실행하면 샘플 데이터를 복사해 시작한다.

## API

| 메서드 | 경로 | 설명 |
|---|---|---|
| GET | `/api/expenses?month=YYYY-MM` | 지출 목록 조회 (month 생략 시 전체) |
| POST | `/api/expenses` | 지출 등록 (음수 금액은 환불) |
| GET | `/api/summary?month=YYYY-MM` | 월 합계와 카테고리별 합계 |
