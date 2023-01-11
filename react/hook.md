> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 1. 리액트 훅(React Hook)?

- 기존에 사용하던 클래스형 컴포넌트의 단점을 보완하기 위해 등장
  - state, lifecycle 메서드를 사용하기 위함
    - 해당 컴포넌트의 state나 객체를 선언할때 사용된다.
- 즉, **함수형 컴포넌트에서 클래스형 컴포넌트의 기능을 사용하게 해주는 기능**이다.
  - state의 관리를 할 수 있게 해주는 `useState`, 렌더링 이후 실행할 작업을 정의하는 `useEffect`등이 있다.

---

### 1 - 1. State Hook

> 컴포넌트의 상태를 관리하게 해주는 **useState**가 여기 속한다.

```
Code 1.

class Example extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Click me
        </button>
      </div>
    );
  }
}
```

- Code 1을 보면, 클래스형 컴포넌트에서 상태를 어떻게 정의하고 사용하는지에 대한 예시가 있다.

- 여기서의 state는 {count : 0}이며, "Click me"라는 버튼을 클릭하면 state의 변화가 일어난다.

- 이러한 코드를 함수형 컴포넌트에서 Hook을 사용하여 간단하게 바꿀수 있다.

```
Code 2.

import React, {useState} from "react";

function Example(){
	const [count, setCount] = useState(0);
    const clickBtn = () => {
    	setCount(count+1);
    };

	return(
    	<div>
        	<button onClick={clickBtn}>
            	Click me
            </button>
        </div>
    )
}
export default Example;
```

- Code 2와 Code 1은 클래스형, 함수형만 다르고 동일한 기능을 하는 코드이다. 확실히 함수형 컴포넌트에서 Hook을 이용하여 작성하는 코드가 훨씬 가독성도 좋고 간단하다.

- Code 2에서 정의한 `count`는 **현재의 count 상태 값**을 뜻한다.
- `setCount`는 **현재의 count값을 변화시키기 위한 메서드**이다. (현재의 state를 바꿀때 사용한다.)

### 1 - 2. Effect Hook

- 함수형 컴포넌트 내에서 side Effect를 발생할수 있게 하는 Hook이다.

> Side Effect : 컴포넌트 내에서 데이터를 가져오거나, DOM을 직접 조작하는 것 (렌더링이 끝나고 수행되는 작업)

```
Code 3.

import React, {useState, useEffect} from "react";

function Example(){
	const [count, setCount] = useState(0);
    const clickBtn = () => {
    	setCount(count+1);
    };
    useEffect(() => {
    	document.title = `You clicked {count} times`;
    })
	return(
    	<div>
        	<button onClick={clickBtn}>
            	Click me
            </button>
        </div>
    )
}
export default Example;
```

- Code 3에서는 Code 2의 코드에서 useEffect만 추가되었다.

- useEffect 함수는 **컴포넌트의 렌더링이 끝난 후에 수행할 작업을 지정한다.**

- 즉, Example 컴포넌트의 렌더링이 끝나고, count 상태가 정해진 후, 해당 컴포넌트의 title을 `You cliked {count} times`라고 바꾼다.

- 사용자가 버튼을 몇 번 클릭함에 따라, 타이틀의 count의 숫자는 바뀌게 된다.
