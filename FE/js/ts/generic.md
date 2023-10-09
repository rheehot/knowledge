타입스크립트를 사용하면서 여러 새로운 개념들을 접했는데 그중 가장 많이 접했던 개념이 바로 제네릭이다. 그동안 제네릭이 정확히 뭔지 이해하지 못했었는데 이번 기회에 공부해보자

### Generic

> 제네릭이란 변수의 구체적인 타입을 명시하지 않고 다양한 타입을 처리하게끔 만들어 주는 기술이다.

만약 같은 기능의 함수인데 매개변수와 반환타입이 달라서 여러개의 함수를 작성해야 한다면 매우 비효율적이다

```javascript
function sample_Num(x: number) {
  return x;
}
function sample_Str(x: string) {
  return x;
}
```

이러한 부분을 제네릭을 사용하여 간단하게 만들어 줄 수 있다.

```javascript
function sample_G<T>(x: T) {
  return x;
}

let num_variable = sample_G < number > 1;
let str_variable = sample_G < string > "제네릭";
```

함수명 뒤에 `<T>`를 작성함으로써 매개변수, 반환값의 타입으로 설정이 가능하다.
다만 T는 타입의 약자로써 자주 사용되는 것이고 다른 문자를 사용해도 무방하다.

제네릭으로 만든 함수를 호출하는 경우, 함수호출 부분 뒤에 `<{타입}>`의 형식으로 인자의 타입을 작성한다.
(`<>`를 생략할 경우 컴파일러가 인수의 타입을 확인하여 타입을 결정한다)

### 그렇다면 any는 왜?

그런데 위에서 말한 내용을 살펴보면 `any` 키워드와 다를 바가 없다. 사실 굳이 제네릭을 사용하지 않더라도 `any`로도 충분히 구현이 가능하기 때문이다.

우리가 제네릭을 사용하는 `any`대신 제네릭을 사용하는 이유는

> 어떤 값을 반환하는지 알기 위해서이다.

```javascript
function sample_Any(x: any) {
  return x;
}

function sample_G<T>(x: T) {
  return x;
}

// 반환값 타입 유추에서 차이가 발생한다.
let any_variable = sample_Any(1);
let generic_variable = sample_G < number > 1;
```

`any`의 경우 어떤 값이든지 반환될수 있어 실제로 반환되는 값이 무엇인지 유추가 힘들다.
**하지만** 제네릭의 경우 어떤 값이든지 반환될수 있다는 점은 같지만, `<>`에 타입을 명시하여 어떤 값이 반환되는지 유추하기 수월하다.

```javascript
function sample_Any(x: any){
  return x.id;
}

function sample_G)<T>(x: T){
  // Property 'id' does not exist on type 'T'
  return x.id
}
```

위 예시 코드가 두번째 차이점이다.
`any`의 경우 변수의 프로퍼티를 확인하지 않는다. 하지만 제네릭의 경우 매개변수로 들어오는 타입이 어떤것인지 알지 못하기 떄문에 에러가 발생한다.
