![](https://velog.velcdn.com/images/cnffjd95/post/761dd893-ce82-46ea-9107-b2e91c6fc64d/image.png)

서버와 클라이언트간의 통신은 HTTP를 통하여 이루어진다. 이 HTTP는 단방향 통신으로써, `클라이언트 Requeset ➡️ 서버` 와 `서버 Response➡️ 클라이언트`를 보내는 방식으로 작동한다.

- 기본적으로 HTTP는 Stateless로 상태를 저장하지 않는다

여기서 한가지 문제점이 발생하는데 서버의 데이터가 업데이트 되더라도 클라이언트에서 요청을 보내지 않는다면 클라이언트는 업데이트된 데이터를 불러올 수 없다는 점이다.

이를 해결하기 위해서 기존에는 주기적으로 서버에 요청을 보내 데이터를 업데이트 하는 Polling이라는 방식을 사용하였다. 하지만 이 방식도 결국 불필요한 요청을 생성하여 결국 서버에 부하가 커지게 된다.
그리고 주기적으로 요청을 보내기 때문에 다음 주기의 요청사이에 데이터가 업데이트 된다면 즉각적으로 반영할수는 없다.

이러한 문제점을 보완할수 있는 기술이 바로 Websocket이다.

## 1️⃣ Websocket이란?

클라이언트와 서버간 양방향 통신(Full-Duplex)을 가능하게 하는 프로토콜이다. 한번 연결을 성공하면 끊기지 않고 계속 연결되어 있다.

- HTTP와는 다르게 Stateful로 같은 연결을 이용하여 통신한다.

이로 인하여 클라이언트 측에서 요청을 보내지 않더라도 서버에 데이터가 업데이트 될때 업데이트된 데이터를 수신할 수 있다.
이러한 특성으로 위치 기반 App이나 증권 거래 사이트 등 실시간 데이터의 변화를 즉각적으로 감지해 업데이트 하는 기능이 들어간 어플리케이션에서 주로 사용되고 있다.

## 2️⃣ 동작 과정

Websocket은 크게 3가지의 동작 과정을 가진다.
![](https://velog.velcdn.com/images/cnffjd95/post/8f2be91d-57dc-4712-a70e-2ea5d90887d6/image.png)

### Opening HandShake

Websocket 클라이언트에서 HTTP upgrade(핸드쉐이크 요청)을 전송하고 응답으로 핸드쉐이크 응답을 받는다. (응답코드 101)

> HandShake란 통신에서 연결을 설정하기 위한 과정이다.
> 이 과정에서 두 통신 장치 간 데이터 교환 규칙, 속도, 보안설정 등을 협상하고 동기화시킨다.

아래는 Opening HandShake에서 사용되는 요청/응답 헤더이다.

요청헤더

```
// HTTP 버전은 1.1이상, GET 메서드를 사용해야 한다.
GET /chat HTTP/1.1
Host : localhost:8000
// 프로토콜을 전환하기 위해 사용하는 헤더이며 이 값이 없거나 다르다면 접속을 중지한다.
Upgrade : websocket
// 전송이 완료 된 후 네트워크 접속을 유지할것인지의 정보. Upgrade라는 값이 없거나 다르다면 접속을 중지한다.
Connection : Upgrade
// 유효한 요청인지 확인하기 위해 사용하는 키값
Sec-WebSocket-Key: --
// 클라이언트가 사용하려는 웹소켓 버전
Sec-WebSocket-Version: 13
```

응답헤더

```
// 101코드와 함께 응답
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
// 요청헤더의 Sec-WebSocket-Key에 유니크 아이디를 더해서 해싱한 후 base64로 인코딩 한 결과
// 웹 소켓이 연결되었음을 알려준다
Sec-WebSocket-Accept: --
Sec-WebSocket-Protocol: chat

```

### Data transfer

Opening HandShake 과정을 거쳐 웹 소켓과 연결이 된 후 진행되는 부분이다.
클라이언트와 서버는 `메시지`라는 개념으로 데이터는 송수신한다.

> 메시지는 여러 frame이 모여 구성되는 단위이다.
> 이 frame에는 Text, Data binary 등 다양한 신호가 들어있다.

- 이 단계에서 클라이언트와 서버는 끊임없이 서로의 상태를 확인하기 위해 heartbeat 패킷을 보내고, 주기적으로 ping을 보내서 체크한다.

- Closing HandShake

### Close HandShake

- Opening HandShake와 반대로 연결을 종료하는 과정이다.

- 클라이언트와 서버 둘다 보낼수 있으며, 둘 중 어디서든지 Close를 송신한다면 수신한측에서 Close 응답을 보내 연결이 종료된다.

- 연결 종료 이후에 수신되는 모든 데이터들은 버려진다.
