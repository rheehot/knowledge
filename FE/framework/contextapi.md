최근 프로젝트에 리덕스를 도입하려고 하는데 "꼭 리덕스를 사용해야하나? 리액트면 context api도 사용이 가능할텐데"라는 생각이 들어 context api를 알아보려고 한다.

### Context api

context api는 리액트의 단방향 데이터 흐름으로 인한 props drilling을 해결하기 위해 개발된 내장 라이브러리이다.

`createContext` 메서드를 이용하는데 간단한 예시를 살펴보자.

```javascript
import { createContext, useState } from "react";

interface Props {
  children: React.ReactNode;
}
const CountContext = createContext({
  count: 0,
  plus: () => {},
});
const CountProvider = ({ children }: Props) => {
  const [count, setCount] = useState(0);
  const plus = (): void => {
    setCount(count + 1);
  };

  return (
    <CountContext.Provider
      value={{
        count,
        plus,
      }}
    >
      {children}
    </CountContext.Provider>
  );
};

export { CountContext, CountProvider };
```

Counter를 구현하기 위해 작성하는 Provider이다.
리덕스에서도 Provide라는 키워드를 사용하곤 하는데

> Provider란 정의한 상태를 하위 컴포넌트에게 전달(제공)하는 역할을 수행한다.

기본적인 Provider 형태는 리덕스와 비슷하다.여기서 사용되는 `context`는 리액트의 컴포넌트이다.
즉, context라는 컴포넌트에서 useState를 사용해 전역변수로 사용될 데이터를 설정하고, provider를 통하여 다른 컴포넌트에서도 사용이 가능하게끔 내보내는 것이다.

이렇게 만들어진 context는 통상적으로 부모컴포넌트인 `app` 컴포넌트에서 사용된다. (가장 최상위 컴포넌트이므로)

```javascript
import { CountProvider } from "./context";

function App() {
  return (
    <>
      <CountProvider>. . .</CountProvider>
    </>
  );
}

export default App;
```

이렇게 최상위 컴포넌트에서 자식 컴포넌트를 감싸는 형태로 사용되어, context의 children props에 하위 컴포넌트가 할당되게끔 해준다.

---

### vs redux?

여기서 잠깐 생각해보자.

우리가 Provider의 value에 넣어준 값이 다른 컴포넌트에서 사용될수 있는 값이다.
그런데 value에 넣어준 값은 useState의 반환값이므로 **상태값 자체는 useState가 관리하게 된다.**
실질적으로 **context api가 상태관리를 해주지 않고 useState가 해주는 것**이다.

우리가 말하는 **상태관리**라 함은

- 초기값 저장 (store)

- 현재 값 확인 (useSelector)

- 값 업데이트 (action 객체 -> dispatch)

가 가능해야 한다. redux의 경우 괄호안의 기능으로 위 3개가 다 가능하기에 상태관리 라이브러리라고 할 수 있다. 그런데 context api는 위에 언급했듯이 useState와 useReducer를 통하여 위 3개의 항목을 실시한다.

> 이말은 곧, **context api는 상태관리 라이브러리가 아니라는 뜻이된다.**
> 자연스럽게, **redux와 context api는 비교대상이 아니게 된다.**

redux는 상태관리 라이브러리인데 반하여, context api는 **데이터를 단지 전역적으로 사용할수 있게 만들어주는 라이브러리**이기 때문이다.

그렇기에 우리가 전역**상태관리**가 필요할때는 context api를 사용하지 않고 redux, recoil등의 라이브러리를 사용하는것이다.
