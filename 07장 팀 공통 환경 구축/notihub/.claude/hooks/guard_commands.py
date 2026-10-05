import re
import sys
import json

# stdin을 UTF-8로 명시해 읽는다. 로캘 기본 인코딩에서는 한글이 깨질 수 있다
event = json.loads(sys.stdin.buffer.read().decode("utf-8"))
command = event.get("tool_input", {}).get("command", "")


def block(reason):
    # 종료 코드 2가 차단이다. stderr의 메시지는 에이전트에게 전달된다
    sys.stderr.buffer.write(reason.encode("utf-8"))
    sys.exit(2)


# 1. 보호 브랜치를 향한 강제 푸시 차단 (--force, -f, --force-with-lease)
if re.search(r"git\s+push\b", command) and re.search(r"(--force|-f)\b", command):
    if re.search(r"\b(main|release/\S+)\b", command):
        block("정책: main과 release 브랜치에는 강제 푸시할 수 없다. "
              "이력 수정이 필요하면 새 브랜치에서 PR로 진행할 것.")

# 2. 운영 발송 채널 호출 차단 (채널 주소 기준)
if re.search(r"(notify\.internal|hooks\.slack\.com)", command):
    block("정책: 운영 발송 채널은 호출할 수 없다. "
          "테스트는 샌드박스 채널(notify-sandbox.internal)을 사용할 것.")

sys.exit(0)
