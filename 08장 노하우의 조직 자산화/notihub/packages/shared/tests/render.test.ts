import { describe, it, expect } from 'vitest';
import { renderTemplate } from '../src/index';

describe('renderTemplate', () => {
  it('자리 표시자를 값으로 치환한다', () => {
    expect(renderTemplate('안녕하세요 {{name}}님', { name: '민수' })).toBe('안녕하세요 민수님');
  });
  it('값이 없는 키는 빈 문자열로 치환한다', () => {
    expect(renderTemplate('{{missing}}', {})).toBe('');
  });
});
