> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 1. 화살표 함수?

- 자바 스크립트 ES6에서 추가되었으며, 간결하게 함수를 표현할 수 있다.

```
화살표 함수

const ArrowFunc = () => {
	return "화살표 함수";
}

일반 함수
function NormalFunc(){
	return "일반 함수";
}
```

## 2. 일반 함수와 화살표 함수 차이점

### 2 - 1 . this

- 일반 함수에서의 this는 **_전역객체 (window)_**를 가르킨다.

```
function Example(){
	console.log(this);
};

Example()
// console.log에 찍힌 this는 윈도우 객체를 표시한다.
```

- 화살표 함수에서의 this는 **_언제나 상위 스코프의 this_**를 가리킨다.

```
function arrFun() {
    this.name = "하이";
    return {
    	name: "바이";
        speak: () => {
            console.log(this.name);
        },
    };
}
```

- 위의 코드와 같이 arrFun의 반환객체안의 speak는 화살표 함수를 이용하여 name : "바이"와 console.log(this.name)을 반환하고 있다.

- 하지만 화살표 함수의 this는 **상위 스코프인 arrFun의 this를 가리키므로**, "하이"를 출력하게 된다.

### 2 - 2 . 생성자 함수

- 생성자 함수를 사용할수 있는 일반 함수와 달리, 화살표 함수는 사용이 불가하다. (**prototype 프로퍼티를 가지고 있지 않기 때문**)

```
function fun() {
    this.name = "일반함수";
}
const arrFun = () => {
    this.name = "화살표함수";
};

const funA = new fun();
console.log(funA.name);     // 일반함수

const funB = new arrFun(); // Error
```

### 2 - 3 . argument

- 일반 함수는 실행이 될때 argument 변수가 전달이 되기 때문에 사용이 가능하지만 화살표 함수는 argument가 전달되지 않아 사용이 불가하다.

```
function fun() {
    console.log(arguments); // Arguments(3) [[1, 2, 3, ... ]]
}

fun(1, 2, 3);

const arrFun = () => {
    console.log(arguments); // Uncaught ReferenceError: arguments is not defined
};

arrFun(1, 2, 3);
```

**_reference_**

**모던 자바스크립트**
