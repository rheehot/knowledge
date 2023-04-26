![](https://velog.velcdn.com/images/cnffjd95/post/efe3c1ff-38b9-43e2-a0b5-ec4681f8a2be/image.png)

## Nginx

- 경량화 된 소프트웨어 `Web Server`

- 클라이언트가 웹 요청을 받았을때 , 요청에 맞는 static 파일을 응답해주는 HTTP Web Application Server (WAS)

- 로드 밸런서, 웹 서버 가속기 등 여러 역할을 담당하지만 이번에는 이미지 서버에 초점을 맞추어 적용할 예정이다.

### 기능

1. HTTP Server

   - WAS를 거치지 않고 요청에 맞는 Static File(ex. React build file)을 응답한다.

   > WAS : Web Application Server의 약자로 동적인 요청을 처리하는 서버를 말한다.
   > 흔히 아는 백엔드 서버이다.

2. Reverse Proxy Server

   - Client의 요청과 Server의 응답을 중개하는 서버역할

   - 로드 밸런서의 역할
     - 서버의 **부하** (Load)를 **분산** (Balancing)시키는 것

### 장/단점

1. 장점

   - 이벤트 중심 접근 방식

   - 단일 스레드로 여러 연결을 처리 가능

   - 최소한의 리소스로 독립형 HTTP 서버 배치

2. 단점

   - 동적 컨텐츠 처리 X

   - 동적 컨텐츠를 처리시, 외부지원 연계가 필요 (ex. php fpm)
