// hello-todo 로직 테스트. 실행: node --test
const test = require("node:test");
const assert = require("node:assert");
const { addTodo, toggleDone, visibleTodos } = require("./todo.js");

test("추가하면 목록 끝에 미완료 항목이 생긴다", function () {
  const todos = addTodo([], "우유 사기");
  assert.strictEqual(todos.length, 1);
  assert.strictEqual(todos[0].text, "우유 사기");
  assert.strictEqual(todos[0].done, false);
});

test("완료 처리하면 done이 참이 된다", function () {
  const todos = toggleDone(addTodo([], "우유 사기"), 0);
  assert.strictEqual(todos[0].done, true);
});

test("숨기기가 켜지면 완료 항목이 목록에서 빠진다", function () {
  const todos = toggleDone(addTodo(addTodo([], "우유 사기"), "책 반납"), 0);
  const visible = visibleTodos(todos, true);
  assert.strictEqual(visible.length, 1);
  assert.strictEqual(visible[0].text, "책 반납");
});
