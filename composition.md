> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

![react](https://velog.velcdn.com/images/cnffjd95/post/74975bdb-7603-49d5-9e50-a9c9d8329843/image.png)

## 1. 합성(Composition)

- 합성이란 여러개의 컴포넌트를 합쳐 새로운 컴포넌트를 만드는 것을 말한다.

- 리액트를 사용하여 개발을 하다보면, 여러개의 동일한 컴포넌트들이 하나의 큰 컴포넌트로 구성되어 한 페이지를 구성하는 경우가 상당히 많다.

- 하지만 새로 구성된 하나의 큰 컴포넌트는 자신의 하위 컴포넌트에 어떠한 내용이 올지 모르는 경우가 많다. (ex. 사이드바)

- 이러한 경우 리액트 props의 속성 중 하나인 **_`children`_**을 사용한다.

### 1 - 1. 단일 children

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

### 1 - 2. 여러개의 children

- 1 - 1에서는 한개의 children을 필요로 하는 경우였지만 이번에는 여러개의 children이 필요한 경우를 살펴 보려고 한다.

- 이 경우에는, 별도로 props를 정의해서 원하는 컴포넌트에 넣어주면 된다.

```
function SplitPane(props) {
  return (
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
