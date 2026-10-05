# 예산 경고

## 목표
카테고리별 월 예산을 설정하고, 그 달의 지출이 예산을 넘으면 화면에서 경고를
보여준다.

## 범위 밖
- 예산의 다음 달 이월, 알림(메일·푸시) 발송, 예산 변경 이력

## 데이터
- data/budgets.json에 저장한다. 형식: {"식비": 300000, "교통": 100000}
- expenses.json은 변경하지 않는다.

## 인터페이스
- GET /api/budgets → 200, {"식비": 300000, ...}
- PUT /api/budgets → 본문 {"카테고리": 금액}, 성공 200. 금액이 양의 정수가
  아니면 400과 {"errors": [...]}
- GET /api/summary?month=YYYY-MM 응답에 "alerts" 배열을 추가한다.
  초과 항목: {"category": "식비", "budget": 300000, "spent": 321000,
  "over": 21000}
- services/budget.py: get_budgets(storage), set_budget(storage, category,
  amount), over_budget(expenses, budgets, month)

## 판정 규칙
- 초과 판정은 환불을 차감한 순지출 기준이다.
- 예산이 설정되지 않은 카테고리는 경고하지 않는다.

## 검증
1. python -m pytest tests/ 전체 통과 (budget 테스트 포함)
2. 브라우저에서 식비 예산을 30000으로 설정하고 2026-07 조회 시 식비 경고가
   보일 것
3. 예산 미설정 카테고리(기타)는 경고가 없을 것
