// 관리 콘솔의 발송 상태 표기(실습용 최소 골격)
export type DeliveryState = 'queued' | 'sent' | 'failed';

export function stateLabel(state: DeliveryState): string {
  if (state === 'queued') return '대기';
  if (state === 'sent') return '발송됨';
  return '실패';
}
