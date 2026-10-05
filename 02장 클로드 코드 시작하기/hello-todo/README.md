# hello-todo

2장 첫 세션 실습용 예제. 브라우저에서 동작하는 간단한 할 일 목록 웹 애플리케이션이다.

## 구성

- `index.html` — 화면. 브라우저로 열면 바로 동작한다.
- `todo.js` — 할 일 목록의 상태와 조작 로직. 브라우저와 Node 양쪽에서 쓰인다.
- `todo.test.js` — 로직 테스트.

## 실행

```
index.html을 브라우저로 연다   # 앱 실행
node --test                  # 테스트 실행 (Node.js 22 이상)
```

## 동작

- 할 일 데이터는 브라우저의 localStorage에 저장된다.
- 로직은 목록을 입력받아 새 목록을 반환하는 순수 함수(addTodo, toggleDone, visibleTodos)로 구성된다.
