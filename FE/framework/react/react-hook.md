![](https://velog.velcdn.com/images/cnffjd95/post/2436fe97-bdad-4895-85a3-8c458a6831a8/image.png)

리액트를 사용하며 가장 많이 사용하는 것 중 하나가 바로 React Hook이다.
useState, useEffect 등의 Hook을 많이 사용하곤 했는데 무엇을 React Hook이라고 부르는 것이며 무슨 역할을 하는지 [공식 문서](https://ko.legacy.reactjs.org/docs/hooks-intro.html)를 보며 공부해보자

## React Hook?

리액트 컴포넌트는 함수형과 클래스형으로 선언할수 있다.
기본적인 두 선언방식의 차이는 아래와 같다.

클래스형 컴포넌트

- State, LifeCycle 기능 사용 가능

- 메모리 자원을 함수형보다 적게 사용

함수형 컴포넌트

- State, LifeCycle 기능 사용 불가능

그럼 간단히 예시 코드를 작성해보자.

```
Class

import React, {Component} from "react";

export default class App extends Component {
	render(){
    	return (
        	<div>
            	클래스형 컴포넌트
            </div>
        )
    }
}
```

```
Function

import React from "react";

function App(){
	return (
    	<div>
        	함수형 컴포넌트
        </div>
    )
}
```

만약 위의 코드에서 상태 초기 값을 선언해야 한다고 가정해보자.
그렇다면 클래스형 컴포넌트에서는 코드를

```
import React, {Component} from "react";

export default class App extends Component {
	constructor (props){
    	super(props);

        // 상태값은 객체형식이다.
        this.state = {
        	age : 20
        };
        setAge = () => {
        	this.setState({age : age + 1})
        }
		render(){
          return (
              <div>
                  클래스형 컴포넌트
                  <p>나이 : {this.state.age}</p>
              </div>
          )
        }
    }
}
```

이렇게 constructor안에서 `this.state`를 사용하여 선언 할 수 있고, `this.setState(상태값)`를 통하여 상태 값의 변경이 가능하다.

그렇다면 함수형 컴포넌트에서는 어떻게 선언할까?

```
import React, {useState} from "react";

function App(){
	const [age, setAge] = useState(20)
	return (
    	<div>
        	함수형 컴포넌트
            <p>나이 : {age}</p>
        </div>
    )
}
```

매우 익숙한 코드이다. `useState`를 사용하여 상태값을 선언하고 변경한다.

그런데 분명 함수형 컴포넌트에서는 상태값에 관련된 기능을 사용하지 못한다고 했는데 우리는 useState를 이용하여 상태값을 사용하고 있다. 이 useState가 바로 **React Hook**의 대표적인 예이다.

> React Hook은 함수형 컴포넌트에서 클래스형 컴포넌트의 기능을 온전히 사용할수 있도록 해주는 기능이다.

기본적으로 함수형 컴포넌트는 리렌더링시 함수안의 코드가 다시 실행된다. 따라서 컴포넌트 안의 상태값이 초기화되어 상태와 관련된 기능을 사용하지 못했던 것이다.
그런데 React Hook은 상태를 브라우저 메모리에 저장하여 상태값을 유지할수 있게 만들어 함수형 컴포넌트에서 사용되는 것이다.

React Hook을 사용하는 몇가지 규칙이 존재한다.

- 최상위 레벨에서 호출해야 한다.
  React Hook은 호출된 순서에 의존한다.
  따라서 반복문이나 조건문, 중첩된 함수 내에서 사용할 경우 실행순서가 뒤바뀔 우려가 있어 훅이 정상적으로 작동하기 어렵다.

- 리액트 함수 내에서만 호출해야 한다.

## 자주 사용되는 React Hook

이제 자주 사용되는 React Hook 몇개를 알아보자

### useState

위에 예시를 들었듯이 동적으로 상태를 관리 할 수 있게 만드는 Hook이다.
클래스형 컴포넌트의 `setState`와 유사하게 동작한다.

기본적인 형태는 아래와 같다.

```
const [state, setState] = useState(initialValue)
```

초기값을 인자로 받으며 현재 상태, 상태를 업데이트 하는 함수를 반환한다.

### useEffect

Side Effect를 수행하는 Hook이다.

> Side Effect란 프로그램 실행 도중 어떠한 객체에 접근해서 변화가 일어나는 것을 말한다.

useEffect는 렌더링 이후 지정한 의존성변수가 변경될때 실행되는 Hook이다.
클래스 컴포넌트의 `componentDidMount`, `componentDidUpdate`와 유사하게 동작한다.
기본적인 형태는 아래와 같다.

```
useEffect(Callback Function, [dependencies])
```

첫번째 인자는 컴포넌트에서 실행할 콜백 함수이고, 두번째 인자는 콜백 함수가 실행되는 시점, 즉 해당 변수가 변경될 때 콜백함수가 실행하라고 알려주는 값이다.

> 즉, 컴포넌트가 다시 업데이터 된다고 하더라도 특정 변수의 값에 의존하여 실행되도록 설정하는 Hook이다.

### useMemo

Hook의 이름 그대로 메모하는 기능을 가졌다. 그렇다면 어디메 메모하는것이 관건이다.
프로그램이 동일한 계산을 반복하는 작업을 수행할때 이전 계산 값을 `메모리`에 저장하여 **반복수행을 제거**하고 결과적으로 **컴포넌트의 성능을 최적화** 시키는데 사용된다.

기본적인 형태는 아래와 같다.

```
const memo = useMemo(() => function, [dependencies])
```

useEffect와 유사하게 2번째 인자가 변경되면 함수가 실행된다.
조금 다른점은 **의존성변수가 변경되었을때만** 메모리에 저장할 값을 다시 계산하고 해당 값을 사용하는 컴포넌트는 모두 리렌더링 된다.
따라서 의존성 변수가 변경되지 않는다면 이전에 메모리에 저장되어 있던 값을 바로 반환하고 컴포넌트는 리렌더링 되지 않기 때문에 때문에 최적화에 사용되는 것이다.
