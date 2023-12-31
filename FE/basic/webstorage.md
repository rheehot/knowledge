![](https://velog.velcdn.com/images/cnffjd95/post/2be19211-253e-4b9b-8964-d5ebb508fb77/image.png)

브라우저 저장소는 도메인과 관련된 데이터를 서버가 아니라 웹 브라우저에 저장하는 기능이다.
원래는 쿠키만 존재하였으나 쿠키의 문제점으로 인하여 web storage가 등장하게 되었다.

## Cookie

먼저 쿠키에 대해서 알아보자.
![](https://velog.velcdn.com/images/cnffjd95/post/d7f5cd3a-e818-4d9d-bc3a-aae38f331cf6/image.png)

쿠키는 서버가 생성하여 브라우저로 전송하는 작은 파일이다.

브라우저는 수신받은 쿠키를 **일정 시간, 사용자 세션 기간 동안 저장**한다. 이후 사용자가 서버에 요청을 보낼때 해당 쿠키를 첨부한다.
따라서 우리가 브라우저에서 여러 페이지를 방문할때마다 로그인을 하지 않아도 상태가 유지될수 있는 것이다.

> 세션 : 사용자가 브라우저를 통해 서버에 접속한 시점부터 종료하여 연결을 끝내는 시점까지 사용자로 부터 오는 요청을 일정하게 유지하는 것.
> 클라이언트마다 id값을 부여하여 각각의 클라이언트를 구분할수 있게 한다.

> 사용자 세션이란 사용자가 서버에 접속해 있는 상태를 말한다.

쿠키에 저장된 정보는 항상 서버로 전송된다.
따라서 사용자가 **어떤 요청을 보내도 항상 쿠키가 포함되어 서버에 전송**되기 때문에 네트워크 트래픽을 유발한다. 그리고 방문했던 웹사이트에 대한 정보들이 기록되어 있기 때문에 **보안측면의 위험성** 또한 존재한다.

이러한 단점을 보완하기 위해서 **Web Storage** 기능이 HTML5에서 추가되었다.

## Web Storage

웹 스토리지는 브라우저 데이터를 서버가 아닌 클라이언트에 `key-value`의 형식으로 데이터를 저장하고, **서버에서 접근할수 없는 값**이기 때문에 **서버로의 전송을 하지 않는다.** 또한 쿠키는 자동적으로 사용자의 모든 요청에 포함되어 전송되지만 웹 스토리지는 필요한 경우에 꺼내서 쓰기 때문에 보안적인 측면에서 더 우수하다.

웹스토리지는 로컬스토리지와 세션스토리지로 나뉜다.

### Local Storage

이름 그대로 사용자 로컬에서 존재하는 저장소다. 사용자의 로컬에 저장되고 직접 저장된 데이터를 지우지 않는 이상 **영구적으로 유지**된다. 따라서 사용자가 사이트를 나가도 데이터가 유지된다는 특징이 있다. **도메인(`protocol://host:port`)마다 각각의 로컬스토리지가 생성**되기 때문에 도메인이 같으면 데이터의 공유가 가능하다.

> 즉, 사용자 로컬에서 생성되는 영구저장소이다.

영구적이라는 특성을 가지고 있기 때문에 집 컴퓨터에서 항상 접속하는 사이트등의 자동로그인같은 기능에 활용된다.
아래와 같이 자바스크립트의 전역객체인 `window`를 통해서 접근이 가능하다.

```javascript
window.localStorage;
```

### Session Storage

로컬스토리지와 마찬가지로 `key-value`의 형식으로 데이터를 저장한다.

로컬스토리지와 가장 큰 차이점은 사용자가 **세션을 종료하는 시점에 데이터가 삭제**된다는 것이다. 사용자가 브라우저를 다시 접속하여 서버와의 접속을 연결하면 새로운 세션이 시작되어 새로운 세션스토리지가 생성된다.
또한 로컬스토리지와 달리 도메인이 같아도 세션이 다르다면 해당 저장공간에 접근이 불가능하고, 각각의 세션스토리지는 독립적으로 동작한다.

> 즉, 사용자가 **세션을 유지하는 기간동안 생성되는 독립적인 저장공간**이다.

일회성이라는 특성을 가지고 있어, 비로그인상태의 활동, 일회성 로그인 등의 기능에 활용된다.
로컬스토리지와 동일하게 `window` 전역객체를 통해 접근할 수 있다.

```javascript
window.sessionStorage;
```

![](https://velog.velcdn.com/images/cnffjd95/post/334e0c5e-8e77-4934-b79b-617ab0b659ad/image.png)
