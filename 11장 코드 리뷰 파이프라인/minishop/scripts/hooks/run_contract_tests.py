"""에이전트가 pricing.py를 수정하면 계약 테스트를 실행하는 훅 (9.3.3).

클로드 코드는 PostToolUse 훅에 도구 호출 정보를 JSON으로 전달한다.
수정된 파일이 계약의 구현(pricing.py)일 때만 계약 테스트를 돌리고,
실패하면 종료 코드 2로 세션에 실패 내용을 되먹인다.
"""
import json
import subprocess
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path.endswith("src/minishop/pricing.py"):
        return 0   # 계약 구현이 아니면 통과

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_pricing_contract.py", "-q"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        # 종료 코드 2: 실패 출력을 세션의 컨텍스트로 되돌려 보낸다
        print(result.stdout + result.stderr, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
