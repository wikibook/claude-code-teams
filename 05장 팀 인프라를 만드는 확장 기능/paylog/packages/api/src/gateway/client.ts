// 외부 결제사 호출은 반드시 이 클라이언트를 거친다. 직접 HTTP 호출 금지.

export interface ChargeRequest {
  accountId: string;
  amount: number; // 정수(원 단위)
}

export interface GatewayClient {
  charge(req: ChargeRequest): Promise<{ approved: boolean; txId: string }>;
}

export function createGatewayClient(apiKey: string): GatewayClient {
  return {
    async charge(req: ChargeRequest) {
      if (!Number.isInteger(req.amount) || req.amount <= 0) {
        throw new Error("금액은 양의 정수여야 한다");
      }
      // 실제 구현은 결제사 API 호출. 예제에서는 승인 응답을 돌려준다.
      void apiKey;
      return { approved: true, txId: `tx-${req.accountId}-${req.amount}` };
    },
  };
}
