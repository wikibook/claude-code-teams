// 잔액 계산 — 감사 대상 코드다. 수정 전에 계획을 세워 승인받아야 한다.

export interface Entry {
  id: number;
  accountId: string;
  // 금액은 항상 정수(원 단위)다. 환불은 음수로 기록한다.
  amount: number;
  memo: string;
}

export function recordCharge(entries: Entry[], entry: Entry): Entry[] {
  if (!Number.isInteger(entry.amount)) {
    throw new Error("금액은 정수(원 단위)여야 한다");
  }
  if (entries.some((e) => e.id === entry.id)) {
    throw new Error("이미 기록된 항목이다");
  }
  return [...entries, entry];
}

export function balanceOf(entries: Entry[], accountId: string): number {
  return entries
    .filter((e) => e.accountId === accountId)
    .reduce((sum, e) => sum + e.amount, 0);
}
