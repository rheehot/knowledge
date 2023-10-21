자바스크립트로 코드작성을 하다보면 `import`를 사용하여 특정 모듈이나 컴포넌트를 ~~텍스트~~불러와서 사용해야 하는 경우가 많다. 그런데 `import` 말고도 `require`도 사용하는 경우도 종종 생긴다.
이를 찾아보니 Common Js와 ES6의 차이라고 하는데 한번 알아보자.

---

### Common js와 ES

먼저 CommonJS와 ES는 **자바스크립트의 모듈화를 지원**하기위해 개발되었다.

> Common JS는 **node js에서 자바스크립트 패키지를 불러올때 사용하는 방식**을 의미한다.

자바스크립트를 서버사이드 앱에서 사용하려고 개발되었으며, 모듈화에 있어서 각 파일간의 스코프를 확립하여 파일간 사용이 용이하게 한다.

그런데 클라이언트 측에서도 이를 사용하고 있었으나 [바벨](https://velog.io/@cnffjd95/Babel) 포스팅에서 언급했다시피

> **Common JS를 모든 브라우저에서 사용할수 있도록 표준을 만든것이 바로 ECMAScript, ES6**이다.

현재 우리가 사용하는 react, next js 등의 최근의 라이브러리/프레임워크들은 es6방식을 채택하고 있다.

하지만 `script` 태그를 사용하는 브라우저환경이나 node js에서는 아직 common js를 채택하고 있기 때문에, 트랜스파일러(ex. babel)를 사용하지 못하는 경우에는 common js의 문법을 사용해야한다.

---

### 모듈사용에 있어서의 Common js와 ES

두 방식의 문법은 모듈사용에 있어서 큰 차이를 보이는데 간단한 예시를 보자.

```javascript
// ex1
const test = require("./test.js);
// ex2
import test from "./test.js"
```

react, next js 두 프레임워크 (react는 라이브러리지만)가 es6문법을 사용하기 때문에 ex2의 코드는 매우 친숙할 것이다. ex1의 경우, node js(express)에서 사용되는 코드인데, 만약 express에서 es6의 문법을 사용하고 싶다면 앞서 말한 바벨을 설치하여 사용이 가능하다.

이번엔 모듈 내보내기의 경우를 확인해보자.
Common js의 경우, 모듈을 내보낼때 객체를 따로 세팅해줘야한다.

```javascript
const test = () => {
  return "test";
};

module.exports = { test };

//또는
exports.test = test;
```

위 코드처럼 `module`객체의 `exports`를 사용하여 구현한 객체를 내보내는 식이다.

es6의 경우, `export`자체만으로 모듈을 내보낼수 있는 기능이 있기 때문에 조금더 사용이 간편하고 가독성이 좋다.

```javascript
const test = () => {
  return "test";
};

export { test };
```

추가적으로, 한 파일에서 내보낼 기본 객체를 정할때는 `export default`를 사용한다. (react 컴포넌트파일에서 사용되는 이유가 바로 이것이다.)

```javascript
const test = () => {
  return "test";
};

export default test;
```
