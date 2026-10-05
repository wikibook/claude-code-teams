# HTTP 서버와 라우팅
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from . import api
from .storage import Storage

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


class MoneylogHandler(SimpleHTTPRequestHandler):
    """/api/*는 API로 처리하고 나머지는 static/의 파일을 돌려준다."""

    storage = Storage()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def _send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _query(self):
        raw = parse_qs(urlparse(self.path).query)
        return {k: v[0] for k, v in raw.items()}

    def do_GET(self):
        route = urlparse(self.path).path
        if route == "/api/expenses":
            self._send_json(*api.handle_get_expenses(self.storage, self._query()))
        elif route == "/api/summary":
            self._send_json(*api.handle_get_summary(self.storage, self._query()))
        else:
            # 정적 파일(index.html, app.js 등)은 기본 핸들러에 맡긴다
            super().do_GET()

    def do_POST(self):
        route = urlparse(self.path).path
        if route == "/api/expenses":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            self._send_json(*api.handle_post_expense(self.storage, body))
        else:
            self.send_error(404)


def run(port=8000):
    server = HTTPServer(("localhost", port), MoneylogHandler)
    print(f"moneylog 서버 실행 중: http://localhost:{port}")
    server.serve_forever()
