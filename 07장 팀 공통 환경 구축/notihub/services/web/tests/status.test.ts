import { describe, it, expect } from 'vitest';
import { stateLabel } from '../src/status';

describe('stateLabel', () => {
  it('상태를 한글 라벨로 바꾼다', () => {
    expect(stateLabel('sent')).toBe('발송됨');
  });
});
