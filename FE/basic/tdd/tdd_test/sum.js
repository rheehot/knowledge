function sum(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    return "숫자가 아닙니다.";
  }
  return a + b;
}

module.exports = sum;
