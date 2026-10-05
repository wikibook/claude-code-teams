import re
import sys
import json
import subprocess

# stdin을 UTF-8로 명시해 읽는다. 로캘 기본 인코딩에서는 한글이 깨질 수 있다
event = json.loads(sys.stdin.buffer.read().decode("utf-8"))
command = event.get("tool_input", {}).get("command", "")

# git commit이 아니면 통과시킨다
if not re.search(r"git\s+commit\b", command):
    sys.exit(0)

# 빠른 검사만 커밋 전에 수행한다 (전 패키지 타입 검사, 약 10초)
check = subprocess.run(["pnpm", "-r", "check"], capture_output=True, text=True)
if check.returncode != 0:
    message = ("정책: 커밋 전 검사가 실패했다. 아래 출력을 확인해 수정한 뒤 "
               "다시 커밋할 것.\n" + check.stdout[-2000:])
    sys.stderr.buffer.write(message.encode("utf-8"))
    sys.exit(2)

sys.exit(0)
