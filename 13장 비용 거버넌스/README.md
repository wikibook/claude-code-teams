# 13장 실습 안내: notihub (비용 거버넌스)

13장의 예제 저장소입니다. notihub 조직의 비용 거버넌스 운영 파일만 담은
부분 스냅샷입니다(서비스 코드는 「07장」·「08장」 폴더의 notihub를 참조하세요).

<br>

## 본문 예제와 파일 대응

- ops/managed-settings.json: 예제 13.1 (텔레메트리 배포용 관리 설정)
- ops/weekly_cost_report.py: 예제 13.2 (주간 비용 리포트 생성기, 지면은 발췌)
- ops/member_team.json: 구성원과 팀의 매핑 표 (13.2.2)
- spend_this_week.csv, spend_last_week.csv: 지출 보고서 형식의 샘플 데이터

<br>

## 실행 (예제 13.3)

```bash
python ops/weekly_cost_report.py spend_this_week.csv spend_last_week.csv
```

출력은 본문 13.3.2의 "출력 결과"와 문자 단위로 일치합니다(급증 표시,
미배정 항목 포함). CSV 컬럼(email, total_net_spend_usd)은 지출 보고서
내보내기 형식을 따른 샘플이며, 실제 내보내기 파일의 리터럴 헤더는
운영 환경에서 확인하세요.
