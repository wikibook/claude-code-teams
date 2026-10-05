---
paths:
  - "src/graphql/**/*.ts"
  - "src/rest/**/*.ts"
---

# API 설계 규칙

- 모든 엔드포인트는 입력 검증을 포함할 것
- 오류 응답은 표준 형식 {"errors": [...]}을 쓸 것
