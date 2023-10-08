![](https://velog.velcdn.com/images/cnffjd95/post/161ceaea-b99b-46b9-8a4d-3aed73562ba3/image.webp)

이전 포스팅에 이어서 이번엔 여러 타입의 인터페이스를 공부해보자

### 함수 타입

인터페이스는 함수의 타입을 정의할수도 있다.
변수의 타입을 지정하는것과 비슷하게 함수의 **파라미터와 리턴값을 지정**하여 타입으로 정의한다.

```javascript
interface info {
  // 함수의 파라미터 : 리턴값
  (id : string, pwd = string): boolean;
}

let login : info = function (id, pwd){
  console.log(로그인);
  return true;
}
```

추가적으로 함수타입을 오버로드 시키는 것이 가능하다.

> 오버로딩(Overloading) : 한 클래스 내에 같은 이름의 메서드를 여러개 정의하는 것.
> 타입스크립트의 경우 매개변수와 반환타입이 다른 여러 함수를 여러개 정의한다는 뜻이다.

```javascript
inferface Add {
  (x: number, y: number) : number;
  (x: string, y: string) : string;
}

const add_number : Add = (x: number, y : number) => x + y;
const add_string : Add = (x : string, y : string) => x + y;
```

### 클래스 타입

인터페이스로 클래스를 정의하는 경우, `implement` 키워드를 사용하여 클래스 정의에 작성한다.
또한 `implement`하는 클래스의 프로퍼티는 반드시 해당 인터페이스 클래스에 정의된 내용을 따라야 한다.

```javascript
interface User_inter {
  name: string;
  getName(): string;
}
class User implements User_inter {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  getName() {
    return this.name;
  }
}

const test = new User("test");
test.getName(); // test
```

예시코드에서는 `User_inter`라는 인터페이스를 implement한 `User`클래스를 생성하였다. 이 `User`클래스는 반드시 인터페이스의 속성을 따라야 하기 때문에 `name`과 `getName()` 속성을 모두 가지고 있는 것을 확인할 수 있다.

---

위처럼 타입 구조를 정의하는 것 뿐만 아니라 생성자 함수의 타입구조 또한 정의가 가능하고 이 기능을 **구성 시그니처** 라고 한다.
주로 함수 매개변수에 클래스를 전달하여 함수 호출시 클래스가 초기화되는 로직을 구현시 사용된다.

```javascript
interface FullName {
   firstName: string;
   lastName: string;
}

interface FullNameConstructor {
   new (firstName: string): FullName;
}

class Anderson implements FullName {
   public lastName: string;

   constructor(public firstName: string) { // public firstName 접근 제어자로 선언해서 자동으로 this.firstName으로 만들어줌
      this.lastName = 'Anderson';
   }
}

function makeSon(c: FullNameConstructor, firstName: string) {
   return new c(firstName);
}

function getFullName(son: FullName) {
   return `${son.firstName} ${son.lastName}`;
}

const tomas = makeSon(Anderson, 'Tomas');
const jack = makeSon(Anderson, 'Jack');

getFullName(tomas); // Tomas Anderson
getFullName(jack); // Jack Anderson
```

위 코드에서 `FullNameConstructor`부분이 바로 구성 시그니처이다.
생성자 함수 구조타입을 정의하여 추후 함수에 클래스 자체를 인자로 넘기기 위하여 선언한 것이다. 이후 `makeSon`이라는 함수에서 실제로 `Anderson`이라는 클래스 자체를 받아와서 대신 클래스 초기화를 시켜주는 모습을 확인 할 수 있다.

### 인덱스 타입

만약 인터페이스를 사용하여 정의할 속성이 많아질경우에는 하나하나 작성하는 것이 매우 힘들고 잘못 작성할 확률이 높아진다. 속성간의 규칙이 없다면 어쩔수 없겠지만 규칙이 있는 경우라면 인덱스 타입의 인터페이스를 이용하여 이를 해결할 수 있다.

```javascript
type Score = "A" | "B" | "C" | "D" | "F";

interface User {
  name: string;
  [grade: number]: Score;
}

const user1: User = {
  name: "test",
  1: "A",
};

const user2: User = {
  name: "test1",
  3: "F",
};
```

위 코드는 인덱스 타입의 인터페이스 사용 예제이다.
`User` 인터페이스를 지정하는 부분에서 키값고 밸류값을 각각 타입을 지정하여 객체를 해당 속성에 맞게 구성할 수 있도록 만들었다.
추가적으로 배열 또한 지정이 가능하다.

```javascript
interface Item {
  [itemIndex: number]: string | boolean | number[];
}

let item: Item = ["Hello", false, [1, 2, 3]];

console.log(item[0]); // Hello
console.log(item[1]); // false
console.log(item[2]); // [1, 2, 3]
```

`Item`이라는 인터페이스는 여러개의 타입이 합쳐져 만들어져 있다. 이후 변수생성시 명시한 타입값에 따라 값을 할당하여 해당 인터페이스를 사용할 수 있다. 이때 유의할 점은 `[itemindex]`는 배열의 인덱스 값을 가리키기 때문에 `number` 타입을 사용해야만 한다.
