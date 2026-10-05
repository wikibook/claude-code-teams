import re
import sys
import json

# 입출력을 UTF-8로 고정한다. 콘솔 인코딩이 다른 환경과 BOM이 붙은 입력에도 동일하게 동작한다.
sys.stdout.reconfigure(encoding="utf-8")
event = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
command = event.get("tool_input", {}).get("command", "")

# git commit이 아니면 통과시킨다
if not re.search(r"git\s+commit\b", command):
    sys.exit(0)

# 스테이징된 파일 목록에서 계약 인접 코드와 계약 문서의 변경 여부를 확인한다
import subprocess
staged = subprocess.run(["git", "diff", "--cached", "--name-only"],
                        capture_output=True, encoding="utf-8").stdout.splitlines()
code_touched = any(re.match(r"src/minishop/(pricing|points|refunds|dispatch)", f)
                   for f in staged)
spec_touched = any(f.startswith("specs/") for f in staged)

if code_touched and not spec_touched:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                "계약 인접 코드가 변경되었지만 specs/ 문서는 변경되지 않았다. "
                "계약·문서의 갱신이 필요 없는 변경인지 확인할 것."),
        }
    }, ensure_ascii=False))

sys.exit(0)
