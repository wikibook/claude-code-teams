// 테스트는 실제 결제사 샌드박스 대신 이 모의 객체를 쓴다.
import type { GatewayClient } from "../../src/gateway/client";

export function createMockGateway(approved = true): GatewayClient {
  return {
    async charge(req) {
      return { approved, txId: `mock-${req.accountId}` };
    },
  };
}
