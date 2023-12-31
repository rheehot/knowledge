지난번 쿠키와 웹스토리지에 대해서 공부해보았는데 이어서 이번엔 인증/인가방식에 대해서 공부해보려고 한다.

## 인증 / 인가

인증과 인가라는 단어가 나왔는데 잠시 용어를 정리하고 가자.

**인증 (Authentication)** 이란 클라이언트에서 **사용자 본인이 맞는지 확인하는 과정**이다.
우리가 흔히 말하는 **로그인**이라고 생각하면 편하다.

**인가(Authorization)**는 인증을 한 후에 수행되며, **인증된 사용자가 어떤 자원에 대하여 접근이 가능한지 확인하는 과정**이다.

간단한 예시를 들자면, 나도 구글에 로그인이 가능하고 동생도 로그인이 가능하다. 구글 db상에 등록된 사용자가 본인이 맞는지 확인하고 등록이 되어있고 본인이 맞음이 확인된다면 인증 (로그인)이 되는것이다.
하지만, 내가 작성한 게시글을 동생이 수정할수는 없다. 이유는 내가 작성한 게시물에 대해서 동생은 수정작업 접근이 불가능하기 때문이다. 이것이 **인가**이다.

다시 돌아와서, 클라이언트에서 유저가 로그인을 시도요청을 보낸 후, 성공했다면 서버는 클라이언트에게 **인증이 완료되었다**라는 의미로 **세션이나 토큰**을 전송한다.

그렇다면 여기서 세션과 토큰의 차이를 알아보자

## 세션

먼저 세션은 사용자의 인증정보가 서버의 저장소에 저장된다.

![](https://velog.velcdn.com/images/cnffjd95/post/1f80da0a-98be-4016-aefb-7538f345259c/image.png)

사용자가 로그인 요청시, 해당 인증 정보를 서버 세션 저장소에 저장 후, 사용자에게 **Session ID**를 발급한다. 발급한 session id는 브라우저의 쿠키형태로 저장된다.

> Session id는 브라우저쿠키에 저장되지만, 인증정보 자체는 서버에 저장된다.

따라서 로그인을 성공했다는 증거인 session id가 **쿠키에 저장되어 있기 때문에** 클라이언트는 모든 요청에 쿠키를 담아 전송하게 된다.
이후 서버는 클라이언트에서 넘어온 **쿠키에 담긴 session id와 서버에 저장된 session id를 비교하여 일치한 경우에만 인가를 수행**한다.

세션은 기본적으로 인증정보를 서버에 저장하기 때문에 (즉, 상태정보를 서버에서 관리한다) 보안성이 매우 높다. 다만, 클라이언트의 상태를 서버에서 유지하기 때문에 세션데이터가 증가하게 되면 부하가 발생할 확률이 크다.

## 토큰 (JWT)

세션과 달리 토큰은 사용자의 인정정보가 서버에 저장되지 않고 클라이언트에서 저장된다.
사용자가 로그인 요청시, 서버에서 **인증이 가능한 토큰을 만들어서 클라이언트에 전달**한다. 이후 클라이언트는 요청시 토큰을 서버로 전달하고, 서버에서는 **토큰의 유효성은 검증하여 인증**하는 방식이다.

> 다시말해, 서버측에서 더이상 상태를 관리하지(유지하지) 않기 때문에 클라이언트의 요청만으로 인증처리가 가능하다.

이 토큰중에 가장 많이 사용되는 것이 바로 **JWT**이다.
Json Web token의 약자로써 단어 그대로 Json형태로 정보를 주고 받기 위해서 암호화된 토큰을 사용한다.

JWT는 헤더, 페이로드, 시그니처 부분으로 나뉜다.

![](https://velog.velcdn.com/images/cnffjd95/post/040e5571-ebd2-421b-92d8-8cb4155e054f/image.png)

- **Header**
  어떻게 토큰을 검증할것인가 에 대한 내용을 담고있다.

- **payload**
  토큰에 담긴 사용자의 정보가 저장된다. (유효기간, 닉네임, 발급대상 등등)
  토큰 자체에 정보가 담겨있기 때문에 서버측에서는 db를 사용할 일이 적어진다.

- **signature**
  헤더와 페이로드를 합친후 서버가 **지정한 secret key로 암호화**시키는 부분이다. (이 Secret Key는 서버가 가지고 있다.)
  때문에 토큰 발급후, 페이로드의 내용이 변조되었어도 시그니처에 **수정전의 내용이 저장되어 있기 때문에 토큰이 변조되었는지 수월하게 파악할수 있다.**

하지만 결국 JWT도 토큰 탈취의 위험으로부터 자유로울수 없기 때문에, `Access Token`, `Refresh Token` 을 사용하는 방식을 주로 사용한다.

**`Access Token`** 은 클라이언트가 가지고 있는 토큰이다. 여기에는 실제 유저의 정보가 들어있는데, 서버에서는 **요청을 받으면 이 토큰을 이용하여 응답을 진행한다.**
그런데 만약 Access Token이 XSS나 CSRF공격으로 인해 탈취된다면 해당 토큰이 만료될때까지 권한이 부여되는 문제가 있다. 하지만 이것으로 인하여 만료기간이 짧아져 버린다면 사용자 입장에서는 사용자 인증을 계속해야 하는 불편함이 생길수밖에 없다.

> **XSS (Cross Site Scriping)** : 사용자가 특정 스크립트를 강제로 실행하도록 유도하여 액세스 토큰을 탈취하는 공격법. Stored Xss와 Reflected Xss로 나뉜다. 클라이언트 측에서 악성코드가 실행된다.
> 사용자가 사이트를 신뢰하여 발생함.
> ![](https://velog.velcdn.com/images/cnffjd95/post/06cdbaba-d6aa-4fbe-a1b6-8f75d7ac53bf/image.png)

> **CSRF (Cross-site Request Forgery)** : 사이트간의 요청을 위조하는것. 공격자가 의도한 행동 (서버에 req를 보내는 행동 - 등록, 수정 등)을 사이트에 요청하게 하는 공격법. 요청받은 서버측에서 악성코드가 실행된다.
> 사이트가 사용자를 신뢰하여 발생함
> ![](https://velog.velcdn.com/images/cnffjd95/post/91a1d6d4-f9bc-4427-8e11-a740fd286d23/image.png)

이러한 문제를 해결하기 위해서 사용되는것이`Refresh Token`이다.
**`Refresh Token`**은 새로운 Access Token을 발급하기 위해 사용한다. Access Token은 짧은 수명을 가지고 있기 때문에 **만료된 토큰을 새롭게 발급하기 위해 사용되는 토큰이다.**

### JWT 동작과정

마지막으로 JWT의 동작과정에 대해 살펴보자

![](https://velog.velcdn.com/images/cnffjd95/post/786603bb-b367-4783-a3af-3d149db4dee6/image.png)

- 클라이언트에서 로그인 요청을 보낸다.

- 요청을 받은 서버는 정보가 맞는지 확인 후, 맞다면 **JWT를 Secret Key** 로 생성하고 응답으로 보낸다.

- 클라이언트는 응답받은 토큰을 로컬쿠키에 저장한다.

- 이후, 클라이언트는 서버에 요청을 보낼때마다 헤더에 토큰을 포함하여 전송한다.

- 서버는 요청이 올때마다 Secret key를 이용하여 전송받은 **토큰이 유효한지 검증**한다.

- 토큰이 검증된다면, 추가적인 정보확인 없이 인가를 수행한다.
