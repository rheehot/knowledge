![](https://velog.velcdn.com/images/cnffjd95/post/161ceaea-b99b-46b9-8a4d-3aed73562ba3/image.webp)

대부분의 프로젝트를 진행하면서 자바스크립트보단 타입스크립트를 많이 사용하게 되는데 문법상으로 사용하고 있긴 하나 정확히 어떤역할인지, 기존의 자바스크립트와 무엇이 다른지 잘 모르고 사용하는 경우가 대부분이다. 앞으로 하나하나 공부해보려고 한다.

### interface?

interface의 의미는 **상호 간 정의한 약속, 규칙**이다
여기서 말하는 약속,규칙이란 객체의 속성, 클래스, 파라미터 등을 가리킨다.
즉, 우리가 interface를 사용할때는 어떠한 객체(클래스/함수...)는 ~~한 속성을 가질거야 라고 일종의 규칙을 만들어 주는 것이다.

```javascript
interface Sample {
  name: string;
  age: number;
  married: boolean;
}

let sample_variable: Sample;

sample = {
  name: "augusstt",
  age: 20,
  married: false,
};

let samples: Sample[] = [];

function f_Sample(sample: Sample) {
  samples = [...samples, sample];
}
```

간단한 interface 사용법을 작성한 코드이다.`interface` 키워드를 이용하여 새로운 인터페이스를 정의한다. 이후 변수의 타입으로 `Sample`이라는 인터페이스를 선언하고, 해당 변수에 `Sample`이 가지고 있는 속성들을 할당시킨다.

또한 함수 파라미터의 타입으로 선언이 가능하다.
이 경우에는 파라미터에 지정한 인터페이스를 준수하는 인자를 전달해야 한다.

---

### Optioanl Properties

그렇다면 인터페이스에 정의한 모든 속성을 다 사용해야 하는가?에 대한 생각이 든다.
인터페이스를 선언할때마다 정의한 속성을 반드시 모두 사용해야만 한다면 유연성이 너무 떨어진다.
다행히도 인터페이스는 **선택적 프로퍼티**기능을 제공한다.

```javascript
interface Sample_Optional {
  name: string;
  age: number;
  married?: boolean;
}

function f_SampleOptional(sample: Sample_Optional) {
  console.log(sample.name);
}

let sample_optional = {
  name: "augusstt",
  age: 20,
};
f_sampleOptional(sample_optional); // augusstt

let sample_optional_not = {
  name: "augusstt",
  age: 20,
  email: "test@test.com",
};
```

위 코드처럼 `?`연산자를 붙이면 선택적 프로퍼티가 되어 추후 객체타입을 해당 인터페이스로 설정할때 선택적 프로퍼티를 붙인 속성이 없어도 정상적으로 작동하는 것을 볼 수 있다.
하지만 맨 마지막 `sample_optional_not` 처럼 애초에 없는 속성에 대해 정의는 할수 없다.

선택적 프로퍼티를 사용할때 한가지 주의사항이 있다.
코드를 작성할때 선택적 프로퍼티를 사용하려면 **해당 속성이 있을때만 로직이 작동하게끔 코드를 작성**해 줘야한다. 그렇지 않은 경우, 아래와 같이 속성이 쓰이는지 안쓰이는지 알수 없기 때문에 에러가 발생한다.

```javascript
interface Sample {
  name: string;
  age?: number;
}

let sample: Sample = {
  name: "augusstt",
  age: 20,
};
if (sample.age && sample.age > 20) {
  console.log("미성년자");
}
```

---

### readonly

단어 그대로 읽기 전용 속성이라는 뜻이다.
인터페이스로 처음 객체를 생성하고 값을 할당한 이후로는 변경할 수 없는 속성을 가리킨다.

> const와 유사하지만 const는 변수에 사용하고, readonly는 프로퍼티에 사용된다.

```javascript
interface Sample {
  name : string;
  age : number;
  readonly birth : string;
}

let sample : Sample = {
  name : "augusstt",
  age : 20,
  birth : "xxxx/yy/dd",
}

sample.birth = "2023/10/07"; // Error


```

위 코드처럼 `readonly` 키워드를 사용하여 설정한다. 최초 객체 생성시 이후론 값 변경이 불가하다.
만약 인터페이스의 모든 속성이 readonly일 경우는 **Assertion**, **Utility**를 사용한다.

```javascript
interface Sample_Utility {
  name : string;
  age : number;
  birth : string;
}

let sample_util : ReadOnly<Sample_Utility> = {
  name : "augusstt",
  age : 20,
  birth : "xxxx/yy/dd",
}

let sample_assertion = {
  name : "augusstt",
  age : 20,
  birth : "xxxx/yy/dd",
} as const;
```

> Assertion(타입 단언) : 이 타입은 ~~가 확실하다 라고 컴파일러에게 알려주는 것.
> 형변환처럼 실제 데이터를 변환시키는 것이 아니라 타입에 한하여 컴파일러에게 알려주는 것이므로 데이터가 바뀌지는 않는다. 런타임이 아니라 컴파일 단계에서 사용된다.

---

### extends

기존 자바스크립트에서는 클래스를 상속할때 `extends` 키워드를 사용하는 것처럼 인터페이스에서도 사용된다.

```javascript
interface Middle_student {
  math: number;
}

interface High_student extends Middle_student {
  calculus: number;
}

let student: High_student = {
  math: 80,
  calculus: 60,
};
```

클래스와 비슷하지만 인터페이스는 여러개 `extends`가 가능하다는 점이 차이점이다.

```javascript
interface Korean {
  name: string;
  age: number;
}
interface Hobby {
  game: string;
}

interface Augusstt extends Korean, Hobby {
  married: boolean;
}

const me: Augusstt = {
  name: "augusstt",
  age: 20,
  game: "lostark",
};
```

---

**[reference](https://inpa.tistory.com/entry/TS-%F0%9F%93%98-%ED%83%80%EC%9E%85%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-%F0%9F%92%AF-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0)**
