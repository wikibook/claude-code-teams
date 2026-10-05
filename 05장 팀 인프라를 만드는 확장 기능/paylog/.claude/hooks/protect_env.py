import json
import sys

# stdin을 UTF-8로 명시해 읽는다.
event = json.loads(sys.stdin.buffer.read().decode("utf-8"))
path = event.get("tool_input", {}).get("file_path", "")

# .env 계열 파일의 수정 시도를 차단한다 (.env.example은 허용)
name = path.replace("\\", "/").split("/")[-1]
if name.startswith(".env") and name != ".env.example":
    sys.stderr.buffer.write(
        "정책: .env 파일은 에이전트가 수정할 수 없다. "
        "필요한 변경을 사용자에게 요청할 것.".encode("utf-8"))
    sys.exit(2)

sys.exit(0)
