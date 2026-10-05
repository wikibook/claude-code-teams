#!/bin/sh
# 주간 리포트 본문을 읽어 한 줄 논평을 생성한다
python ops/weekly_cost_report.py "$1" "$2" | claude -p --bare \
  "다음 주간 비용 리포트에서 팀 리더가 주목할 변화 한 가지를 한 문장으로 요약하라." \
  --output-format json \
  --json-schema '{"type":"object","properties":{"comment":{"type":"string"}},"required":["comment"]}' \
  --max-turns 3 --max-budget-usd 0.50 \
  | python -c "import sys,json; print(json.load(sys.stdin)['structured_output']['comment'])"
