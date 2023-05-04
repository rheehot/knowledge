![psql](https://velog.velcdn.com/images/cnffjd95/post/7837b4f6-4fd1-458e-8127-ff596d34783f/image.png)

자주 사용되는 관계형 DBMS를 꼽으라 하면 mysql, postgresql이 있는데 내가 시청한 강의 영상에 사용된것이 바로 postgresql이기도 하고, 이전에 잠깐 사용해 본적이 있는 DBMS라 이번 기회에 상세하게 공부하고 사용해보려 한다.

## 📌 Postgresql

오픈소스 객체관계형 데이터베이스 시스템이다. 보통 ORDMBS이라고 부른다.
다른 관계형 데이터베이스 시스템과 달리, 연산자, 복합 자료형, 자료형 변환자 등 데이터베이스 객체를 유저가 생성할 수 있는 기능을 제공한다.

- template database
  데이터베이스 생성시, 기본으로 생성되어 있는 `template1 database`를 복사하여 생성한다.
  이 `template1 database`는 원본 데이터베이스로 인코딩이나 로케일 같은 설정을 담당한다.
  이것 외에 `template0 database`도 존재하는데, 이것은 `template1 database`의 원본과 같은 상태를 항상 유지하여 수정하지 않은 상태의 데이터 베이스를 생성한다.

### 설치

현재 나는 Mac m1칩을 사용하고 있다.
먼저 homebrew를 이용하여 설치해보자

```bash
# postgresql 종류 확인
brew search postgresql

==> Formulae
postgresql@10     postgresql@11     postgresql@12     postgresql@13     postgresql@14     postgresql@15  postgresql@9.4    postgresql@9.5    qt-postgresql     postgrest

==> Casks
navicat-for-postgresql
```

이렇게 나오는데 가장 최신 버전인 postgresql@15를 설치한다.

```bash
brew install postgresql@15
```

이후 잘 설치되었는지 확인해보자

```bash
brew list
==> Formulae
ca-certificates		gettext			krb5			openssl@1.1		readline		zsh-syntax-highlighting
docker-machine		icu4c			lz4			postgresql@15		zsh-autosuggestions

==> Casks
docker
```

잘 설치되었으므로 이제 실행해볼 차례이다.

### 실행 및 사용

```bash
brew services start postgresql@15
==> Successfully started `postgresql@15` (label: homebrew.mxcl.postgresql@15)
```

실행이 되었으니 이제 postgresql에 접속한다.

```bash
psql postgres                                                                                                                                          ok  base py  13:26:08
psql (15.2)
Type "help" for help.

postgres=#
```

위와 같이 `postgres=#`이 뜬다면 접속에 성공한 것이다.
가장 먼저 현재 db의 유저를 확인한다.

```bash
postgres=# \du
                                     List of roles
  Role name   |                         Attributes                         | Member of
--------------+------------------------------------------------------------+-----------
 chungyeonkim | Superuser, Create role, Create DB                          | {}
 postgres     | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

`\du`를 쉘에 입력하면 현재 데이터베이스에 등록된 유저와, 유저들에게 할당된 권한이 나타난다.
테스트 사용자를 한번 추가해보자

```bash
postgres=# create role testUser with login password '123';
CREATE ROLE
postgres=# \du
                                     List of roles
  Role name   |                         Attributes                         | Member of
--------------+------------------------------------------------------------+-----------
 chungyeonkim | Superuser, Create role, Create DB                          | {}
 postgres     | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 testuser     |                                                            | {}
```

`create role 사용자이름 with login password '비밀번호';`의 명령어로 유저를 생성할 수 있다.
(저 비밀번호는 ""가 아닌 ''로 감싸야 한다...여기서 헛고생을 많이 했다...)
현재 생성한 testUser에는 아무 권한도 주어지지 않았는데 다른 유저처럼 권한을 부여해 보자

```bash
postgres=# alter role testuser createDB;
ALTER ROLE
postgres=# \du
                                     List of roles
  Role name   |                         Attributes                         | Member of
--------------+------------------------------------------------------------+-----------
 chungyeonkim | Superuser, Create role, Create DB                          | {}
 postgres     | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 testuser     | Create DB                                                  | {}
```

`alter role 사용자이름 부여권한`명령어를 사용하여 권한을 부여할수 있다.
위 명령어의 경우, `createdb`를 사용하여 데이터베이스를 사용할수 있는 권한을 부여하였다.

생성한 사용자로 접속하려면

```bash
# 쉘 접속 해제
\q
# 지정한 사용자로 postgresql 접속
psql postgres -U 사용자이름
```

으로 접속할수 있다.
추가적으로 `postgres=#`은 관리자에게 나타나는 쉘이며, `postgres=>`는 관리자가 아닌 사용자에게 나타나는 쉘이다.

생성한 사용자를 삭제하려면,

```bash
postgres=# drop user testuser;
DROP ROLE
postgres=# \du
                                     List of roles
  Role name   |                         Attributes                         | Member of
--------------+------------------------------------------------------------+-----------
 chungyeonkim | Superuser, Create role, Create DB                          | {}
 postgres     | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

`drop user 사용자이름;`의 명령어를 사용하면 된다.

이제 현재 생성되어있는 데이터베이스들을 확인해보자

```bash
postgres=# \list
                                                 List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileges
-----------+----------+----------+-------------+-------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
(3 rows)
```

`\list` 또는 `\l`의 명령어로 현재 생성되어 있는 데이터베이스를 확인 할 수 있다.
(현재 접속되어있는 유저가 가지고 있는 데이터베이스들이다)

데이터베이스를 생성하려면

```bash
postgres=# create database testdb;
CREATE DATABASE
postgres=# \list
                                                   List of databases
   Name    |    Owner     | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileges
-----------+--------------+----------+-------------+-------------+------------+-----------------+-----------------------
 postgres  | postgres     | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             |
 template0 | postgres     | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
           |              |          |             |             |            |                 | postgres=CTc/postgres
 template1 | postgres     | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
           |              |          |             |             |            |                 | postgres=CTc/postgres
 testdb    | chungyeonkim | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             |
(4 rows)
```

`create database db이름;`의 명령어로 새로운 데이터베이스를 생성할 수 있다.
