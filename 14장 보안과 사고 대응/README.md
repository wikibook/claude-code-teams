# 14장 실습 안내: notihub (보안과 사고 대응)

14장의 예제 저장소입니다. notihub 조직의 보안 운영 파일만 담은 부분 스냅샷입니다
(서비스 코드는 「07장」·「08장」 폴더의 notihub를 참조하세요).

<br>

## 본문 예제와 파일 대응

- payments-api/.claude/settings.json: 예제 14.1 (규제 등급 권한 프로파일)
  + 예제 14.2 (샌드박스 설정 발췌). 두 예제는 같은 파일의 발췌입니다.
- ops/managed-settings.d/10-security.json: 예제 14.4 (조직 공통 보안 정책)
- ops/managed-settings.d/20-supply-chain.json: 예제 14.3 (MCP·마켓플레이스 허용 목록)
- ops/managed-settings.d/30-audit.json: 예제 14.5 (감사 이벤트 송출)

<br>

## 실습 참고

- managed-settings.d의 파일은 조직 관리 설정의 드롭인 예시입니다. 실제 배포는
  운영체제별 시스템 디렉터리에 놓습니다(본문 14.3.1, 표 7.4의 경로).
- payments-api 프로파일을 체험하려면 해당 디렉터리에서 세션을 열고
  `.env` 읽기나 `aws` 명령을 지시해 deny 동작을 확인합니다. 샌드박스는
  macOS·리눅스·WSL2에서만 동작합니다(14.1.2).
- 우회 모드 차단(disableBypassPermissionsMode)은 관리 설정으로 배포됐을
  때만 강제됩니다. 드롭인 파일을 시스템 경로에 두고 확인하세요.
