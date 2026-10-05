// 새 API는 GraphQL로 작성한다.

export const typeDefs = /* GraphQL */ `
  type Query {
    balance(accountId: ID!): Int!
  }
`;
