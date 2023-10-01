> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

> 공부를 하면서 구글링을 해보면 대부분이 Function형으로 작성되어 있지만, Class형으로 작성된 것들도 꽤 존재했다. 항상 Function만을 사용해왔기에 차이점을 잘 몰라 이번기회에 공부하려고 한다.

## 1. 함수형 컴포넌트 (Function)

- 내가 그동안 일반적으로 리액트를 사용하면서 사용한 컴포넌트들은 모두 함수형으로 되어있다.

### 1 - 1. 선언 방식

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

### 1 - 1. 특징

- State, LifeCycle 관련 기능 사용이 안되었지만, React Hook으로 사용이 가능하다.

> 여기서 State란 컴포넌트 내에서 변경이 가능한 값을 말한다.
> 함수형은 useState Hook을 사용하여 State를 사용한다.
> ex) `const [testState, setTestState] = useState("");`

- 컴포넌트 선언이 간편하다.

- props를 따로 불러올 필요없이 바로 사용이 가능하다.

## 2. 클래스형 컴포넌트 (Class)

### 2 - 1. 선언 방식

```
import React, {Component} from "react";

class App extends Component {
	render(){
    	const name = "Class Component";
        const {age} = this.props;

        return (
        	<div>
            	<p>{name}</p>
                <p>{age}</p>
            </div>
        )
    }
}
```

### 2 - 2. 특징

- 클래스형 컴포넌트는 Component로 상속을 받아야 하고, render 메서드가 있어야 한다.

- 함수형과 다르게 props 사용시, `this.props`를 통해 값을 사용할 수 있다.

- construnctor라는 메서드가 존재하는데, 생성자로 props를 전달받아 state를 초기화 해야 할때 사용한다. (추후에 생명주기 메서드에 관해 좀 더 공부하고 정리 해야겠다.)

```
import React, {Component} from "react";

class Test extends Component {
	constructor(props){
    	super(props);

        this.state = {
        	age : 20;
        };
    };
    render () {
    	const {age} = this.state;
        return (
        	<div>
            	<p>{age}</p>
                <button onClick={() => {
                		this.setState({age : age + 1});
                	}
                }>
                + 1
                </button>
            </div>
        )
    }
}
export default Test;
```
