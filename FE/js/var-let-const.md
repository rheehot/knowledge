var, let, const는 모두 자바스크립트에서의 변수 선언 방식이다.
하지만 3가지로 분류해놓은 만큼 차이점이 분명히 존재하는데 이번 기회에 제대로 공부해보자

### 1️⃣ var

가장 먼저 등장한 자바스크립트에서의 변수 선언 방식이다.

```
var name = "augusstt"
console.log(name) ; // augusstt

var name = "kuku";
console.log(name) // kuku

name = "test"
console.log(name) // test
```

첫번째 특징은 예시 코드처럼 동일한 변수이름으로 **중복선언이 가능**하므로 가장 마지막에 할당된 값이 변수에 최종적으로 저장된다.

두번째 특징은 **함수레벨 스코프**를 가지고 있다.
즉 함수 내부에서 선언된 변수만을 지역변수, 나머지는 모두 전역변수로 취급한다.

```
function test_var(){
	var f_scope = "함수레벨 스코프";
    console.log(f_scope);
}

test_var(); // 함수레벨 스코프
console.log(f_scope) // ReferenceError : f_scope is not defined

if (true){
	var not_f_scope = "함수가 아닐경우";
    console.log(not_f_scope) // 함수가 아닐경우
}
console.log(not_f_scope); // 함수가 아닐경우
```

함수내부에 한정하여 지역변수로 간주하기 때문에 함수를 제외한 부분에서 var로 선언한 변수는 전역변수로 취급된다.

마지막으로 **변수 호이스팅**에 관한 부분이다.
간단하게 호이스팅에 대해 설명하자면

> 코드가 실행되기 전 필요한 변수들을 모아서 최상단에 선언한것처럼 동작하는 것을 말한다.

유의할 점은 실제로 코드가 최상단으로 올라가는 것이 아니라 자바스크립트 parser 내부에서 처리되는 것이므로 실제 메모리 값에는 변화가 없다.

```
console.log(hoisting_var); // undefined

var hoisting_var = "var 호이스팅";

console.log(hoisting_var); // var 호이스팅
```

var로 선언한 변수 `hoisting_var`가 선언되기 전에 참조되었지만 자바스크립트 내부에서 미리 해당 변수를 선언한 후 undefined로 초기화를 해두어 참조에러가 발생하지 않는다..

언뜻 생각해보면 별 제약이 없기에 편해보이지만 코드가 길고 복잡해질수록 중복선언과 전역변수 취급의 문제로 값의 변경/에러등이 어디서 발생하는지 파악하기 힘들다는 단점이 있다.

이러한 단점을 보완하기 위해 let과 const가 도입되었다.

### 2️⃣ let

ES6부터 도입된 변수 선언 방식이다.

```
let name = "augusstt";
console.log(name) // augusstt

let name = "kuku";
console.log(name) // Uncaught SyntaxError : Identifier 'name' has already been declared

name = "test";
console.log(name) // test
```

예시를 보면 var와의 차이점이 한눈에 보인다.

> **중복 선언은불가능 하지만 재할당은 가능하다.**

또한 **블록레벨 스코프**로써 var와는 다르게 함수 내부를 포함하여 if, while, for등의 코드 블록에서 선언된 변수도 **지역변수로 취급**된다. 따라서 아래 코드와 같이 블록 외부에서는 지역블록변수를 참조할수 없다.

```
if (true){
	let block_scope = "let은 블럭레벨 스코프를 가진다.";
    console.log(block_scope);
}
conole.log(block_scope) // ReferenceError : block_scope is not defined
```

호이스팅의 경우, var와 달리 **코드 실행전에는 변수 선언만 실시하고, 초기화는 실행과정에서 변수 선언문을 만났을때 수행한다.**

> 즉, 호이스팅이 발생하기는 하지만, 값을 참조할수 없기 때문에 호이스팅이 발생하지 않는 것 처럼 보인다.

```
console.log(hoisting_let); // ReferenceError : hoisting_let is not defined

let hoisting_let = "let 호이스팅";

console.log(hoisting_let); // let 호이스팅
```

### 3️⃣ const

마지막 변수 선언방식인 const이다. 기본적으로는 let과 비슷하게 작동하지만 가장 큰 차이점이

> **변수를 재할당할 수 없다.**

```
const name = "augusstt";
console.log(name); // augusstt

const name = "kuku";
console.log(name); // //Uncaught SyntaxError: Identifier 'name' has already been declared

name = "test";
// Uncaught SyntaxError: Identifier 'name' has already been declared
```

즉 const는 선언하는 동시에 초기화되며 일정한 상수의 값을 유지한다.
하지만 객체의 경우, 마찬가지로 값변경이 불가하지만 **객체의 속성은 변경이 가능하다.**

```
const test : {
	name : "augusstt",
    age : 20
}

// 아래처럼 값의 변경은 불가능하지만
test = {
	name : "값 변경",
    age : 2
} // error:  Assignment to constant variable.

// 이처럼 객체의 속성은 변경이 가능하다.
test.age = 25;
```

호이스팅의 경우 let과 동일하게 동작한다.

---

### ++using

TypeScript에서 추가된 키워드이다. 따로 포스팅을 해서 자세히 다룰 예정이니 간단히 소개정도만 하고 넘어가려고한다.

using은 주로 데이터베이스 연결이나 파일처리와 같은 상황에서 let, const를 대체하는 키워드이다.

먼저 using을 사용하지 않았을때의 예시를 보자

```
function writeFile(path:string) {
  const file = fs.openSync(`files/${path}`, 'w+')

  fs.writeFileSync(file, "Text/n")

  if(path.includes("temp")) {
  	fs.closeSync(file)
    return
  }

  fs.writeSync(file, "Permanent")
  fs.closeSync(file)
}

writeFile("a.txt")
writeFile("temp.txt")
```

위 코드를 보면 if문 아래에서 만약 `temp.txt`라는 파일일 경우와 아닐 경우 모두 파일을 닫는 코드를 작성해야 하는 것을 볼 수 있다. 만약 if문 안에서 `fs.closeSync(file)`코드를 작성하지 않으면 해당 경우에 파일을 닫지 않고 return해 버리기 때문이다.

이처럼 코드 블록 중간에서 종료를 시켜야 하는 경우가 있다면 그 위치에 모두 종료를 시켜주는 코드를 작성해야 한다.

using은 바로 이런 경우에서 유용하게 사용될 수 있다.
위의 예시를 `using`을 이용하여 수정해보자

```
function openFile(){
	const file = fs.openSync(`files/${path}`, 'w+);
    return {
    	handle : file,
        [Symbol.dispose] () {
        	console.log("Disposed");
            fs.closeSync(file)
        }
    }
};
```

먼저 다룰 파일을 여는 기능을 가진 함수를 작성한다.
이때 `Symbol.dispose`라는 global symbol이 속성으로 할당되어 있으면 해당 함수를 리소스로 판단되어 선언적으로 using키워드를 사용하여 관리할수 있게 된다.

```
function writeFile(path : string){
	using file = fs.openSync(`files/${path}`, 'w+')

    fs.writeFilesync(file.handle, "Permanent");

    if (path.includes("temp")){
    	return ;
    }
    fs.writeSync(file.handle, "Permanent")
}
writeFile("a.txt");
writeFile("temp.txt");
```

using 변수는 블록 스코프를 벗어나는 순간 해당 변수에 접근할수 없고 동시에 할당된 메모리를 해제 시키기 때문에, 앞선 코드에서 반복적으로 사용된 코드가 제거된 것을 볼 수 있다.
