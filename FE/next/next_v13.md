![](https://velog.velcdn.com/images/cnffjd95/post/642adebc-e90b-4fe3-a15f-851dfb4c54af/image.png)

앞으로 진행하게 될 프로젝트 및 공부할 내용에서 Next js를 주로 사용할 계획이다.
과거에 사용해본적이 있지만 v.13으로 업데이트가 되었기에 [Next js 공식 홈페이지](https://nextjs.org/blog/next-13)를 참고하여 어떠한 부분이 바뀌었는지 간단하게 포스팅해보려한다.

## 설치 / 실행

> 설치를 위해 필요한 최소 버전에 변화가 생겼다.
> React : 17.0.2 ➡️ 18.2.0
> Node : 12.22.0 ➡️ 14.6.0

현재까지 업데이트된 최신 버전의 Next js는 아래 명령어를 통하여 설치 할 수 있다.

```
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

추가적으로 pnpm을 사용하려면 아래 명령어를 입력하면 된다.

```
pnpm create next-app [프로젝트 이름]
```

아래는 프로젝트 생성 후 기본적인 프로젝트 구조이다

```
.
├── README.md
├── next-env.d.ts
├── next.config.js
├── node_modules
├── package.json
├── pnpm-lock.yaml
├── postcss.config.js
├── public
│   ├── next.svg
│   └── vercel.svg
├── src
│   └── app
│       ├── favicon.ico
│       ├── globals.css
│       ├── layout.tsx
│       └── page.tsx
├── tailwind.config.ts
└── tsconfig.json
```

## 주요 변경점

### 1️⃣ app 디렉토리 구조 변경

업데이트 전의 Next js는 `pages/`의 경로로 폴더와 파일을 생성하여 라우팅을 설정했었다.
이번 13버전에서부터는 `app/`의 경로로 라우팅을 설정하며, 레이아웃, 서버구성요소, 간결해진 데이터 패칭 등의 기능까지 지원한다.
![구조변경](https://velog.velcdn.com/images/cnffjd95/post/bf3232ea-d557-4255-9f66-7bde20a86552/image.png)

```
├── src
│   └── app
│       ├── favicon.ico
│       ├── globals.css
│       ├── layout.tsx
│       └── page.tsx
```

기본적으로 생성되어 있는 app 디렉토리 안의 page.tsx(jsx)는 해당 경로를 방문하였을때 나타나는 페이지 컴포넌트이다.

```
├── src
│   └── app
│       ├── test
│       │  └── page.tsx
│       ├── favicon.ico
│       ├── globals.css
│       ├── layout.tsx
│       └── page.tsx
│
```

위의 경로로 프로젝트를 구성한다면 `localhost:3000`의 경로에는 `app/page.tsx`가, `localhost:3000/test`의 경로에는 `app/test/page.tsx`가 표시된다.

### 2️⃣ Layouts

페이지에서 사용되는 공통적인 UI들을 `children`을 감싸는 컴포넌트로 제공한다.
공통적으로 사용되는 레이아웃의 상태를 유지하고, 불필요한 리렌더링을 방지하여 성능을 향상시킨다.

프로젝트 디렉토리의 최상위 수준에서 정의된 layout을 `Root Layout`이라고 한다.
이 Root Layout에는 몇가지 규칙이 존재한다.

- app 디렉토리에서는 반드시 Root Layout을 포함해야 한다.

- html, body 태그를 정의해야 한다.

```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

기본적으로 Layout들은 중첩이 가능한데 이것들을 Nesting Layouts (중첩 레이아웃)이라고 한다.
정확히는 app 하위 디렉토리안에 정의된 Layout들을 뜻하는데, children prop을 통하여 하위 Layout을 맵핑한다.

```
app/test/layout.tsx

export default function TestLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <h2>레이아웃 테스트</h2>
      <a>{children}</a>
    </div>
  );
}
```

위 예시코드를 작성하게 되면 test 하위 디렉토리에서 렌더링하는 모든 페이지에 해당 Layout이 중첩되어 나타난다.

아래는 공식홈페이지에서 사용된 사진과 코드이다.
![](https://velog.velcdn.com/images/cnffjd95/post/efec20f4-8dce-4265-9579-fe619bcab155/image.png)

```
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

> Template.tsx는 Layout과 비슷한 역할을 하지만 상태가 유지되는 Layout과 달리 항상 새로운 Children을 생성한다.

### 3️⃣ Server Component

위에서 말했듯이, 기존 Next js에서 사용되던 pages 디렉토리가 app 디렉토리로 변경되었는데, 이 **app 디렉토리 내부의 모든 컴포넌트가 서버 컴포넌트로 동작한다.**

만약 서버 컴포넌트가 아니라 클라이언트로 동작되게 하고 싶다면 아래와 같이 해당 컴포넌트 파일 최상단에 `use client`를 명시해주면 된다.

```
"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked the Count++ button {count} times</p>
      <button onClick={() => setCount(count + 1)}>Count++</button>
    </div>
  );
}
```

서버 컴포넌트는 클라이언트에 전송되는 코드량을 줄여서 초기 페이지 로딩을 빠르게 만들고, 토큰 및 API 키와 같은 민감한 데이터를 서버에 안전하게 보관할 수 있다.

### 4️⃣ Data Fetching

기존에 사용하던 Next js 구버전에서 Data Fetching을 수행하려면 `getStaticProps` 또는 `getServerSideProps`를 사용해야 했지만, 이제 이 함수들을 사용하지 않고 해당 로직을 구현할 수 있게 되었다.

```
// This request should be cached until manually invalidated.
// Similar to `getStaticProps`.
// `force-cache` is the default and can be omitted.
fetch(URL, { cache: 'force-cache' });

// This request should be refetched on every request.
// Similar to `getServerSideProps`.
fetch(URL, { cache: 'no-store' });

// This request should be cached with a lifetime of 10 seconds.
// Similar to `getStaticProps` with the `revalidate` option.
fetch(URL, { next: { revalidate: 10 } });
```

위 코드와 같이 SSG, SSR, ISR(추후에 자세히 다뤄보려고 한다)를 fetch()를 이용하여 간단하게 구현할수 있게 되었다.

### 5️⃣ Turbo Pack (Alpha)

![](https://velog.velcdn.com/images/cnffjd95/post/a85f783d-076b-48d6-8e6c-913501029da9/image.png)

기존에 사용하던 Barbel에서 마이그레이션하여 새로운 Bundler인 Turbopack을 적용하였다. 공식 페이지의 소개로는 webpack, vite보다 뛰어난 성능을 가지고있다고 한다.
공식 홈페이지에 소개된 자세한 수치로는

- Webpack보다 700배 빠른 업데이트

- Webpack보다 4배 빠른 스타트

- Vite 보다 10배 빠른 업데이트

로 소개되고 있다. 장기적으로 webpack의 역할을 수행할수 있도록 빌드하는 것 같다.

---

여기까지 Next js 공식홈페이지를 참고하여 간단하게 변경점을 알아보았는데 추후, Next js를 사용하여 느낀 상세한 변경점들은 그때그때 따로 포스팅하려 한다.
