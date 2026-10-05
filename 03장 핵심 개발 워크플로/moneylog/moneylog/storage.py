# JSON 파일 저장소
import json
import shutil
from pathlib import Path

from . import models

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "expenses.json"
SAMPLE_FILE = BASE_DIR / "data" / "sample_expenses.json"


class Storage:
    """지출 목록을 JSON 파일 하나에 저장한다."""

    def __init__(self, path=DATA_FILE):
        self.path = Path(path)

    def _ensure_file(self):
        # 기본 데이터 파일이 없으면 샘플 데이터를 복사해 시작한다
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            if self.path == DATA_FILE and SAMPLE_FILE.exists():
                shutil.copy(SAMPLE_FILE, self.path)
            else:
                self.path.write_text("[]", encoding="utf-8")

    def load(self):
        """저장된 지출 전체를 Expense 목록으로 돌려준다."""
        self._ensure_file()
        rows = json.loads(self.path.read_text(encoding="utf-8"))
        return [models.from_dict(row) for row in rows]

    def save(self, expenses):
        """Expense 목록 전체를 파일에 덮어쓴다."""
        self._ensure_file()
        rows = [e.to_dict() for e in expenses]
        self.path.write_text(
            json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def next_id(self):
        """새 지출에 부여할 id를 돌려준다."""
        expenses = self.load()
        if not expenses:
            return 1
        return max(e.id for e in expenses) + 1
