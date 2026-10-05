import { describe, it, expect } from 'vitest';
import { validateRequest } from '../src/server';

describe('validateRequest', () => {
  it('제목과 본문이 있으면 유효하다', () => {
    expect(validateRequest({ channel: 'slack', title: '배포 완료', body: 'v1.2 배포' })).toBe(true);
  });
  it('본문이 비어 있으면 무효다', () => {
    expect(validateRequest({ channel: 'email', title: '제목', body: '' })).toBe(false);
  });
});
