> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

![react](https://velog.velcdn.com/images/cnffjd95/post/74975bdb-7603-49d5-9e50-a9c9d8329843/image.png)

## 1. 생명주기 (Life Cycle)?

- 컴포넌트가 생성되고 사라지기까지, 즉 **앱이 실행되고 종료될때까지 실행**되는 일련의 과정을 말한다.

- 앱이 실행되고 종료되기까지, 메서드로 나누어 관리되는데 이것을 **라이프 사이클 메서드** 라고 한다.

- 크게 3가지 생명 주기를 가지는데, **마운트, 업데이트, 언마운트** 이다.

![](https://velog.velcdn.com/images/cnffjd95/post/7437eba9-5eba-4534-a668-c643bed55316/image.png)

### 1 - 1. 마운트

> 마운트란, **_DOM이 생성되어 브라우저에 나타나는 과정_**이다

- **constructor**

  - 컴포넌트를 생성할 때마다 실행되는 메서드 (가장 먼저 실행된다.)
    - 해당 컴포넌트의 state나 객체를 선언할때 사용된다.

  ```
  constructor(props){}
  ```

- **getDerivedStateFromProps**

  - 컴포넌트의 props로 받아온 값을 state에 넣을때 사용되는 메서드.
  - 컴포넌트가 렌더링 되기 전에 실행된다. (리렌더링때도 마찬가지)
    - 해당 컴포넌트의 state나 객체를 선언할때 사용된다.

  ```
  getDerivedStateFromProps(props, state){}
  ```

- **render**
  - 컴포넌트를 브라우저에 렌더링 할 때 사용되는 메서드.
    - 메서드 뒤 중괄호안에 있는 JSX를 보여준다.
  ```
  render (){JSX}
  ```
- **componentDidMount**
  - 컴포넌트가 첫 렌더링을 마친 뒤에 실행되는 메서드.
  - 호출시점에 컴포넌트는 브라우저에 나타나 있다.
    - axios, fetch 등의 메서드를 이용해 해당 컴포넌트에서 요청하는 작업을 실행한다.
  ```
  componentDidMount(){}
  ```

---

### 1 - 2. 업데이트

> 컴포넌트의 변경사항이 있을때 실시한다. (4가지의 경우 존재)
> 업데이트를 거친 컴포넌트는 리렌더링을 통해 브라우저에 표시.

- **getDerivedStateFromProps**

  - 컴포넌트의 props, state의 변경이 일어났을때 호출되는 메서드

  - 마운트 과정에서 실행된 것과 동일하다.

  ```
  getDerivedStateFromProps(props, state) {}
  ```

- **shouldComponentUpdate**
  - 컴포넌트의 리렌더링 여부를 결정하는 메서드.
  - 반환값이 boolean이고, 이 값에 따라 리렌더링을 결정한다.
  ```
  shouldComponentUpdate(nextProps, nextState) {}
  ```
- **render**
  - 컴포넌트의 리렌더링을 위해 마운트와 마찬가지로 가지고 있는 메서드.
- **getSnapshotBeforeUpdate**

  - 컴포넌트의 리렌더링 직전에 실행되는 메서드.
  - 렌더링 직전의 렌더링 요소 크기나 스크롤 위치등의 DOM의 정보에 접근할 때 사용된다.

  ```
  getSnapshotBeforeUpdate(preProps, preState) {}
  ```

- **componentDidMount**
  - 컴포넌트가 모든 업데이트 과정을 마친 후에 실행되는 메서드.
  - 3번째 파라미터인 **snapshot은 getSnapshotBeforeUpdate 메서드로 부터 받아온 DOM 정보이다.**
  ```
  componentDidUpdate(preProps, preState, snapshot) {}
  ```

---

### 1 - 3. 언마운트

> DOM에서 컴포넌트를 제거하는 과정.

- **componentWillUnmount**
  - 컴포넌트가 브라우저에서 사라지기 전에 실행되는 메서드.
  - DOM에 직접 등록했던 이벤트들을 제거한다.
  ```
  componentWillUnmount() {}
  ```

---

## 2. 함수형 컴포넌트의 생명주기

> 위에서 언급한 생명주기 메서드와 과정은 **클래스형 컴포넌트**의 경우이고, 함수형 컴포넌트의 경우 기능은 같지만 다른 방식으로 구현된다.

### 2-1. 마운트

- **constructor** 기능

  - 클래스형 컴포넌트에서 constuctor 메서드가 수행하는 기능을 함수형 컴포넌트에선 컴포넌트 내부에서 수행한다.
    - axios, fetch 등의 메서드를 이용해 해당 컴포넌트에서 요청하는 작업을 실행한다.

  ```
  import React, {useState} from "react";

  function App(){
      const name = "함수형 컴포넌트";
      const [age, setAge] = useState(20);

      return (
          <div>
              <p>{name}</p>
              <p>{age}</p>
          </div>
      )
  }
  ```

### 2-?. 요약

|      | 클래스형                                   | 함수형                                                                          |
| ---- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| 특징 | render 메서드와 Component 상속 필수        | React Hook 사용, 간단한 Component 선언                                          |
| 단점 | 많은 메모리 사용, state, props 사용이 불편 | useState, useEffect의 메서드를 사용하여 state, 생명주기 메서드를 구현해야 한다. |
