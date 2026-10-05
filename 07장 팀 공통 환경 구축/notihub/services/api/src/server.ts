// 알림 API와 발송 파이프라인의 진입점(실습용 최소 골격)
export interface DispatchRequest {
  channel: 'slack' | 'email' | 'webhook';
  title: string;
  body: string;
}

// 발송 규칙(재시도·중복 제거)은 specs/delivery-contract.md를 따른다.
export function validateRequest(req: DispatchRequest): boolean {
  return req.title.length > 0 && req.body.length > 0;
}
