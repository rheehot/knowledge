const sum = require("./sum");

describe("테스트 그룹", () => {
  test("1과 2를 더하면 3이다", () => {
    expect(sum(1, 2)).toBe(3);
  });
  test("1과 -3을 더하면 -2이다", () => {
    expect(sum(1, -3)).toBe(-2);
  });
  test("-3과 -10을 더하면 -13이다.", () => {
    expect(sum(-3, -10)).toBe(-13);
  });
  test("하나는 숫자가 아닙니다.", () => {
    expect(sum("하나", 2)).toBe("숫자가 아닙니다.");
  });
  test("둘은 숫자가 아닙니다.", () => {
    expect(sum(1, "둘")).toBe("숫자가 아닙니다.");
  });
  test("하나와 둘은 숫자가 아닙니다.", () => {
    expect(sum("하나", "둘")).toBe("숫자가 아닙니다.");
  });
});
