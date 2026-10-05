import anyio
from claude_agent_sdk import query, ClaudeAgentOptions

SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "problems": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["ok", "problems"],
}

async def lint(template_text: str) -> dict:
    """알림 템플릿 하나를 검수해 판정과 문제 목록을 반환한다."""
    options = ClaudeAgentOptions(
        setting_sources=[],           # 파일 설정을 로드하지 않는다
        tools=[],                     # 도구 없이 텍스트 판정만 수행한다
        max_turns=3,
        output_format={"type": "json_schema", "schema": SCHEMA},
    )
    prompt = ("다음 알림 템플릿이 문구 지침을 지키는지 검수하라. "
              "지침: 수신 거부 안내 포함, 과장 표현 금지, 변수 자리표시자 형식 준수.\n\n"
              + template_text)
    result = None
    async for message in query(prompt=prompt, options=options):
        if type(message).__name__ == "ResultMessage":
            result = message.structured_output
    return result

if __name__ == "__main__":
    import sys
    text = open(sys.argv[1], encoding="utf-8").read()
    print(anyio.run(lint, text))
