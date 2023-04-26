> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

![ref](https://velog.velcdn.com/images/cnffjd95/post/6b4ad281-5d11-4c16-b8fc-eefb33bbc76e/image.png)

## 1. ref?

> **reference의 약자로, 리액트의 element가 참조하는 변수에 접근하여 제어가 가능하다.**

```
<body>
	<div id="box">
    	<button>클릭</button>
    </div>
</body>
```

- 위의 코드처럼, 일반적인 html에서는 element에는 id라는 속성값을 붙여 DOM에 이름을 붙이며, 이 값은 **`중복되서는 안되는 유일한 값`**이다.

- 이와 같이, 리액트 프로젝트 내부에서 DOM에 이름을 붙이는 역할을 하는 것이 ref이다.

  - 리액트에서 ref를 사용하는 이유?
    - 만약, 위의 코드처럼 DOM에 이름을 붙여 사용한 컴포넌트를 재사용시, **동일한 id를 가진 DOM 요소가 여러개가 된다.**
    - 하지만, ref는 전역으로 유효한 것이 아닌, **`사용된 컴포넌트 내에서 지역적으로 유효하기 때문에`** 문제가 없다.

- 또한 ref는 state와 같이 어떠한 값을 저장하는 공간이 되기도 한다.

- 하지만, ref는 state와 달리, 값이 변할때 리렌더링이 되지 않기 때문에, 전체 컴포넌트를 렌더링 시키지 않고, 내가 원하는 값만 변경하고 싶을때 사용한다.

## 2. useRef

- 리액트의 함수형 컴포넌트에서 ref를 쉽게 사용 할 수 있게 하는 Hook이다.

### 2 - 1. State와 Ref

```
Code 1

import React, { useState } from "react";

const App = () => {
	const [count, setCount] = useState(0);
    const increaseCountState = () => {
    	setCount(count + 1);
    };

    console.log("리렌더링");

    return (
    	<div>
        	<p> State : {count} </p>
            <button onClick={increaseCountState}>
            	+1
            </button>
        </div>
    )
}

export default App;
```

- 위의 코드를 실행해 보면, 버튼을 한번 누를때마다, `count`라는 상태의 값이 변경되면서, 콘솔에 찍은 "리렌더링"이라는 문자가 출력된다.

- 컴포넌트(함수) 내부의 상태값이 변경되어, 컴포넌트 자체가 다시 렌더링 되는 것이다. 자주 변경되는 state값을 사용시, 성능적으로 좋지 않다.

- 이것을 useRef를 사용하여 변경해 보면,

```
Code 2

import React, { useRef } from "react";

const App = () => {
	const countRef = useRef(0);
    const increaseCountRef = () => {
    	countRef.current += 1;
        console.log(`Ref : ${countRef.current}`);
    };

    console.log("리렌더링");

    return (
    	<div>
        	<p> State : {count} </p>
            <button onClick={increaseCountRef}>
            	+1
            </button>
        </div>
    )
}

export default App;
```

- Code 1과 다른점은 이전에 useState를 사용하여 관리하던 상태값을 useRef로 변경한 것이다.

- 버튼을 클릭시, "리렌더링"이라는 문자가 전혀 출력되지 않는다. state와 다르게 값이 변경되도 컴포넌트 (함수)의 리렌더링이 일어나지 않는 것이다.

- 하지만 리렌더링이 일어나지 않더라도, `increaseRef` 함수 내부에 적혀있는 console.log에 의하여 변경되는 ref의 값을 알 수 있다

> console.log(countRef)를 실행해 보면 **{current : 0}이라는 객체 값**을 얻을 수 있다. 우리가 필요한 것은 해당 객체의 **value 값**이므로, increaseRef의 실행 구문에 countRef.current로 작성한 것.

### 2 - 2. 일반 변수와 Ref

```
Code 3

import React, { useRef, useState } from "react";

const App = () => {
	const [render, setRender] = useState(0);
   	const countRef = useRef(0);
    let countVar = 0;

    const increaseRef = () => {
    	countRef.current += 1;
        console.log(`countRef = ${countRef}`);
    };

    const increaseVar = () => {
    	countVar += 1;
        console.log(`countVar = ${countVar}`);
    }

    const doRendering = () => {
    	serRender(render + 1);
    }

    return (
    	<div>
        	<p>Ref : {countRef}</p>
            <p>Var : {countVar}</p>

            <button onClick={doRendering}> Rendering </button>
            <button onClick={increaseRef}> + Ref </button>
            <button onClick={increaseVar}> + Var </button>
        </div>
    )
}

export default App;
```

- 우선 Code 3에 대한 설명을 간략하게 하자면, App 컴포넌트 내의 **일반변수 `countVar`**, **ref인 `countRef`**를 변경시켜주는 함수 increaseVar, increaseRef를 각각 선언한 뒤, **브라우저를 리렌더링 시켜줄 함수 `doRendering`**을 선언 해놨다.

- Code 3을 실행 해 보면, 리렌더링이 되기 전, countVar, countRef는 1씩 증가하면서 잘 작동한다.

- 하지만, doRendering함수가 실행된 후에는 countVar변수는 0으로 초기화 되고, countRef는 이전에 더해진 값이 그대로 유지된다.

- **리렌더링이 일어나면, 컴포넌트(함수)의 모든 로직이 재실행되는데**, 이 과정에서 컴포넌트 내의 **일반 변수 countVar는 0으로 초기화**되지만, **ref는 그렇지 않고 이전의 값을 그대로 유지**한다.

> 정리하자면, useRef는 **어떠한 값을 변화시켜야 하지만, 그 값이 렌더링을 발생시켜야 하지 않아야 할때 사용한다.**
