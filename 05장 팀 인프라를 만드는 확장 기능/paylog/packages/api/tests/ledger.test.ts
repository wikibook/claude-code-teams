import { describe, expect, it } from "vitest";
import { balanceOf, recordCharge, type Entry } from "../src/models/ledger";
import { createMockGateway } from "./mocks/gateway";

const base: Entry[] = [
  { id: 1, accountId: "a1", amount: 10000, memo: "충전" },
  { id: 2, accountId: "a1", amount: -3000, memo: "환불" },
  { id: 3, accountId: "a2", amount: 500, memo: "수수료" },
];

describe("ledger", () => {
  it("잔액은 부호를 살려 합산한다", () => {
    expect(balanceOf(base, "a1")).toBe(7000);
  });

  it("정수가 아닌 금액은 거부한다", () => {
    expect(() =>
      recordCharge(base, { id: 4, accountId: "a1", amount: 10.5, memo: "" })
    ).toThrow();
  });

  it("같은 id를 두 번 기록할 수 없다", () => {
    expect(() =>
      recordCharge(base, { id: 1, accountId: "a1", amount: 100, memo: "" })
    ).toThrow();
  });
});

describe("gateway mock", () => {
  it("모의 결제는 승인 응답을 돌려준다", async () => {
    const gw = createMockGateway();
    const res = await gw.charge({ accountId: "a1", amount: 1000 });
    expect(res.approved).toBe(true);
  });
});
