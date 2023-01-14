> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 렌더링 과정

- 브라우저의 렌더링은 크게 4가지의 과정을 통하여 실행된다.

1. HTML, CSS, JS 등 **렌더링에 필요한 리소스를 요청**하고 서버로부터 응답을 받는다.

2. 렌더링 엔진은 서버로부터 받아온 **HTML, CSS를 파싱하여 DOM, CSSOM을 생성**하고 이를 **결합하여 렌더트리**를 만든다

3. 자바스크립트 엔진은 서버로부터 받아온 **자바스크립트를 파싱하여 AST를 생성하고 바이트 코드로 변환 후 실행**한다.

   - 이때, DOM API를 통하여 DOM, CSSOM을 변경할수 있고, 변경 후에는 다시 Render Tree로 결합됨

4. Render Tree를 기반으로 하여 브라우저 화면에 HTML요소를 배치한다.

> 리소스 : 프로그램이 활용 가능한 데이터들을 통틀어 말한다.
> 파싱 (Parsing) : 데이터들을 다루기 쉬운 형태로 바꿔주는 것

- 이제 각각의 과정을 조금더 자세히 살펴보자.

---

## 1. 리소스 요청

- 브라우저의 렌더링에 필요한 요소들은 모두 **서버에 존재**한다.
  따라서, 필요한 리소스들을 서버에 요청하고, 응답한 리소스들을 파싱하여 렌더링하는 것이다.

- 브라우저는 주소창을 통하여 서버에 요청을 보낸다.

  - URI에 대한 간단한 사진
    ![](https://velog.velcdn.com/images/cnffjd95/post/ae114bc4-6eb7-437e-ab8e-240ebd600483/image.JPG)

- 예를 들어, `https://www.testweb.com`으로 접속을 시도한다는 가정을 해보자.
  - 즉, https:// (Scheme)과 www.testweb.com (Host)만으로 구성된 URI에 요청을 보낸것이다.
    - 해당 컴포넌트의 state나 객체를 선언할때 사용된다.
- 요청에는 명확한 리소스가 명시되어 있지 않지만, 서버는 이 요청에 대하여 암묵적으로 `index.html`을 응답하도록 설정되어있다.

- 결론적으로 `https://www.testweb.com`의 요청은 `https://www.testweb.com/index.html`과 같은 요청인 것이다.

## 2. 파싱, DOM, 렌더트리 생성

### 2 - 1. HTML 파싱, DOM 생성

- 브라우저가 요청에 의해 응답받은 HTML 문서를 시각적으로 렌더링하기 위해서는 **HTML을 브라우저가 이해할 수 있는 구조로 변환하여 메모리에 저장**해야 한다.

- 이 과정을 **_HTML 파싱_**이라고 한다.

```
Code 1.

<!DOCTYPE html>
<html>
	<head>
    	<meta charset="UTF-8"/>
        <link rel = "stylesheet" href="style.css"/>
    </head>
    <body>
    	<ul>
        	<li id = "apple"> Apple </li>
            <li id = "banana"> Banana </li>
            <li id = "orange"> Orange </li>
        </ul>
        <script src = "app.js"></script>
    </body>
</html>
```

- Code 1의 HTML 문서가 서버로부터 응답 되었다고 가정하자.

- 브라우저는 다음과 같은 과정을 통하여 문서를 파싱하여 DOM을 생성한다.
  ![파싱](https://velog.velcdn.com/images/cnffjd95/post/0a5f975c-2717-486b-8d1a-2e7fedeef6cc/image.JPG)

> **_DOM은 HTML 문서를 파싱했을때 생기는 결과이다._**

### 2 - 2. CSS 파싱, CSSOM 생성

- 렌더링 엔진은 HTML을 순차적으로 파싱하면서 DOM을 생성하는데, 중간에 CSS를 로드하는 `link`, `style` 태그를 만나면 중단한다.

- 이후, link의 href에 지정된 CSS를 서버에 요청하여 CSS파일 또는 style태그의 CSS를 HTML과 동일한 파싱 과정을 거치며 CSSOM을 생성한다.

- CSS 파싱을 완료하면, 다시 HTML 파싱이 중단된 시점부터 순차적으로 파싱을 시작한다.

### 2 - 3. 렌더트리 생성

- 위의 과정에서 생성된 **DOM과 CSSOM을 결합하여 렌더트리가 생성된다.**

- 렌더트리는 렌더링을 위한 트리구조이기 때문에, **렌더링 되지 않는 노드들은 포함되지 않는다.** - 대표적으로 CSS의 `display : none`이 있다.
  ![렌더트리](https://velog.velcdn.com/images/cnffjd95/post/a6bb0e06-26ef-4cdd-9eb5-51031935db6b/image.JPG)

## 3. 자바스크립트 파싱

- CSS 파싱과 마찬가지로, 렌더링 엔진은 파싱중 `script`태그를 만나면 DOM 생성을 일시 중단한다.

- 그 후, `script`의 src에 명시된 자바스크립트 파일을 서버에 요청하고, 요청받은 자바스크립트 파일, `script`에 명시된 자바스크립트 코드를 파싱하기 위해 **제어권을 자바스크립트 엔진에 넘긴다.**

  > 자바스크립트 파싱은 렌더링 엔진이 아니라 자바스크립트 엔진이 처리한다.

- 자바스크립트 엔진은 자바스크립트를 해석하여 AST을 생성하고, 이것을 기반으로 바이트 코드를 생성하여 실행한다.

  > AST : 컴퓨터 과학에서 추상 구문 트리(abstract syntax tree, AST), 또는 간단히 구문 트리(syntax tree)는 프로그래밍 언어로 작성된 소스 코드의 추상 구문 구조의 트리를 말한다.

- 자바스크립트 파싱을 완료하면, 다시 HTML 파싱이 중단된 시점부터 순차적으로 파싱을 시작한다.

---

**_reference_**

**모던 자바스크립트 Deep Dive**
