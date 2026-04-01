const test1 = "test";
const test2 = null;

const result1 = test1 ?? null; // ?? 연산자는 왼쪽 피연산자가 null 또는 undefined인 경우에만 오른쪽 피연산자를 반환합니다. 그렇지 않으면 왼쪽 피연산자를 반환합니다.
const result2 = test2 ?? "뒤에꺼";

console.log(result1);
console.log(result2);   