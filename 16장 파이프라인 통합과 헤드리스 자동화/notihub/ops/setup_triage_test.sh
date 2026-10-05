#!/bin/sh
# 예제 16.6 — 이슈 분류 파이프라인의 시험 준비
# 분류에 사용할 라벨을 만들고, 분류 대상 이슈를 하나 생성한다.
# 사전 조건: gh 인증 완료, 저장소 Settings > Actions > General의
#            Workflow permissions가 Read and write permissions로 지정되어 있어야 한다.

for label in area/channel area/template area/scheduler area/api area/console \
             type/bug type/feature type/question type/ops \
             p0 p1 p2 p3 needs-info; do
  gh label create "$label"
done

gh issue create --title "예약 알림이 같은 사용자에게 두 번 발송됩니다" --body "어제 오후 3시 예약
발송에서 일부 사용자가 동일한 푸시 알림을 두 번 받았습니다.
- 발생 시각: 8/29 15:00 예약 발송
- 채널: 푸시
- 재현: 재시도가 일어난 건에서만 확인됨
- 영향: 약 40건"
