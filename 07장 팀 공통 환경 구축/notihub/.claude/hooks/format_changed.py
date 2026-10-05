import json
import subprocess
import sys

# stdin을 UTF-8로 명시해 읽는다. 로캘 기본 인코딩에서는 한글이 깨질 수 있다
event = json.loads(sys.stdin.buffer.read().decode("utf-8"))
path = event.get("tool_input", {}).get("file_path", "")

# 포맷 대상 확장자만 처리하고, 나머지는 그대로 통과시킨다
if not path.endswith((".ts", ".tsx", ".js", ".json")):
    sys.exit(0)

# 수정된 파일 하나만 포맷한다. 실패해도 세션을 막지 않는다
subprocess.run(["pnpm", "exec", "prettier", "--write", path],
               capture_output=True)
sys.exit(0)
