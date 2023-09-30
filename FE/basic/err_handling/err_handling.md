프론트엔드를 공부하면서 정말 많이 접하는 요소가 바로 async await 구문이다. 하지만 기계적으로 async에는 await을 사용해야지 라는 생각으로 무분별하게 사용하고 있던것 같아 이번 기회에 해당 구문을 좀 자세히 살펴보고 공부하고자 한다.

## 1️⃣ async / await

먼저 간단히 async/await에 대해 알아보자.
async/await은 자바스크립트의 비동기 처리 패턴 중 하나이다.
사용하려는 함수 앞에 `async`를 붙여서 사용하며, 해당 구문을 붙인 함수는 항상 **`Promise`** 객체를 반환하고, **Promise가 아닌 값을 반환하게 된다면 Promise로 값을 감싸 반환시킨다.**

await는 async 함수 안에서 사용된다.
Promise가 처리될때까지 함수 실행을 기다리게 한다. 이후 Promise가 처리되면 처리결과와 함께 실행된다.

```
async function Test() {
  return "Finish";
}

const doTest = Test();
console.log(doTest);

function Test2() {
  return new Promise((resolve, reject) => {
    resolve("Finish");
  });
}

const doTest2 = Test2();
console.log(doTest2);

> Promise { 'Finish' }
> Promise { 'Finish' }
```

위 코드를 보면 `Test`라는 함수는 async를 앞에 붙여 비동기 처리를 하는 함수이다. 반환값이 Promise가 아니기 때문에 Promise로 감싼 `Promise { 'Finish' }`를 리턴한다.
그리고`Test2`라는 함수는 아예 반환값이 Promise이기 때문에 두 함수의 반환값은 같다.

## 2️⃣ 예외처리

위에서 말했듯이 async 함수는 항상 Promise를 반환한다.
만약 작업을 성공적으로 처리하면 `Promise.resolve()`를, 실패하면 `Promise.reject()`를 반환한다.
이 Promise.reject()를 어디서 발생하게 할것이냐가 바로 예외처리의 요점이다.

예시를 한번 작성해보자

### 1. try/catch

```
async function test() {
  console.log("Do Test!");
  throw new Error("New Error in function test");
}

function main() {
  try {
    console.log("try start");
    test();
    console.log("try end");
  } catch (err) {
    console.error("catch err in main");
    console.log(err);
    return console.log("main end in catch");
  }
  return console.log("main end");
}
main();

>
try start
Do Test!
try end
main end
Error: New Error in function test
```

위 코드의 실행결과를 살펴보자.
비동기 함수로 선언한 `test`라는 함수에서 에러가 발생했지만, 해당 에러가 `catch`에서 발생하지 않고, `main`함수를 모두 실행한 이후에 발생한 것을 확인 할 수 있다.

> 이유는 **`main`함수는 비동기 함수인 `test`함수가 Promise를 처리하는 과정을 기다리지 않고 실행**되기 때문이다.

test함수의 반환값이 처리된 시점에 이미 main함수의 try/catch문은 모두 실행을 완료했기 때문에 catch문에 걸리지 않아 거부된 Promise를 처리 할수 없기 때문이다.

따라서, 비동기 함수의 에러를 catch문에서 잡기 위해서는

- **await 사용**

- 비동기 함수 호출에서 catch문 연결

이라는 2가지 방법을 사용할수 있다.

### 2. await을 이용한 try/catch

먼저 await을 사용하여 에러처리를 해보자

```
async function test2() {
  console.log("test2 start");
  throw new Error("New Error in function test");
}

async function main() {
  try {
    console.log("try start");
    await test2();
    console.log("try end");
  } catch (err) {
    console.error("catch from main");
    console.error(err);
    return console.log("main end in catch");
  }
return console.log("main end");
}

main();

>
try start
test2 start
catch from main
Error: New Error in function test
main end in catch
```

await를 사용하지 않았을때와 실행결과가 다른것을 볼 수 있다.
간단하게 실행 순서를 알아보도록 하자

- main 함수의 console.log("try start")를 실행.

- await을 사용하여 test2 함수를 실행했기 때문에 해당 함수가 Promise객체를 반환할때까지 이후 실행을 대기한다

- test2의 실행 결과값인 Promise.reject()가 반환되어 곧바로 catch문을 실행한다.

- catch문에 있는 console.error("catch from main")와 console.error(err)를 실행한다.

- catch문 안의 return으로 인하여 console.log("main end in catch") 실행 후 프로그램이 종료된다.

await를 사용하여 test2 함수를 호출했기 때문에 **Promise를 반환할때까지 기다렸다가 이후의 코드들이 실행된다.**

다음으로 직접 catch문을 연결하는 방법이다.

### 3. 직접 catch문 연결

```
async function test3() {
  console.log("test3 start");
  throw new Error("New Error in function test3");
}

function main() {
  console.log("main start");
  test3().catch((err) => {
    console.error("catch from main");
    console.error(err);
    return console.log("main end in catch");
  });
  return console.log("main end");
}

main();
>
main start
test3 start
main end
catch from main
Error: New Error in function test3
```

2번과 달라진점은 `try/catch`문이 사라지고 비동기 함수를 호출하는 부분에 직접 catch를 연결하여 해당 함수가 Promise를 처리한 이후에 catch문이 실행되도록 작성한 코드이다.

두 방법 모두 비동기함수 에러처리에 유용하지만 try catch를 사용하는것이 조금더 간결하고 깔끔해 보인다.

## 3️⃣ 정리

예외처리 1번과 2번에서 나타났듯이 두 방법의 가장 큰 차이점은 **어느 부분에서 프로그램이 에러를 발생시키고 종료되냐는 것**이다.

단순하게 try/catch를 사용하여 코드를 작성하던 과거를 생각해보면 내가 지금 구현하는 기능의 어디서 예외처리를 할 것인지 명확히 생각해본적이 없었던 것 같다.

사용자 입장에서 생각해보았을때, 엄청 중요한 에러가 아닌이상 앱을 사용하는데 지장이 없어야 한다. 하지만 이러한 부분을 고려하지 않는다면 예상치 못한 부분에서 프로그램이 종료되거나 해당 기능을 사용을 못하게 되어 사용자 경험이 매우 떨어지는 결과를 낳을수 있기에 항상 염두에 두고 개발을 하는 습관이 필요해 보인다.
