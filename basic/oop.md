![](https://velog.velcdn.com/images/cnffjd95/post/bb784dcc-20ad-4344-a24d-b8eabf9dcae7/image.webp)

## 1. 객체지향 프로그래밍 (Object-Oriented Programming)?

> ❗️ 프로그램을 수많은 객체 (Object)로 나누고,그 객체들간의 상호작용을 통하여 로직을 구성하는 것

이라고 정의되어 있는데 처음 봤을 때는 이해가 잘 안가서 몇번을 다시 봤는지 모르겠다. 사실 내가 지금껏 공부하고, 작성했던 코드가 모두 객체 지향 프로그래밍이다.
![src](https://velog.velcdn.com/images/cnffjd95/post/b86142aa-80e1-4e07-901f-33d24ebdec13/image.png)

현재 진행중인 블로그 프로젝트의 폴더이다.

프로그램을 구성하는 파일들을 크게 역할에 따라 폴더로 나뉘어 있는것을 확인 할 수 있다. pages 폴더에는 각 페이지가 나타내야 할 항목들을 프로그래밍 하는데, 각 파일들은

```
export const getServerSideProps: GetServerSideProps = async (context) => {
  const category = context.query.category;
  const res = await axios.get(url, {
    withCredentials: true,
  });
  return { props: { data: res.data } };
};

export default function Project({ data }: any) {
  const router = useRouter();

  const category_query = router.query.category;
  return (
    <>
      <header className="ex-header">
      .
      .
      .
```

이렇게 여러 함수들로 이루어져 있고, 그 함수안에는 변수, 메서드 등 여러 **객체**로 이루어져 있다.

위에서 정의된 말을 한번 다시 보자.
`프로그램을 수많은 객체 (Object)로 나누고,그 객체들간의 상호작용을 통하여 로직을 구성하는 것`

동일하다.

블로그를 구성하는 프로그램은 엄청나게 많은 함수들로 이루어져 있고, 그 함수안에는 사용되는 변수나 메서드 객체들이 정의되어 서로 상호작용하며 프로그램의 로직을 구성한다.

쉽게 다시 말하면 객체 지향 프로그래밍은 `프로그램을 객체들의 모임`으로 보는것으로 이해했다

## 2. 객체 지향 프로그래밍의 특징

### 2 - 1. 추상화

정의를 먼저 보자면

> **객체에서 공통된 속성과 행위를 추출하는 것**

역시나 정의만 보고는 한눈에 이해하기는 힘든 것 같다. 간단한 예를 들어 이해해보자

![추상화](https://velog.velcdn.com/images/cnffjd95/post/665085a6-0be1-45a0-aa4e-28709608ab19/image.png)

아우디, 니싼, 볼보는 다른 외형, 다른 내부 구성을 지녔지만 결국 같은 `자동차`이다. 자동차가 가지는 `공통적인 특징(전진, 후진, 브레이크 등)을 가진 각기 다른 객체`라고 볼 수 있다. 추후에 다른 자동차 브랜드가 출시 되더라도 `자동차`라는 객체가 갖는 공통적인 특징은 가지고 출시 된다.

> 아우디, 니싼, 볼보 (객체들)에서 공통된 속성(자동차)와 행위(전/후진, 브레이크 등)을 추출하는 것. 이것이 추상화이다.

### 2 - 2. 캡슐화

캡슐화의 정의 먼저 확인해보자

> **객체에 대한 구체적인 정보를 노출시키지 않도록 하기 위해 데이터 구조와 데이터를 다루는 방법들을 결합시켜 묶는 것**
> || 비슷한 역할을 하는 속성과 메서드 들을 하나의 틀(클래스)에 묶는 것

아직은 뭔지 잘 모르겠지만 무엇인가를 묶는 것인거 같다.
자바스크립트에서의 간단한 예시를 들어보자

```
var Score = function(math, eng){
	var coef = 1.2

    this.getMath = function(){
    	return math * coef
    }

    this.getEng = function(){
    	return eng * coef
    }
}

var my_score = new Score()

console.log(my_score.getMath(80,60))
console.log(my_score.coef) //undefined
```

위의 코드를 보면 Score로 선언된 생성자 함수 안에 getMath와 getEng라는 메서드는 this로 선언되어 객체의 프로퍼티로 적용되어 상위 레벨에서도 참조가 가능하다.
하지만 coef라는 변수는 접근이 불가능하다.

> 캡슐화를 통하여 coef라는 객체의 중요한 변수를 숨기기 위해 Score라는 하나의 객체로 묶었다고 볼 수 있다.(자바스크립트의 클로저 참조)

### 2 - 3. 상속

오랜만에 익숙한 단어가 나왔지만 역시 정의 먼저 확인해보자

> **클래스의 속성과 행위를 하위 클래스에 물려주거나 하위 클래스가 상위 클래스의 속성과 행위를 물려받는 것**

다행히도 내가 알고있는 상속과 같은 의미다.
자바스크립트에서는 `extends`를 사용하여 새로 생성되는 자식 클래스가 부모 클래스의 속성을 그대로 이어받아 사용 할 수 있다.

### 2 - 4. 다형성

> **하나의 변수명, 함수명이 상황에 따라 다른 의미로 변형할 수 있다는 것**

쉽게 말해서, 한 객체의 속성/기능이 맥락에 따라 다른 역할을 수행 할 수 있다는 것이다.
대표적인 예로는 메서드 오버라이딩이 있다.

> 오버라이딩(Overriding) : 자식 클래스에서 부모 클래스의 기능을 재정의 할때 사용되는 기능

간단한 코드 예시를 보자

```
function testScore(math, eng){
	this.math = math;
    this.eng = eng
};

testScore.prototype.getScore = function(){
	return `My Math score is ${this.math}, English Score is ${this.eng}`
};

function Score (math, eng, korean){
	this.math = math;
    this.eng = eng
	this.korean = korean
}
Score.prototype = new testScore();

// getScore를 상속한 자식에서 재정의
Score.prototype.getScore = function(){
return `My Math score is ${this.math}, English Score is ${this.eng} and Korean Score is ${this.korean}`
}
```

testScore라는 부모 클래스에서 정의된 getScore라는 메서드가 testScore를 상속한 자식 클래스에서 재정의 되었다.

> 즉, 하나의 함수명 (getScore)가 자식에게 상속되어 재정의됨으로써, 다른 값을 가지게 되었다.

## 3. 객체 지향 프로그래밍의 장/단점

위에서 살펴본 4가지의 특징은 베이스로한 객체 지향 프로그래밍의 장/단점을 살펴보자

### 3 - 1. 장점

먼저 **추상화**를 통해 객체 단위로 모듈화하여 프로그램을 설계하기 때문에, 업무 부담이 줄어들고 이로인해 대규모 프로그래밍에 적합하다.

또한, **상속과 다형성**을 통하여 코드 재사용이 용이하여 프로그램의 유지보수가 편해진다.

마지막으로 **캡슐화**를 통하여 공개를 원치 않는 정보를 은닉할 수 있기 때문에 보안성 측면에서 높은 수치를 나타낸다.

### 3 - 2. 단점

객체들의 상호작용으로 프로그램이 구성되기에 초기 설계의 난이도가 올라간다.
또한, 프로그램의 모든것이 객체이기 때문에 추가적인 포인터의 크기와 메모리 연산에 대한 비용이 들어간다.

## 4. 객체 지향 설계 원칙 (SOLID)

마지막으로 객체 지향 설계원칙 5개를 살펴보고 포스트를 마무리 하겠다.

### 4 - 1. 단일 책임 원칙 (Single Responsibility Principle)

모든 클래스는 하나의 책임을 가져야 한다. 즉, 클래스는 그 책임을 완전히 캡슐화 해야 한다.
간단히 말해, `**_하나의 클래스는 하나의 기능만을 수행해야 한다는 것이다._**

### 4 - 2. 개방 / 폐쇄 원칙 (Open/Closed Principle)

기존의 코드는 변하지 않으면서 (Closed) 기능을 추가 할수 있도록(Open) 설계가 되어야 한다는 원칙이다.

### 4 - 3. 리스코프 치환 원칙(Liskov Substitution Principle)

설계되는 프로그램의 객체는 정확성을 깨뜨리지 않은채 하위 타입의 인스턴스로 치환될수 있어야 한다.

간단히 말해 **_자식 클래스는 언제든지 부모 클래스를 대체 할 수 있어야 한다_**는 말이다.
부모 클래스 자리에 자식 클래스를 넣어도 이상 없이 잘 작동해야 한다.

### 4 - 4. 인터페이스 분리 원칙 (Interface Segregation Principle)

범용적인 인터페이스 하나보다 클라이언트를 위한 여러개의 인터페이스가 낫다는 원칙이다.
**_클라이언트가 필요로 하는 인터페이스를 분리하여 각각의 클라이언트가 사용하지 않는 인터페이스에 변경이 있어도 영향을 받지 않도록 만들어야 한다_**

### 4 - 5. 의존 관계 역전 원칙 (Dependency Inversion Principle)

의존 관계를 맺을때, 변화가 쉬운 것보다 변화하기 어려운것에 의존하라는 원칙
**_즉, 구체적인 클래스보다, 추상화나 인터페이스에 의존하라는 것_**

---

reference (참고 및 사진 출처)

https://velog.io/@nayeon/%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-OOPObject-Oriented-Programming

https://hckcksrl.medium.com/solid-%EC%9B%90%EC%B9%99-182f04d0d2b
