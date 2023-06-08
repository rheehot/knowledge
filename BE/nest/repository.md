![nest](https://velog.velcdn.com/images/cnffjd95/post/1aec9b73-036c-4a06-b9ea-0e7a623c0ed9/image.png)

## 📌 Repository Pattern

![repository](https://velog.velcdn.com/images/cnffjd95/post/ad4b7e91-3277-480f-b34f-fdb2ed6aef6b/image.png)

간단히 설명하자면 비즈니스 로직이 있는 Service Layer와 DB에 접근하는 DataSource Layer 사이에 Repository Layer를 생성하여 두 Layer를 중계하는 것을 말한다.

Repository 패턴을 도입함으로써 Service Layer에서 DB 접근 로직을 온전히 Repository로 이전하여 비즈니스 로직에 집중할수 있게 된다.

현재 공부하고 있는 Nest js 에서 한번 적용해 보도록 하자.

### Project tree

우선 현재 프로젝트의 구조이다.

```bash
├── app.controller.ts
├── app.module.ts
├── app.service.ts
├── domain
│   └── users
│       ├── dto
│       │   └── create-user.dto.ts
│       ├── users.controller.ts
│       ├── users.module.ts
│       ├── users.repository.ts
│       └── users.service.ts
├── entity
│   └── users.entity.ts
└── main.ts
```

Repository 패턴을 사용할 것이기 때문에 DB에 접근하는 로직은 모두 `users.repository.ts` 파일에서 구현한다.
통상적으로 `controller => service => repository` 의 흐름으로 데이터가 이동하기 때문에 해당 순서로 코드를 작성하지만 나는 repository에서 필요한 모든 DB 접근 로직을 구현한 후 service, controller의 순으로 작성하는게 더 편할것 같아 반대로 작성하였다.

### app.module.ts

```bash
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersModule } from './domain/users/users.module';
import { User } from './entity/users.entity';

@Module({
  imports: [
    UsersModule,
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'localhost',
      port: 3306,
      username: 사용할 DB 유저 이름,
      password: 사용할 DB 유저 PWD,
      database: 사용할 DB,
      entities: [User],
      synchronize: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

```

본격적으로 Repository 패턴을 구현하기 전에 `app.module.ts`에서 사용할 DB 연결 정보를 세팅한다.

[참고 문서](https://docs.nestjs.com/techniques/database)

### users.repository.ts

```bash
import { Injectable } from '@nestjs/common';
import { User } from 'src/entity/users.entity';
import { DataSource, Repository } from 'typeorm';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UsersRepository extends Repository<User> {
  constructor(private dataSource: DataSource) {
    super(User, dataSource.createEntityManager());
  }

  findAllUsers() {
    return this.find();
  }

  createUser(createUserDto: CreateUserDto) {
    const newUser = this.create({ ...createUserDto });
    return this.save(newUser);
  }
}
```

위의 `app.module.ts` 에서 설정한 DB 정보를 바탕으로 Repository에 적용할 `dataSource` 를 Injection 한다.

constructor에 들어갈 기본 형태는 다음과 같다.

```bash
constructor Repository<User>(
	target: EntityTarget<User>,
	manager: EntityManager,
	queryRunner?: QueryRunner): Repository<User>
```

`target` 에 해당하는 엔터티가 현재 `User`이고, manager에 해당하는 코드가 `dataSource.createEntityManager`이다.

Repository를 상속했기 때문에, DB에 접근하는 `create`, `find` 같은 메서드들을 사용가능하다.

우선 간단하게 `findAllUsers` 라는 현재 DB에 등록된 모든 사용자를 조회하는 함수와 `createUSer` 라는 사용자를 생성하는 함수를 작성했다.

### users.service.ts

```bash
import { Injectable } from '@nestjs/common';
import { UsersRepository } from './users.repository';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UsersService {
  constructor(private usersRepository: UsersRepository) {}

  findAllUsers() {
    return this.usersRepository.find();
  }

  createUser(createUserDto: CreateUserDto) {
    return this.usersRepository.createUser(createUserDto);
  }
}
```

다음은 작성한 Repository를 호출하는 Serice Layer이다.
DB에 접근하는 로직은 이미 Repository에서 구현을 해놨기 때문에 해당 로직을 호출하기만 하면 된다.

`createUser` 메서드를 호출하는 과정에서 dto가 파라미터로 들어가는데 user Dto는 다음과 같다.

```bash
create-user.dto.ts

export class CreateUserDto {
  username: string;
  password: string;
}
```

### users.controller.ts

```bash
import { Body, Controller, Get, Post } from '@nestjs/common';
import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('users')
export class UsersController {
  constructor(private userService: UsersService) {}

  @Get()
  findAllUsers() {
    return this.userService.findAllUsers();
  }

  @Post()
  createUser(@Body() createUserDto: CreateUserDto) {
    this.userService.createUser(createUserDto);
  }
}
```

다음은 controller이다.
작성한 `findAllUsers` 는 조회기능이기 때문에 간단히 `@Get` 데코레이터를 사용하여 구현해주고, `createUser`는 데이터를 작성한 DTO에 따라 Body로 받아올 것이다.

### users.module.ts

마지막으로 작성한 service, controller, repository를 Module에 등록한다.

```bash
import { Module } from '@nestjs/common';
import { UsersService } from './users.service';
import { UsersController } from './users.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from 'src/entity/users.entity';
import { UsersRepository } from './users.repository';

@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [UsersService, UsersRepository],
})
export class UsersModule {}
```

이때, `@Module`의 `providers`에 UsersRepository를 등록하지 않으면

```
Nest can't resolve dependencies of the UsersService (?). Please make sure that the argument UsersRepository at index [0] is available in the UsersModule context.
```

와 같은 의존성 에러가 발생한다. 반드시 module에 생성한 repository를 등록하자.

---

**reference**
[Nest js 공식 문서](https://docs.nestjs.com/techniques/database)
[Type Orm 공식 문서](https://typeorm.io/)
