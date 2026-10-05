#!/bin/sh
# 워크트리에서 한 번 실행해 개발 환경을 준비한다
set -eu

cd "$(git rev-parse --show-toplevel)"

python -m venv .venv
BIN=.venv/bin
[ -d .venv/Scripts ] && BIN=.venv/Scripts

"$BIN/python" -m pip install --quiet pytest

# 환경이 실제로 동작하는지 계약 테스트로 확인한다
"$BIN/python" -m pytest tests/test_pricing_contract.py -q

echo "준비 완료: $(pwd)"
