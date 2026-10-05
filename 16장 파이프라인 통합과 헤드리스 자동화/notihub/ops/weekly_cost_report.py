"""주간 비용 리포트 생성기.

지출 보고서 CSV 두 주치를 읽어 팀별 요약을 만들고 표준 출력으로 내보낸다.
게시는 CI에서 이 출력을 슬랙 웹훅으로 전달하는 단계가 담당한다.

사용법: python ops/weekly_cost_report.py <이번 주 CSV> <지난주 CSV>
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import date, timedelta

ALERT_RATIO = 1.5   # 전주 대비 급증 판정 배수

def load_team_map(path="ops/member_team.json"):
    """구성원 이메일과 팀의 매핑 표를 읽는다. 모든 원천에 같은 키를 쓴다."""
    return json.load(open(path, encoding="utf-8"))

def load_spend(path, member_team):
    """지출 보고서 CSV를 팀별 지출로 합산한다."""
    spend = defaultdict(float)
    for row in csv.DictReader(open(path, encoding="utf-8")):
        team = member_team.get(row["email"], "(미배정)")
        spend[team] += float(row["total_net_spend_usd"])
    return spend

def check_freshness(path):
    """원천 데이터의 날짜가 기대 범위를 벗어나면 게시 대신 오류를 낸다."""
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    if not rows:
        raise SystemExit("오류: 지출 보고서가 비어 있다")
    dates = {r["date"] for r in rows if r.get("date")}
    if dates and max(dates) < str(date.today() - timedelta(days=9)):
        raise SystemExit("오류: 지출 보고서의 날짜가 기대 범위를 벗어났다")

def build_report(this_week, last_week):
    lines = ["주간 비용 리포트"]
    for team, amount in sorted(this_week.items(), key=lambda x: -x[1]):
        prev = last_week.get(team, 0.0)
        surge = prev > 0 and amount > prev * ALERT_RATIO
        mark = " [전주 대비 급증]" if surge else ""
        lines.append(f"- {team}: {amount:,.0f}달러 (전주 {prev:,.0f}달러){mark}")
    return "\n".join(lines)

if __name__ == "__main__":
    member_team = load_team_map()
    check_freshness(sys.argv[1])
    report = build_report(load_spend(sys.argv[1], member_team),
                          load_spend(sys.argv[2], member_team))
    print(report)
