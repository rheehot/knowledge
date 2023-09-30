## TDD란?

![tdd](https://velog.velcdn.com/images/cnffjd95/post/77666161-42ec-43cc-b46c-e799118c89dc/image.png)
`Test Driven Develpment`의 약자로써 **테스트 주도 개발**이라는 뜻을 가진다.
짧은 개발 사이클을 반복하는 프로세스로, 테스트로 하여금 전체적인 개발을 주도하게끔하는 방법론 중 하나이다.
기존에 사용하던 개발방법은 **(설계 ➡️ 개발 ➡️ 테스트) ➡️ 수정 ➡️ 반복**의 순서를 따랐다면, TDD는 **(설계 ➡️ 수정 ➡️ 테스트) ➡️ 반복 ➡️ 개발**의 순서를 가진다.

기존에 사용하던 개발방법의 단점으로는 요구사항이 처음부터 명확하지 않을수 있기 떄문에 최초에 완벽한 설계가 어렵다. 이로 인해 개발자가 코드를 재설계(코드를 수정, 삭제, 삽입)하는 과정에서 불필요한 코드가 남겨지거나 중복되는 코드가 생길 가능성이 높다. 또한 작은 기능 수정에도 전체적인 부분을 테스트해야 하므로 버그 검출이 힘들어지고, 어디서 버그가 발생할지 모르므로 전체적인 소스코드의 품질이 저하된다. 최종적으로 재사용이 어렵고, 유지보수가 힘들어지고 테스트 비용이 높아지는 결과를 낳는다.

TDD의 경우, 기존의 개발방식과 큰 차이점이 **테스트 코드를 작성 후 실제 코드를 작성 한다는 점이다.**
테스트 코드를 작성하며 생기는 버그 또는 수정사항을 테스트 케이스에 추가하여 설계하고, 이후 테스트를 통과한 코드들을 개발단계에서 사용한다. 따라서, 코드의 버그 검출능력이 상승하고, 소스코드 또한 매우 간결해진다. 또한 테스트케이스가 존재하기때문에 다른 개발자가 보았을때 코드의 이해가 빨라질수 있기 때문에 협업시 이점이 있다..

하지만 장점 뿐만 아니라 단점도 존재한다.
우선 테스트케이스가 많을수록 실제 개발 소스코드를 완성하기까지의 시간이 증가하기 때문에 기존 개발방식보다 생산성이 떨어진다. 장기적인 측면에서(프로젝트 전체) 보면 개발시간이 줄어들수 있지만, 단기적인 측면에서 바라보았을때 성과를 내기 힘들다는 것이다. 다음으로 기존 개발방식에 체화된 시간이 길수록 개발방식을 바꾸기 힘들다는 것이다.

따라서 무조건적으로 적용하여 사용하는 것보다 특정 상황에 대하여 적용하는 것이 바람직하다고 생각된다.
예를 들어 개발하려는 프로그램의 기능을 많이 구현 해보았다면, 해당 프로그램이 어떠한 예외와 테스트케이스를 염두에 두어야 하는지 잘 알고 있기 때문에 TDD의 적용은 오히려 독이 될수도 있다.
앞서 말한 특정상황이란 처음 개발하게 되는 프로그램, 개발중인 프로그램에 대한 요구조건이 바뀌거나 추가될 요소가 많다고 판단되는 경우, 추후에 다른 사람이 해당 코드를 유지보수해야 하는 경우 등이 있을것 같다.

## TDD 예시

JavaScript에서 사용되는 테스트 프레임워크인 **Jest**를 사용하여 간단한 사용예시를 들어보자.

먼저`pnpm init` 와 `pnpm install --save-dev jest`를 입력하여 package.json 파일을 만들고 Jest를 개발 의존성으로 설치한다.

간단히 테스트할 파일 구조이다.

```
├── node_modules
│   └── jest -> .pnpm/jest@29.7.0/node_modules/jest
├── package.json
├── pnpm-lock.yaml
├── sum.js
└── sum.test.js
```

```
package.json

{
  "name": "tdd_test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "jest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^29.7.0"
  }
}

```

package.json의 test 커맨드를 `jest`로 수정하여 `pnpm test`를 실행하였을때 jest로 하여금 테스트 할수 있도록 만들어 준다.

매우 간단한 더하기 기능을 만들건데, 예외를 두기 위해 매개변수에 숫자가 아닌 값이 들어오면 "숫자가 아닙니다"를 리턴해야한다는 가정을 추가하자.

그렇다면 테스트해야할 사항들은

1. 양수/음수 + 양수/음수
2. 문자열 + 양수 / 음수

정도가 있을 것 같다.

위 2가지 조건에서 Fail을 검출해야 하는 조건은 2번이다.
먼저 위 두가지의 조건을 충족하는 테스트케이스를 작성해보자

```
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
  test("하나와 둘은 숫자가 아닙니다.", () => {
    expect(sum("하나", "둘")).toBe("숫자가 아닙니다.");
  });
});

```

총 4가지의 테스트케이스를 작성해보았는데, 각각 양수+양수, 양수+음수, 음수+양수, 그리고 sum이라는 함수에 필요한 매개변수 중 하나가 문자열인 경우 2개와 두 매개변수가 문자열인 경우를 작성했다.

이제 테스트케이스의 신뢰성을 위해 문자열이 매개변수로 들어간 테스트케이스가 Fail을 리턴하는 검증 코드를 작성한후 테스트를 실행해보자

```
sum.js

function sum(a, b) {
  return a + b;
}

module.exports = sum;
```

`pnpm test` 커맨드를 입력하여 실행하게 되면

```
pnpm test

> tdd_test@1.0.0 test /Users/chungyeonkim/Desktop/tdd_test
> jest

 FAIL  ./sum.test.js
  테스트 그룹
    ✓ 1과 2를 더하면 3이다 (2 ms)
    ✓ 1과 -3을 더하면 -2이다
    ✓ -3과 -10을 더하면 -13이다.
    ✕ 하나는 숫자가 아닙니다. (2 ms)
    ✕ 둘은 숫자가 아닙니다.
    ✕ 하나와 둘은 숫자가 아닙니다.

  ● 테스트 그룹 › 하나는 숫자가 아닙니다.

    expect(received).toBe(expected) // Object.is equality

    Expected: "숫자가 아닙니다."
    Received: "하나2"

      12 |   });
      13 |   test("하나는 숫자가 아닙니다.", () => {
    > 14 |     expect(sum("하나", 2)).toBe("숫자가 아닙니다.");
         |                          ^
      15 |   });
      16 |   test("둘은 숫자가 아닙니다.", () => {
      17 |     expect(sum(1, "둘")).toBe("숫자가 아닙니다.");

      at Object.toBe (sum.test.js:14:26)

  ● 테스트 그룹 › 둘은 숫자가 아닙니다.

    expect(received).toBe(expected) // Object.is equality

    Expected: "숫자가 아닙니다."
    Received: "1둘"

      15 |   });
      16 |   test("둘은 숫자가 아닙니다.", () => {
    > 17 |     expect(sum(1, "둘")).toBe("숫자가 아닙니다.");
         |                         ^
      18 |   });
      19 |   test("하나와 둘은 숫자가 아닙니다.", () => {
      20 |     expect(sum("하나", "둘")).toBe("숫자가 아닙니다.");

      at Object.toBe (sum.test.js:17:25)

  ● 테스트 그룹 › 하나와 둘은 숫자가 아닙니다.

    expect(received).toBe(expected) // Object.is equality

    Expected: "숫자가 아닙니다."
    Received: "하나둘"

      18 |   });
      19 |   test("하나와 둘은 숫자가 아닙니다.", () => {
    > 20 |     expect(sum("하나", "둘")).toBe("숫자가 아닙니다.");
         |                            ^
      21 |   });
      22 | });
      23 |

      at Object.toBe (sum.test.js:20:28)

Test Suites: 1 failed, 1 total
Tests:       3 failed, 3 passed, 6 total
Snapshots:   0 total
Time:        0.267 s, estimated 1 s
Ran all test suites.
 ELIFECYCLE  Test failed. See above for more details.
```

위처럼 테스트 결과가 나오게 된다.

의도한대로 문자열이 매개변수에 들어간 경우는 모두 Fail을 리턴하였으므로, 이제 해당 케이스들이 모두 Success를 할 수 있도록 코드를 수정한다.

```
sum.js

function sum(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    return "숫자가 아닙니다.";
  }
  return a + b;
}

module.exports = sum;
```

이제 다시 한번 테스트를 진행해보자

```
sum.test.js

pnpm test

> tdd_test@1.0.0 test /Users/chungyeonkim/Desktop/tdd_test
> jest

 PASS  ./sum.test.js
  테스트 그룹
    ✓ 1과 2를 더하면 3이다 (1 ms)
    ✓ 1과 -3을 더하면 -2이다
    ✓ -3과 -10을 더하면 -13이다.
    ✓ 하나는 숫자가 아닙니다. (1 ms)
    ✓ 둘은 숫자가 아닙니다.
    ✓ 하나와 둘은 숫자가 아닙니다.

Test Suites: 1 passed, 1 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        0.147 s, estimated 1 s
Ran all test suites.
```

현재 작성한 테스트가 모두 통과했기 때문에 해당 코드를 개발단계로 가져가 사용할수 있다는 뜻이 된다.
