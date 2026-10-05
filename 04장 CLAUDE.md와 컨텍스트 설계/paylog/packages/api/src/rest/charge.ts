// src/rest/는 동결 상태다. 버그 수정 외 변경 금지.

export interface RestResult {
  status: number;
  body: unknown;
}

export function handleCharge(rawAmount: unknown): RestResult {
  const amount = Number(rawAmount);
  if (!Number.isInteger(amount) || amount <= 0) {
    return { status: 400, body: { errors: ["금액은 양의 정수여야 한다"] } };
  }
  return { status: 200, body: { charged: amount } };
}
