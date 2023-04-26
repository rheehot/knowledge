> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

![event](https://velog.velcdn.com/images/cnffjd95/post/a23070b6-b4ce-4f86-8043-67f1f4a879f2/image.png)

### Event?

- 이벤트란 사용자가 키보드를 입력하거나, 마우스로 특정 버튼을 클릭하는 등, 어떤 특정한 동작을 실시 하는 것을 말한다.

  > 즉, 사용자가 브라우저에서 DOM 요소들과 상호 작용하는 것을 말한다.

- 이벤트를 처리한다는 것은 "사용자가 어떠한 행동을 하였을 때, 어떠한 결과물을 나타내"라고 하는 것.

```
<button onCick={clickEventFunc}>클릭</button>

. . .
function clickEventFunc (){
	return (
    	alert("클릭했음!")
    )
}
```

- 예를 들면 위의 코드에서 "클릭"이라는 버튼을 누르면 clickEventFunc라는 함수가 실행되는데, 이 함수는 "클릭했음" 이라는 알림창을 띄워준다.

- 즉, "클릭"이라는 **이벤트가 발생**하였을때, **"clickEventFunc"라는 함수로 하여금 이벤트 처리**를 지시하는 것이다.

  > 이벤트 타겟 : 이벤트가 일어날 객체를 뜻한다

- 이벤트 타입
  - 클릭, 스크롤, 호버 등, 어떤 이벤트가 발생했는지를 뜻함.
- **리액트에서 "div", "button", "input"등 DOM 요소에는 이벤트 등록이 가능하지만, 각각의 컴포넌트에는 등록이 불가하다.**
  ```
  function Component(){
      return(
          <div>
              <Component name="컴포넌트"/>
          </div>
      )
  };
  ```
  - **_이런 식으로 props 전달은 가능하지만, 이벤트 등록은 불가하다._**

```
function Component(){
    const [inputValue, setInputValue] = useState("defaultValue");
    const handleChange = (event) => {
        setInputValue(event.target.value);
    }
	return (
    	<div>
        	<input onChange={hadleChange} defaultValue={inputValue} />
        </div>
    )
}
```

- 또한 위의 코드처럼 이벤트 타겟 Element의 value를 State로써 저장이 가능하다.

### 기본동작 방지

- 대부분의 이벤트는 브라우저에 의하여 자동으로 수행된다.
  - 링크 클릭시 url 이동, form 태그의 새로고침

```
<div>
	<button type="submit">버튼 클릭</button>
</div>
```

- 위의 버튼 태그를 클릭하면 "submit"타입의 기본 이벤트 동작으로 인하여 페이지가 새로고침 된다.
- 물론 새로고침이 필요한 경우도 있겠지만, 매번 버튼을 클릭할때마다 페이지가 새로고침 될 순 없으므로, 이때 이벤트 기본동작을 방지 해야 한다.

```

```
