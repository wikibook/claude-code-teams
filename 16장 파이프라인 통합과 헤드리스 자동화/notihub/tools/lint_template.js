// v2 알림 템플릿의 스키마를 검사한다. 사용법: node tools/lint_template.js <파일>
const fs = require('fs');
const path = process.argv[2];
if (!path) { console.error('사용법: npm run lint:template <파일 경로>'); process.exit(2); }

const problems = [];
let t;
try { t = JSON.parse(fs.readFileSync(path, 'utf8')); }
catch (e) { console.error(`JSON 파싱 실패: ${e.message}`); process.exit(1); }

if (t.version !== 2) problems.push('version 필드가 숫자 2가 아니다');
if (!['push', 'email', 'sms'].includes(t.channel)) problems.push('channel은 push, email, sms 중 하나여야 한다');
if (typeof t.title !== 'string') problems.push('title 문자열이 없다');
if (typeof t.body !== 'string') problems.push('body 문자열이 없다');
if (!Array.isArray(t.variables)) problems.push('variables 배열이 없다');
if (!t.optOut || typeof t.optOut.text !== 'string' || typeof t.optOut.url !== 'string') {
  problems.push('optOut 객체에 text와 url이 필요하다');
}
if ('vars' in t) problems.push('v1의 vars 필드가 남아 있다. variables로 바꿔야 한다');

const text = `${t.title || ''} ${t.body || ''}`;
const dollar = text.match(/\$[A-Za-z_][A-Za-z0-9_]*/g);
if (dollar) problems.push(`v1 자리표시자가 남아 있다: ${dollar.join(', ')} — {{변수명}} 형식으로 바꿔야 한다`);
const used = [...text.matchAll(/\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}/g)].map(m => m[1]);
if (Array.isArray(t.variables)) {
  for (const v of used) if (!t.variables.includes(v)) problems.push(`본문에 쓴 ${v}가 variables에 없다`);
  for (const v of t.variables) if (!used.includes(v)) problems.push(`variables의 ${v}가 본문에 쓰이지 않았다`);
}

if (problems.length) {
  console.error(`FAIL ${path}\n형식 규칙은 templates/SPEC-v2.md 참고`);
  problems.forEach(p => console.error(` - ${p}`));
  process.exit(1);
}
console.log(`OK ${path}`);
