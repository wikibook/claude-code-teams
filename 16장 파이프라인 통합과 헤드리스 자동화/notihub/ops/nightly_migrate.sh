#!/bin/sh
# targets.txt의 템플릿을 순회하며 한 파일씩 이관한다
FAIL_STREAK=0
while read -r file; do
  grep -qx "$file" done.txt 2>/dev/null && continue   # 완료분 재실행 방지
  result=$(claude -p --bare \
    "templates/$file 을 v2 알림 형식으로 변환하라. 스키마 검사와 렌더링
     테스트를 실행해 통과를 확인하고, 결과를 요약한 뒤 마지막 줄에 OK 또는 FAIL만 출력하라." \
    --allowedTools "Read,Edit,Bash(npm run lint:template:*),Bash(npm test:*)" \
    --output-format json --max-turns 10 --max-budget-usd 1.00 </dev/null)
  if [ "$(printf '%s\n' "$result" | jq -r '.is_error')" = "false" ] && \
     printf '%s\n' "$result" | jq -r '.result' | tail -n 1 | grep -qx "OK"; then
    echo "$file" >> done.txt
    FAIL_STREAK=0
  else
    printf '%s %s\n' "$file" "$(printf '%s\n' "$result" | jq -r '.result' | tr '\n' ' ' | head -c 100)" >> failed.txt
    FAIL_STREAK=$((FAIL_STREAK + 1))
    [ "$FAIL_STREAK" -ge 3 ] && { echo "연속 실패로 중단"; exit 1; }
  fi
done < targets.txt
