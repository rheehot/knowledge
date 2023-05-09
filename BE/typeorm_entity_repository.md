![typeorm](https://velog.velcdn.com/images/cnffjd95/post/67cc4986-aa03-4cc1-af5a-3e23e834c3d1/image.png)

Nest js와 데이터베이스를 익히면서 사용하는 TypeOrm에 대해 아직 제대로 모르고 사용하는 것 같아 제대로 알고 쓰기 위해 공식문서를 파헤쳐 보았다.

## 1. 📌 Entity?

공식 문서에 따르면, Entity란 연결할 데이터베이스 테이블에 매핑되는 클래스라고 명시되어 있다.

```bash
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number

    @Column()
    description: string
}
```

즉, 연결되는 데이터 테이블이 가지고 있는 인스턴스들을 명시한 것이다.
위의 예시 코드의 경우, User라는 테이블안에 id, firstname, lastname, isActive라는 컬럼이 생성될 것이라고 명시해둔 것이다.

생성한 Entity를 사용하기 위해선 해당 모듈에 등록해야 한다.

```bash
@Module({
  imports: [TypeOrmModule.forFeature([UserEntity])],
  controllers: [UserController],
  providers: [UserService],
})
export class UserModule {}
```

이후, 루트 모듈에까지 등록해주면 된다.

```bash
import { DataSource } from 'typeorm';

@Module({
  imports: [TypeOrmModule.forRoot(), UserModule],
})
export class AppModule {
  constructor(private dataSource: DataSource) {}
}
```

```bash
+-------------+--------------+----------------------------+
|                          user                           |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| description | varchar(255) |                            ||                      |
+-------------+--------------+----------------------------+
```

그 결과 위와 같은 테이블 구조가 생성된다.

## 2. 📌 Repository

앞서 말한 Entity를 관리하기 위해 사용되는 것이 바로 Repository이다.
공식 문서에 따르면, [EntityManager](https://typeorm.io/working-with-entity-manager)와 같은 역할을 수행한다고 써있다.

- EntityManager
  Entity에 대한 생성, 수정, 삭제, 로드 등의 활동을 수행 할 수 있다.

Entity를 관리한다는 것을 곧 데이터베이스 테이블에 대한 CRUD를 수행한다고도 볼 수 있다. 그럼 Nest js의 Service에서 직접 DB에 접근하면 되는데 왜 굳이 Repository를 사용하냐는 의문이 생겼다.

먼저 Repository를 사용하지 않을때의 데이터 흐름을 살펴보자

- 클라이언트에서 Controller로 데이터 전송
  - 이때 데이터는 DTO 객체로 전송된다.
- 데이터를 받은 Controller는 해당 데이터를 Service로 넘김
- Service에서 구현된 로직을 따라 DB에 접근

이 구조에서 발생할 수 있는 문제점은 Service에서 DB에 접근할때 사용되는 로직이 복잡해진다면 비즈니스 로직 자체가 너무 헤비해진다.
또한, 앱의 규모가 커지면 여러 Service가 존재하게 되는데, 각각의 Service들이 서로의 Service를 참조하고 있다면, 코드의 중복과 가독성이 떨어진다는 단점이 존재한다.

이러한 단점을 커버하기 위해 Respository를 사용한다.
Respository를 사용하게 되면, 위 과정 중 마지막 과정에서 Service는 DB에 직접 접근하는 대신 Repository로 데이터를 넘기고 Repository에서 DB에 접근하게 된다.

이 경우, Service에서는 데이터와 상관없이 동일한 방식으로 데이터를 사용할수 있고, 사용하고 있는 DB (mysql, postgresql, mondo db...)와 다른 db로 마이그레이션시, Service를 변경하지 않고 Repository만 변경하면 된다는 장점이 있다.

즉 쉽게 말해 **Repository에서 DB를 중앙통제하는 방식**인 것이다.

그럼 이제 간단한 코드예시를 통하여 Repository를 살펴보자

```bash
import { EntityRepository, Repository } from 'typeorm';
import { User } from './user.entity';

@EntityRepository(Test)
export class UserReposiory extends Repository<User> {}
```

앞서 생성한 Test Entity를 불러와 Test Entity에 대한 Respository임을 명시한다.

이후, Test 모듈에 Repository를 등록해준다.

```bash
import { UserReposiory } from './user.repository';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';

@Module({
  imports: [TypeOrmModule.forFeature([UserReposiory])],
  controllers: [UserController],
  providers: [UserService],
})
export class UserModule {}
```

앞서 Respository를 사용하지 않을때 `imports`에 등록했던 Entity를 `Respository`로 대체된다.

그리고, 이전에 Service에서 구현했던 DB 접근 로직을 Respository로 옮긴다.

```bash
import { EntityRepository, Repository } from 'typeorm';
import { User } from './user.entity';

@EntityRepository(User)
export class UserReposiory extends Repository<User> {
	async createBoard(createUserDto : CreateUserDto) : Promise<User> {
        const {title, description} = createUserDto;
        const user = this.create({
            title,
            description,
            status : UserStatus.PUBLIC
        })

        await this.save(user);
        return user
    }
}
```

구현 부분이 빠진 UserService의 createUser는 다음과 같이 수정된다.

```bash
async createUser(createUserDto : CreateUserDto) : Promise<User> {
    return this.userRepository.createUser(createUserDto);
}
```
