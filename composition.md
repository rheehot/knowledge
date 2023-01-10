> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 1. 합성(Composition)?

> 합성이란 여러개의 컴포넌트를 합쳐 새로운 컴포넌트를 만드는 것을 말한다.

- 리액트를 사용하여 개발을 하다보면, 여러개의 동일한 컴포넌트들이 하나의 큰 컴포넌트로 구성되어 한 페이지를 구성하는 경우가 상당히 많다.

- 하지만 새로 구성된 하나의 큰 컴포넌트는 자신의 하위 컴포넌트에 어떠한 내용이 올지 모르는 경우가 많다. (ex. 사이드바)

- 이러한 경우 리액트 props의 속성 중 하나인 **_`children`_**을 사용한다.

## 2. Containment 방법

- 하위 컴포넌트를 포함하는 형태의 합성 방법

### 2 - 1. 단일 children

```
Code 1.

function FancyBorder(props) {
  return (
    <div className={'FancyBorder FancyBorder-' + props.color}>
      {props.children}
    </div>
  );
}
```

- Code 1에서 사용된 `props.children`을 사용함으로써 FancyBorder의 **하위 컴포넌트들이 모두 props의 children 속성으로 전달된다.**

```
Code 2.

function WelcomeDialog() {
  return (
    <FancyBorder color="blue">
    /**
     * Code 1에서 생성한 FancyBorder 컴포넌트로 jsx를 감싼다.
     * 감싼 부분의 jsx가 모두 props.children으로 들어간다.
     */
      <h1 className="Dialog-title">
        Welcome
      </h1>
      <p className="Dialog-message">
        Thank you for visiting our spacecraft!
      </p>
    </FancyBorder>
  );
}
```

- Code 2를 살펴 보면 Code 1에서 생성한 FancyBorder 컴포넌트가 사용되었다.
- FancyBorder 컴포넌트가 **감싸고 있는 모든 JSX는 FancyBorder에서 사용된 props.children으로 전달되게 된다.**

### 2 - 2. 여러개의 children

- 1 - 1에서는 한개의 children을 필요로 하는 경우였지만 이번에는 여러개의 children이 필요한 경우를 살펴 보려고 한다.

- 이 경우에는, 별도로 props를 정의해서 원하는 컴포넌트에 넣어주면 된다.

```
Code 3.

function SplitPane(props) {
  return (
      /**
     * SplitPane이라는 컴포넌트를 생성하고, 각각 left, right라는 다른 props 속성을 정의하고, 들어갈 위치를 정한다.
     */
    <div className="SplitPane">
      <div className="SplitPane-left">
        {props.left}
      </div>
      <div className="SplitPane-right">
        {props.right}
      </div>
    </div>
  );
}

function App() {
  return (
    /**
     * 위에서 생성한 SplitPane이라는 컴포넌트의 props인 left, right에 각각 다른 내용을 전달한다.
     */
    <SplitPane
      left={
        <Contacts />
      }
      right={
        <Chat />
      } />
  );
}
```

- Code 3을 살펴보면, 먼저 SplitPane이라는 컴포넌트를 생성한다.
- 이 컴포넌트는 각각 left, right라는 props를 받아와 사용한다. (각각의의 props가 표시될 위치는 다르다.)

- App 컴포넌트에서는 이전에 생성한 SplitPane 컴포넌트를 사용하는데, left와 right라는 props에 표시될 내용(컴포넌트)을 전달시킨다.

## 3. Specialization 방법

- 더 구체적인 컴포넌트가 일반적인 컴포넌트를 렌더링하고 props를 통해 내용을 구성하는 방법을 말한다.

```
Code 4.

function Dialog(props) {
    /**
     * 범용적 컴포넌트
     */
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
    </FancyBorder>
  );
}

function WelcomeDialog() {
    /**
     * 구체적 컴포넌트
     */
  return (
    <Dialog
      title="Welcome"
      message="Thank you for visiting our spacecraft!" />
  );
}
```

- Code 4를 보면 범용적으로 사용이 가능한 Dialog 컴포넌트가 있다.

- 이 컴포넌트는 props 속성 중, title, message에 따라 WelcomeDialog가 될수도 있고, AlertDialog가 될수도 있다.

- Dialog 컴포넌트를 사용하는 WelcomeDialog 컴포넌트를 보면, Dialog 컴포넌트의 props의 title, message를 통하여 내용을 전달하고 있다.

- 이처럼 범용적으로 사용이 가능한 컴포넌트를 만들어 놓고, 이를 특수화시켜 컴포넌트를 사용하는 방법이다.

---

**_reference_**

**리액트 공식 문서 ( https://ko.reactjs.org/ )**
