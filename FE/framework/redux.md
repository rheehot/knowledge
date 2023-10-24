## Redux

리덕스는 데이터를 중앙의 `store` 에서 관리하여 전역 상태를 관리 할수 있게 도와주는 자바스크립트의 상태관리 라이브러리이다
사용하면서 리덕스가 어떻게 동작하는지 아직 100% 이해하지 못한것 같아서 이번 기회에 공부해보자

![](https://velog.velcdn.com/images/cnffjd95/post/c3ab3ead-1791-4d3d-b894-273dc41cc865/image.png)

리덕스에서 알아야 할 핵심 키워드는 `store`,`reducer`, `action`, `dispatch` 이다.

---

**`store`** 는 상태를 관리하는 곳이다. 이곳에서 **전역으로 사용할 상태를 관리**하는데, 컴포넌트에서 어떠한 상태를 조회하고 싶다면 `useSelector`를 사용해 store에 접근하여 데이터를 얻는다.
(유의할 점은 하나의 상태는 하나의 store가 관리해야 한다.)

**`action`**은 컴포넌트가 상태를 변경할때 "이 상태를 이렇게 변경 할거야" 라고 알려주는 것이다.
객체로 표현되고, 이 객체를 만들기 위해 **액션 생성 함수**를 이용한다.
간단한 예시를 보자.

```javascript
const ADD_NUM = "ADD_NUM";
const MINUS_NUM = "MINUS_NUM";

function isAdd() {
  return {
    type: ADD_NUM,
  };
}

function isMinus() {
  return {
    type: MINUS_NUM,
  };
}
```

최초 액션의 타입을 정의하고, `isAdd`라는 액션 생성 함수에서 액션 객체를 반환한다. (타입 선언 부분은 문자열을 사용해도 되지만, 변수로 사용해 실수를 줄이는 것이 나아보인다.)

그런데 어떻게 바꿀것인지는 정했는데 이걸 어디서 처리해주지?라는 생각이 든다. 이 장소가 바로 **`reducer`**이다.

```javascript
const initialState = {
  num: 0,
};

function CounterReducer(state = initialState, action) {
  switch (action.type) {
    case ADD_NUM:
      return {
        ...state,
        num: state.num + 1,
      };
    case MINUS_NUM:
      return {
        ...state,
        num: state.num - 1,
      };
    default:
      return { ...state };
  }
}
```

`reducer`는 생성한 액션을 전달받아 store에 있는 현재 상태를 액션의 내용대로 업데이트 해준다.
여기서, 액션을 reducer로 전달하는 역할을 해주는것이 바로 **`dispatch`** 인 것이다.

```javascript
import { useDispatch, useSelector } from "react-redux";
import { isAdd, isMinus } from "./CounterReducer";
import React from "react";

const Counter = () => {
  const count = useSelector((state) => state.num);
  // dispatch를 사용하여 액션을 리듀서에 전달한다.
  const dispatch = useDispatch();

  return (
    <div>
      <h1>{count} </h1>
      <br />
      <button onClick={() => dispatch(isAdd())}> + </button>
      <button onClick={() => dispatch(isMinus())}> - </button>
    </div>
  );
};

export default Counter;
```

그럼 한번 과정을 정리해보자.

> 먼저, 상태를 어떻게 바꿀것인지에 대한 **액션객체가 액션 생성 함수로부터 생성**된다.
> 만들어진 액션 객체는 **dispatch를 통해서 reducer로 전달**되는데, reducer에선 받아온 액션객체를 참고하여 **새로운 상태를 만들어 store에 저장**한다.

라는 과정을 가지는 것이다.
