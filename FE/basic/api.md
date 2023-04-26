> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## API?

### 1. 개념

- Application Programming Interface의 약자로, 운영체제 또는 프로그래밍 언어가 제공하는 기능을 제어 할 수 있도록 만든 인터페이스를 뜻한다.

- UI와 비슷한 역할을 하는데, 사람들이 이용하는 여러 어플리케이션의 데이터를 전달 및 처리하고 프로그램과 프로그램의 상호작용을 이끈다.
  ![](https://velog.velcdn.com/images/cnffjd95/post/19131661-8082-4975-9587-8dec827bcab4/image.png)

- 즉, **_프로그램끼리 데이터를 주고 받기위한 방법과 그 규격을 뜻한다._**

### 2. 종류

1.  **REST API**

    - REST : Representational State Transfer
    - 자원의 이름으로 구분하여 해당 자원의 상태를 주고 받는 것을 뜻한다.
      > ex) 어떠한 DB의 자원이 "성적"이라면, "grade"를 자원의 표현으로 칭한다.

    ![REST](https://velog.velcdn.com/images/cnffjd95/post/f207c39c-4283-47a5-b577-60ebaecf7708/image.png)

    - HTTP URI를 통하여 자원을 명시하고, HTTP Method를 통하여 해당 자원의 전달 방식을 적용한다.
      > HTTP Method
          1. Create(생성) : POST
          2. Read (조회) : GET
          3. Update (수정) : PUT
          4. Delete (삭제) : DELETE
    - 장점
      - HTTP 표준 프로토콜을 사용하는 모든 플랫폼에서 사용이 가능하다.
      - API의 주소와 Method만 봐도 요청의 내용을 알 수 있다.
      - 서버와 클라이언트 개발자 간 소통이 쉽고 혼선이 적다.
    - 단점
      - REST API를 규정하는 표준 규약이 없다.
      - HTTP Method의 갯수가 4개로 제한적이다.
    - RESTFUl
      - 위에 서술한 REST의 원리를 따르는 것을 말한다.
        - REST를 사용하면 모두 RESTFUL한 것이 아니라 REST API의 설계 규칙을 지켜야 한다. (URI 설정, API method 등)

2.  SOAP API

    - SOAP : Simple Object Access Protocol

    - HTTP, HTTPS, SMTP 등을 통해 XML 기반의 메시지를 컴퓨터 네트워크 상에서 교환하는 프로토콜.

    - REST API가 HTTP 프로토콜에 기반한다면, SOAP API는 그 자체로 프로토콜이다.

    - 장점
      - 표준 규약이 정확히 명시되어 있다.
      - REST API에 비하여 훨씬 높은 보안성을 지닌다.
        - 주로 은행, 기업용 어플리케이션 등 보안성이 중요한 곳에서 사용
    - 단점
      - REST API에 비하여 무겁고 느리다.
      - 표준 규약이 정확히 명시되어 있기 때문에 반드시 지켜야 하며, REST API에 비하여 훨씬 어렵다.

![차이점](https://velog.velcdn.com/images/cnffjd95/post/b824316b-c225-4984-93e5-de581139125b/image.png)
