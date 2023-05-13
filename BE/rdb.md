이전에 postgresql에 대한 포스팅을 한 적이 있는데 사실 관계형 데이터베이스에 대한 이해도가 그리 높지 않은 상태에서 사용을 먼저 하는 것이 좋은 방향성이라고 생각되지 않아 이에 대해 공부해보려 한다.

## 📌 관계형 데이터 베이스

말 그대로 데이터들 간의 관계를 바탕으로 한 데이터 베이스이다.
열(Column)과 행(Row)으로 이루어진 2차원 테이블로 데이터를 표현한다.
열에는 데이터의 속성이 위치하고, 행에 열속성에 해당하는 데이터가 위치한다.

```bash
board table

 id |   title    |    description   |    author
----+------------+-------------------------------
  2 | docker     |   다음은 docker    | augusstt06
  1 | test       |   test입니다.      | qwer12
(2 rows)
```

현재 사용하는 postgresql도 관계형 데이터베이스의 일종이다.
위 테이블은 이전에 생성한 Board 게시물을 저장하는 테이블이다. 행에는 각각의 데이터가, 열(Column)에 id, title, description이라는 데이터들의 속성이 명시되어있다.

### "관계"

그렇다면 이 관계라는 단어가 뜻하는 것이 정확히 어떤것인지 알아볼 필요가 있을 것 같다.
여기서 사용되는 관계라는 단어는 각각의 테이블이 가지고 있는 행의 데이터들이 연결되어 있는 것을 뜻한다.

```bash

 id |   title    |    description   |   author   |   author-ranking
----+------------+--------------------------------------------
  3 | RDB        |   Database       | augusstt06 |  38
  2 | docker     |   docker         | augusstt06 |  38
  1 | test       |   test           | qwer12     |  24
(2 rows)
```

만약 위와 같은 테이블이 존재한다고 가정해보자.
각각의 author의 랭킹이 변동 될 때마다 행에 있는 author-ranking의 값을 변경해줘야 한다.
이러한 수고를 줄이기 위해 관계형 데이터베이스는 **기본키**와 **외래키**를 이용하여 다음과 같이 테이블을 구성한다.

```bash
Board-Table

 id |   title    |    description   |   author
----+------------+------------------------------
  3 | RDB        |   Database       | augusstt06
  2 | docker     |   docker         | augusstt06
  1 | test       |   test           | qwer12

(2 rows)
```

```bash
Author-Table

  author    |   author-ranking
----+------------+-------------
 augusstt06 |        38
 qwer12     |        24

(2 rows)
```

- 기본키 (Primary Key)
  테이블이 가지고 있는 고유한 ID 필드

- 외래키 (Foreign Key)
  기본키를 참조하는 필드이며 각 테이블의 행을 연결시키는 역할을 한다.

위의 DB 테이블에서 기본키는 `author`이며, 외래키는 `Board-Table`의 `author`이다.

관계형 데이터베이스에서는 이 두개의 키를 이용하여 테이블내의 중복을 없애고, 이 과정을 **정규화**라고 부른다.

### SQL

SQL(Structured Query Language)은 말 그대로 구조적 쿼리 언어로 관계형 데이터 베이스 시스템의 데이터들을 관리하기 위해 설계된 프로그래밍 언어이다.
자료의 검색과 관리, DB 스키마 생성과 수정, DB객체 관리를 위해 사용된다.
이 sql문은 크게 3가지로 나뉜다.

- DDL (Data Definition Language)

이름 그대로 DB 객체를 생성,삭제,변경하는 역할을 한다. 주로 DB 설계단계에서 사용된다.
자주 쓰는 명령어로는 `CREATE`, `DROP`, `ALTER`가 있다.

- DML (Data Manipulation Language)
  DB를 조회, 삽입, 삭제, 변경하는 역할을 하며 주로 관리 목적으로 사용된다.
  자주 쓰는 명령어로는 `SELECT`, `INSERT`, `UPDATE`등이 있다.

- DCL (Data Conrtol Language)
  사용자의 권한을 관리하는 역할을 한다.
  주로 `GRANT`, `DENY`, `REVOKE`등이 있다.

#### 규칙

유저가 사용하는 DBMS에 따라 조금 상이한 부분이 있지만 일반적인 규칙은 이렇다.

- 세미콜론

명령이 끝나는 부분은 `;`으로 구분한다. 세미콜론 이전의 명령어가 몇줄이던 하나의 명령어로 인식한다.

```bash
SELECT * FROM Table;

SELECT *
FROM Table;
```

- 주석
  우리가 알고 있는 그 주석이다
  단일라인의 주석과 여러라인의 주석사용법이 다르다

```bash
-- SELECT TEST 단일라인 주석
SELECT * FROM Table;
```

```bash
/*
SELECT * FROM Table
여러 라인을 주석한다.
*/
SELECT * FROM Table;
```

- 대소문자
  sql은 문자열을 제외하고는 대소문자를 가리지 않는다. 하지만 주로 가독성을 위해 대소문자를 구분하여 사용한다.

```bash
SELECT * FROM Table;

Select * from table;
```
