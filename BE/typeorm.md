## 📌 Type ORM?

node js에서 실행되고, Type Script에서 작성된 **객체 관계형 매퍼 라이브러리**

ORM이란, 객체와 관계형 데이터베이스를 자동으로 변형 및 연결하는 작업이다.
데이터베이스 변형에 유용하게 사용이 가능
![](https://velog.velcdn.com/images/cnffjd95/post/98c81dec-b51c-4d0a-aa28-7ac3614c12a1/image.png)

**Type ORM**

```bash
const boards = Board.find({title : "Hello", status : 'PUBLIC})
```

**Java Script**

```bash
db.query('SELECT'*FROM boards WHERE title = 'HELLO' AND  status = 'PUBLIC', (err, result) => {
	if(err){
    	throw new Error('error')
    }
    boards = reesult.rows;
})
```

한눈에 봐도 Type ORM을 사용하는 것이 훨씬 쉽고 깔끔하다.

Type ORM이 가지고 있는 특징으로는

- 모델을 기반으로 데이터베이스 테이블을 자동으로 생성한다.
- 데이터 베이스에서 개체를 삽입, 업데이트 , 삭제가 쉽게 가능
- 테이블 간의 매핑 (일대일, 일대다, 다대다) 생성
- 간단한 CLI 명령 제공
