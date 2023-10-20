앞으로의 프로젝트를 제작하는데 있어서 Next js를 사용할 예정이라 자주 사용할 부분을 템플릿으로 만들어두는 작업을 하고있다.
그 중 하나가 간단한 로그인 부분을 템플릿으로 만들어놓으려고 하는데 제작에 있어서 **[`Next-Auth`](https://next-auth.js.org/)**를 사용할 예정이라 해당 라이브러리에 대해 포스팅해보려한다.

### Next-Auth란?

공식문서에 따르면 **Next js를 위한 오픈소스 인증 라이브러리**이다.
**Serverless**로 구동이 가능하며 네이버, 카카오, 구글 등 인기있는 로그인서비스를 기본적으로 지원해준다.
(예전에 간단하게 Next-Auth를 사용한 경험이 있었는데, 복잡한 로직없이 구글 아이디와 연동되어 로그인이 가능하게 하였던 기억이 있다.)
물론 Serverless로 설계되었지만 AWS, Heroku 등 어디서나 실행이 가능하다 라고 설명되어있다.

또한 보안부분에 있어서, 로그인/아웃 요청시 내부에서 CSRF 토큰을 사용하여 요청을 검증한다

> CSRF (Cross Site Requeset Forgery) 토큰 : 서버 어플리케이션에서 생성되어 클라이언트와 공유되는 인증값.
> 서버-클라이언트 통신간 올바른 CSRF 토큰을 보유해야 통신이 연결된다.

### 사용법

기본적으로 설치는 아래의 명령어를 입력하면 된다.

```bash
npm/pnpm install next-auth
```

Next-Auth는 동적 API Route를 이용하여 로그인을 구현한다. 우리가 Next js에서 라우팅을 구현할때와 비슷하게 여러 경로의 api요청을 구성한다.

구 버전의 Next js에서는 `src/pages/` 디렉토리에서 라우팅을 수행했지만 업데이트된 13버전에서는 `app/`으로 변경된 것에 맞추어 사용법이 조금 바뀌었다.

**`api/auth/[...nextauth]/route.ts`** 의 경로로 핸들러를 생성해야 한다.

```javascript
// 경로 : app/api/auth/[...nextauth]/route.ts

import NextAuth from "next-auth";

const handler = NextAuth({
  provider : [...],
              .
              .
              .
});
export { handler as GET, handler as POST }

```
