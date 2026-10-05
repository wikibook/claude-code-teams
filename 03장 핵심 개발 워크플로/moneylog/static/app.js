// moneylog 화면 로직
const CATEGORIES = ["식비", "교통", "주거", "여가", "기타"];

const monthInput = document.getElementById("month-input");
const totalAmount = document.getElementById("total-amount");
const categoryTotals = document.getElementById("category-totals");
const expenseList = document.getElementById("expense-list");
const form = document.getElementById("expense-form");
const formError = document.getElementById("form-error");

// 카테고리 선택지를 채운다
const categoryInput = document.getElementById("category-input");
CATEGORIES.forEach(function (name) {
  const option = document.createElement("option");
  option.value = name;
  option.textContent = name;
  categoryInput.appendChild(option);
});

function currentMonth() {
  return monthInput.value;
}

// 요약과 목록을 서버에서 다시 불러와 그린다
async function refresh() {
  const month = currentMonth();
  const [summaryRes, listRes] = await Promise.all([
    fetch("/api/summary?month=" + month),
    fetch("/api/expenses?month=" + month),
  ]);
  const summary = await summaryRes.json();
  const expenses = await listRes.json();

  totalAmount.textContent = summary.total.toLocaleString();
  categoryTotals.innerHTML = "";
  Object.entries(summary.by_category).forEach(function ([name, value]) {
    const li = document.createElement("li");
    li.textContent = name + " " + value.toLocaleString() + "원";
    categoryTotals.appendChild(li);
  });

  expenseList.innerHTML = "";
  expenses.forEach(function (e) {
    const li = document.createElement("li");
    li.className = e.amount < 0 ? "expense refund" : "expense";
    li.textContent =
      e.date + " · " + e.category + " · " + e.amount.toLocaleString() + "원" +
      (e.memo ? " · " + e.memo : "");
    expenseList.appendChild(li);
  });
}

// 지출 등록
form.addEventListener("submit", async function (event) {
  event.preventDefault();
  formError.textContent = "";
  const res = await fetch("/api/expenses", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      date: document.getElementById("date-input").value,
      category: categoryInput.value,
      amount: parseInt(document.getElementById("amount-input").value, 10),
      memo: document.getElementById("memo-input").value,
    }),
  });
  if (res.status !== 201) {
    const body = await res.json();
    formError.textContent = body.errors.join(", ");
    return;
  }
  form.reset();
  await refresh();
});

// 초기 상태: 이번 달로 설정하고 불러온다
monthInput.value = new Date().toISOString().slice(0, 7);
monthInput.addEventListener("change", refresh);
refresh();
