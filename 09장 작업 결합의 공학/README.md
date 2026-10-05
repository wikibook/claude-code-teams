# 9장 실습 안내: minishop

9장의 예제 저장소입니다. 가상의 쇼핑몰 백엔드(주문·쿠폰·환불)로, 결합 오류의
재현(9.1)부터 인터페이스 계약(9.2), 작업 분할과 결합 전 검증(9.3)까지를
이 저장소 하나로 완주합니다. 이 폴더의 minishop은 9장 완주 스냅샷입니다.
10~12장 실습은 각 장 폴더의 minishop(해당 장 완주 상태)을 사용합니다.

<br>

## 준비

- 파이썬 3.10 이상, pytest 7 이상이 필요합니다.
- 실행은 저장소 루트(minishop/)에서 합니다. 경로 설정은 pyproject.toml이 처리합니다.

<br>

## 본문 예제와 파일 대응

- src/minishop/models.py: 예제 9.1 (데이터 모델)
- examples/before_contract/coupons_a.py: 예제 9.2 (계약 도입 전 쿠폰)
- examples/before_contract/refunds_b.py: 예제 9.3 (계약 도입 전 환불)
- examples/before_contract/reproduce_failure.py: 예제 9.4 (결합 실패 재현)
- specs/pricing-contract.md: 예제 9.5 (금액 계산 인터페이스 계약)
- src/minishop/pricing.py: 예제 9.6 (계약의 구현)
- src/minishop/coupons.py·refunds.py: 예제 9.7 (계약 적용 후)
- CODEOWNERS: 예제 9.8 (파일 오너십)
- CLAUDE.md: 예제 9.9 (작업 경계)
- scripts/check_imports.py: 예제 9.10 (의존성 방향 검사)
- .github/pull_request_template.md: 예제 9.11 (가정을 드러내는 PR 템플릿)
- .github/workflows/ci.yml: 예제 9.12 (병합 게이트)
- tests/test_pricing_contract.py: 예제 9.13 (계약 테스트, 9.3.3)
- .claude/settings.json: 예제 9.14 (계약 파일 수정 시 자동 검사 훅)
- scripts/hooks/run_contract_tests.py: 예제 9.14의 훅이 실행하는 스크립트

<br>

## 실행 순서

```bash
# 1) 결합 실패 재현 (9.1.1): 회사 손실 1,200원이 출력되면 재현 성공
python examples/before_contract/reproduce_failure.py

# 2) 계약 적용 후 전체 테스트 (9.2~9.3)
python -m pytest tests/ -v

# 3) 의존성 방향 검사 (9.3.2)
python scripts/check_imports.py
```

<br>

## 게이트 실습 (9.3.3)

- GitHub에 저장소를 올리고 ci.yml 워크플로와 브랜치 룰셋(잡 이름
  contract-and-tests를 필수 검사로 지정)을 구성하면 그림 9.6~9.8의
  병합 잠금을 재현할 수 있습니다. 무료 개인 계정의 프라이빗 저장소에서는
  룰셋이 강제되지 않으므로 공개 저장소를 권장합니다.
