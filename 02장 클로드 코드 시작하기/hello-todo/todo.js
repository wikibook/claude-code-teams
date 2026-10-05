// hello-todo: 할 일 목록의 상태와 조작. 브라우저와 Node 양쪽에서 쓰인다.

// 할 일을 하나 추가한 새 목록을 돌려준다.
function addTodo(todos, text) {
  return [...todos, { text: text, done: false }];
}

// 지정한 번호(0부터)의 완료 상태를 뒤집은 새 목록을 돌려준다.
function toggleDone(todos, index) {
  return todos.map(function (todo, i) {
    if (i === index) {
      return { text: todo.text, done: !todo.done };
    }
    return todo;
  });
}

// 화면에 보여줄 목록을 돌려준다. hideDone이 참이면 완료 항목을 숨긴다.
function visibleTodos(todos, hideDone) {
  if (!hideDone) {
    return todos;
  }
  return todos.filter(function (todo) {
    return !todo.done;
  });
}

// Node(테스트)에서 불러 쓸 수 있게 내보낸다. 브라우저에서는 무시된다.
if (typeof module !== "undefined") {
  module.exports = { addTodo: addTodo, toggleDone: toggleDone, visibleTodos: visibleTodos };
}
