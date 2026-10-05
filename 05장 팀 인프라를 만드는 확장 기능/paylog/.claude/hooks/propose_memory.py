import json
import sys

# stdin을 UTF-8로 명시해 읽는다.
event = json.loads(sys.stdin.buffer.read().decode("utf-8"))

# 이 훅의 지시로 응답이 이미 한 번 이어졌다면 그대로 통과시킨다 (무한 반복 방지)
if event.get("stop_hook_active"):
    sys.exit(0)

# 사용자가 방향을 교정한 세션에서만 제안하도록,
# 마지막 응답에 수정·재작업의 흔적이 있는지 확인한다
last = event.get("last_assistant_message", "")
signals = ["수정", "정정", "고쳤", "바꿨", "변경",
           "제거", "다시 작성", "되돌", "롤백"]
if not any(word in last for word in signals):
    sys.exit(0)

# stdout도 UTF-8로 직접 써서 로캘에 좌우되지 않게 한다
sys.stdout.buffer.write(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "Stop",
        "additionalContext": (
            "세션을 마치기 전에 확인할 것: 이번 세션에서 사용자가 교정한 "
            "지시나 반복된 실수 중 CLAUDE.md에 규칙으로 남길 것이 있으면 "
            "구체적 문안을 제안하고, 없으면 없다고 답한다."
        )
    }
}, ensure_ascii=False).encode("utf-8"))
sys.exit(0)
