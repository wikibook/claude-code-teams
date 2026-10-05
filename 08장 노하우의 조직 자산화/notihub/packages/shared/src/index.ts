// 알림 채널과 템플릿 렌더링의 공용 타입·유틸리티
export type Channel = 'slack' | 'email' | 'webhook';

export interface Notification {
  channel: Channel;
  title: string;
  body: string;
}

// 템플릿의 {{키}} 자리를 값으로 치환한다.
export function renderTemplate(template: string, values: Record<string, string>): string {
  return template.replace(/\{\{(\w+)\}\}/g, (_, key: string) => values[key] ?? '');
}
