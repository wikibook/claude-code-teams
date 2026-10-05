// v2 템플릿의 렌더링을 검사한다. templates/의 v2 템플릿을 모두 확인한다.
const fs = require('fs');
const SAMPLE = {
  user_name: '홍길동', order_id: 'A-1024', eta_date: '8월 31일',
  amount: '25,000원', reset_url: 'https://example.com/reset',
  unsubscribe_url: 'https://example.com/optout',
};
let failed = 0, checked = 0;
for (const f of fs.readdirSync('templates')) {
  if (!f.endsWith('.json')) continue;
  const t = JSON.parse(fs.readFileSync(`templates/${f}`, 'utf8'));
  if (t.version !== 2) continue;              // 아직 이관하지 않은 템플릿은 건너뛴다
  checked++;
  const render = s => String(s).replace(/\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}/g,
    (_, k) => (k in SAMPLE ? SAMPLE[k] : `<<미정의:${k}>>`));
  const out = `${render(t.title)}\n${render(t.body)}\n${render(t.optOut.text)} ${render(t.optOut.url)}`;
  if (out.includes('<<미정의:')) {
    console.error(`FAIL ${f}: 값을 채울 수 없는 변수가 있다\n${out}`); failed++;
  } else if (/[{}$]/.test(out)) {
    console.error(`FAIL ${f}: 치환되지 않은 자리표시자가 남았다\n${out}`); failed++;
  } else {
    console.log(`OK ${f}`);
  }
}
console.log(`검사한 v2 템플릿 ${checked}개, 실패 ${failed}개`);
process.exit(failed ? 1 : 0);
