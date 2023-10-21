지난 포스팅에서 ajax에 대해 공부한 것에 이어서 비동기 통신라이브러리인 axios와 fetch에 대해 공부해보자.

### fetch

먼저 fetch란 es6에서 추가된 자바스크립트 라이브러리이다.
ajax와 다른점은 **`Promise`** 를 기반으로 구성되어 있다는 점이다.

```javascript
let obj = {
  method : "POST",
  headers : {
    "Content Type" : "application/json",
  },
  body : JSON.stringify({
    id : "test",
    pwd : "test"
  }
};

// 받아온 응답 promise객체를 then 메서드를 이용하여 처리한다.
fetch("http://test.com", obj)
	.then((res) =>
        console.log(res))
	.catch((err) => console.log(err));
```

확실히 ajax를 사용했을때보다 코드가 간결해지고 직관적으로 변한것을 볼 수있다.
기본적으로 자바스크립트에 내장되어 있기 때문에 거의 모든 브라우저(IE11은 지원을 하지 않는다..)에서 지원을 하기 때문에 편하게 사용할수 있고, 별도의 import또한 필요없다는 장점이 있다.

유의할점이 있다면 요청 body에 보내는 데이터는 **`JSON.stringify`** 메서드를 사용해야 한다.
이유는 서버와 클라이언트가 만약 다른 언어를 사용한다면 데이터를 주고 받을때 **공통적으로 사용이 가능한 형태로 바꾸어 통신**해야하는데 그것이 바로 JSON 형태이기 때문이다.

### axios

이번엔 axios를 살펴보자. fetch와 달리 자바스크립트 내장 라이브러리가 아니기 때문에 별도의 설치와 import가 필요하다.

`npm install axios`

```javascript
import axios from "axios";

let obj = {
  headers: {
    "Content Type": "application/json",
  },
  timeout: 3000,
  data: {
    id: "test",
    pwd: "test",
  },
};
axios
  .post("http://test.com", obj)
  .then((res) => console.log(res))
  .catch((err) => console.log(err));
```

fetch와 동일하게 Promise객체를 기반으로 구성되어 있어 응답객체를 다루기 수월하다는 공통점이 있다.

코드를 보면 fetch의 코드와 다른점이 2부분 있다.
먼저 사용하던 JSON.stringify 메서드가 없는것을 볼수 있는데, 이는 axios가 자체적으로 응답데이터를 JSON형태로 변환해서 사용할수 있도록 해주기 때문이다.
두번째로는 `timeout`이라는 속성이 생겼는데 axios에서는 이 속성을 이용하여 요청시간을 조절할수 있다. (지정한 시간이 지나면 에러가 발생하여 catch 문에서 에러처리를 수행한다.)

---

![](https://velog.velcdn.com/images/cnffjd95/post/590b144e-f215-4843-87e0-8001daa07f24/image.png)

실제로 npm trend를 사용해 다운로드 수를 조회해보면 두 라이브러리는 거의 동일한 사용수를 보여주고있다.
기능적으로 어느 한쪽이 압도적으로 높거나 하지 않다고 생각되고, 특정 브라우저를 대상으로 앱을 제작하는 것(IE11 브라우저라던지..)이 아닌 이상 본인이 좀더 익숙한 라이브러리를 택하는 것이 맞는것 같다.

개인적으로 fetch보다 axios가 설정해줘야하는 옵션이 적어 사용이 수월하기 때문에 axios를 주로 사용하는 편이다. 만약 추후 프로젝트 빌드용량을 좀 줄이고 싶거나, 버전이슈에 대한 스트레스가 어느정도 생긴다면 axios대신 fetch를 사용할것 같다.
