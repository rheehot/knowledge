> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## DOM?

### 1. 개념

- The Document Object Model(문서객체모델) 의 약자로, html, xml의 프로그래밍 인터페이스.
  > 문서 객체란?
  > html, xml을 Java Script가 인식 / 사용 할 수 있는 객체로 만든것.
- 쉽게 말해 웹 브라우저가 html을 인식하는 방식

- DOM은 tree구조로 이루어져있고, 이것을 **DOM Tree** 라고 한다.

> 즉, **_브라우저가 html을 문저를 인식 / 이용할수 있도록 Tree 구조의 자료형으로 만든 것_**을 DOM이라 한다.

간단한 html을 통하여 예시를 들어보자.

```
<html>
    <head>
        <meta charset = "UTF-8"/>
        <title/>
    <head/>
    <body>
        <div>
            <h1>~~~<h1/>
            <p>xxx<p/>
        <div/>
        <div>
            <ul>
                <li>1. ~~<li/>
                <li>2. xx<li/>
            <ul/>
        <div/>
    <body/>
<html/>
```

위 작성된 코드의 html 구조대로 브라우저는 DOM Tree를 생성한다.
![Tree](https://velog.velcdn.com/images/cnffjd95/post/06dbc191-643a-4dcc-a871-7c841a5949f5/image.webp)
이렇게 Tree형태로 만들어 브라우저가 인식 / 이용할수 있도록 만드는 것이다.

> 위 트리구조에서 각각의 요소를 **node**라 한다.

### 2. DOM을 사용하는 이유

- html은 정적인 컨텐츠이다.
  - 말 그대로 html은 정적인 컨텐츠이기 때문에 사용자와의 인터랙션이 불가능하다.
    - 따라서, Java Script를 사용하여 **사용자와의 인터랙션**이 가능하게 해야 하는데, 이 역할을 DOM이 담당한다.
      > **_JJava Script의 Event => DOM에 해당 Event 반영 => 브라우저 리렌더링_**
    - 요약하자면, 사용자에게 프로그래밍 인터페이스를 제공하는 역할을 한다.

### 3. 유의점

- DOM !== html

  - html문서에 의해 DOM이 생성되지만, html과 DOM은 완전히 같지 않고, 이것에 대한 2가지 대표 케이스가 존재한다.

    1. 작성된 원본 html이 유효하지 않을 경우
       - 이 경우, 브라우저는 자동으로 html문서를 수정(교정한다)
       ```
       원본 html 문서
       <html>
       	Case 1
       <html/>
       ```
       ```
       생성된 DOM tree 구조
       <html>
       	<head><head/>
           <body>
           	Case 1
           <body/>
       <html/>
       ```
       - 렌더링 된 브라우저 화면을 보았을때, 위 2개의 코드는 동일하다.
         하지만, 원본 html문서에 없는 head, body태그를 브라우저에서 수정하여 DOM Tree에 반영된다.
    2. Java Script에 의한 DOM 수정

       - 앞서 말했듯이, 사용자와 브라우저간의 인터랙션을 위해 DOM이 사용된다.
         즉, DOM의 동적 변경이 가능하다는 뜻이고, 당연하게도 원본 html과 DOM Tree는 달라진다.

       ```
       ** Example for Case 2 **

       var case2 = document.createElement("div");
       var case2_text = document.createTextNode("This is Test");
       case2.appendChild(case2_text);
       document.body.appendChild(case2);

       ```

       - 위 코드는 2번째 예시를 나타낸 것이다.
         case2라는 변수는 document에 div 태그를 생성하고, case2_text라는 변수는 생성된 div 태그 안에 "This is Test"라는 텍스트 노드를 생성한다.
         이후 최종적으로 document에 case2라는 변수, 즉 div 태그 안 텍스트를 추가한다.

       - Java Script를 사용하여 html문서를 동적으로 구조를 변경하였고, 원본 html과 DOM Tree는 당연하게도 구조가 다르다.
