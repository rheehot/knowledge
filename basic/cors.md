> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 1. CORS

![cors](https://velog.velcdn.com/images/cnffjd95/post/44c4d12f-a0e6-4a21-a7a7-d687598b81e2/image.png)

### 1 - 1 개념

- CORS : 교차 출처 자원 공유 (Cross-Origin Resource Sharing)

- 간단히 말해, 브라우저에서 다른 출처의 자원을 서로 공유하는 것을 뜻한다.

  > 같은 출처 : 페이지 주소의 프로토콜, 호스트, 포트가 모두 동일한 것

- 브라우저에서는 SOP를 따르기 때문에 그에 대한 예외 사항이다.
  > SOP (Same Origin Policy) : 동일 출처 정책으로, 다른 출처의 리소스 공유를 금지하는 것

### 1 - 2 동작 원리

1. 브라우저의 요청을 보낼때

   - Origin 헤더에 자신의 Origin을 설정

2. 서버 응답 확인
   - **Access-Control-Allow-Origin** 헤더에 설정된 Origin의 목록에 요청의 Origin 값이 있나 확인한다.

## 2. CORS 해결

### 2 - 1. 로컬에서만 해결

- 구글 크롬의 **Allow CORS: Access-Control-Allow-Origin**을 설치한다.
- 말 그대로 로컬에서만 해결하는 방법으로 환경이 달라지면 적용이 안된다.

### 2 - 2. 응답 헤더 설정

- 서버에서 근본적으로 응답헤더를 설정해주는 방법이다.
- **Access-Control-Allow-Origin**을 설정해준다.
  예시

  ```
  app.express.get('/example', (req, res) => {
    // 특정 도메인만 허락하므로 추천
    res.setHeader('Access-Control-Allow-origin', 'https://localhost:1234');

    // 쿠키 주고받기 허용
    res.setHeader('Access-Control-Allow-Credentials', 'true');
  });
  ```

- 또는 CORS 미들웨어를 설치하여 해결한다.
  `npm install cors`

  ```
  const cors = require("cors");
  const app = express();

  app.use(cors());
  ```

### 2 - 3. Proxy 설정

- 사실 주로 API를 호출하는 프론트엔드단에서 할 수 있는 가장 좋은 해결책이라 생각된다.
- 공개 API를 사용할 경우, 서버 코드를 수정 할 수 없을 뿐더러 로컬에서만 수정하는 것도 한계가 있기 때문이다.

- 현재 내가 주로 사용하는 React에서는 아래와 같은 방식으로 간단하게 Proxy 설정을 할 수 있다.

  ```
  package.json

  "proxy": "https://testUrl:3222.com",
  ```

- 이렇게 proxy 설정을 한 후, url뒤에 추가적인 주소가 붙는다면 그 주소만 붙여서 요청해 주면 된다.

  ```
  API Requeset

  export const getAPI = async() => {
  	try{
    	const res = await customAxios.get("/later/url/123");
      console.log(res.data)
    } catch(err){
    	console.log(err
    }
  }
  ```

  - 위와 같이 요청을 하게 되면, `https://testUrl:3222.com/later/url/123`으로 요청을 하게 되는 것이다.
