> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

> 공부를 하면서 구글링을 해보면 대부분이 Function형으로 작성되어 있지만, Class형으로 작성된 것들도 꽤 존재했다. 항상 Function만을 사용해왔기에 차이점을 잘 몰라 이번기회에 공부하려고 한다.

## 1. 함수형 컴포넌트 (Function)

- 내가 그동안 일반적으로 리액트를 사용하면서 사용한 컴포넌트들은 모두 함수형으로 되어있다.

```
import React from "react";

function App({age}){
	const name = "Function Component";
	return (
    	<div>
        	<p>{name}</p>
            <p>{age}</p>
        </div>
    )
}
export default App;
```

### 특징

- State, LifeCycle 관련 기능 사용이 안되었지만, React Hook으로 사용이 가능하다.

> 여기서 State란 컴포넌트 내에서 변경이 가능한 값을 말한다.
> 함수형은 useState Hook을 사용하여 State를 사용한다.
> ex) `const [testState, setTestState] = useState("");`

- 컴포넌트 선언이 간편하다.

- props를 따로 불러올 필요없이 바로 사용이 가능하다.

## 2. 클래스형 컴포넌트 (Class)

```
import React, {Component} from "react";

class App extends Component {
	render(){
    	const name = "Class Component";
        return (
        	<div>
            	<p>{name}</p>
            </div>
        )
    }
}
```
