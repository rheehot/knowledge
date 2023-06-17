이전에 User Module을 Repository Pattern을 사용해서 만들어 보았는데 이번엔 유저가 게시물을 생성하는 Board Module을 만들어 User Module과 연결해보자

### Project Tree

```bash
├── app.controller.ts
├── app.module.ts
├── app.service.ts
├── domain
│   ├── boards
│   │   ├── boards.controller.ts
│   │   ├── boards.module.ts
│   │   ├── boards.service.ts
│   │   ├── dto
│   │   │   └── board.dto.ts
│   │   └── repository
│   │       └── boards.repository.ts
│   └── users
│       ├── dto
│       │   ├── post.dto.ts
│       │   ├── profile.dto.ts
│       │   └── user.dto.ts
│       ├── repository
│       │   ├── post.repository.ts
│       │   ├── profile.repository.ts
│       │   └── users.repository.ts
│       ├── users.controller.ts
│       ├── users.module.ts
│       └── users.service.ts
├── entity
│   ├── boards
│   │   └── board.entity.ts
│   └── users
│       ├── post.entity.ts
│       ├── profile.entity.ts
│       └── user.entity.ts
└── main.ts
```

우선 최종적인 프로젝트 트리는 위와 같다.
먼저 `domain` 폴더 하위에 모듈이 들어갈 `boards` 폴더를 생성해주고,
`nest g module boards`, `nest g controller boards`, `nest g service boards` 이 3개의 명령어로 기본적인 구조를 만들어 준다.

나는 전과 같이 Repository Pattern을 사용할 것이기 때문에 Service가 아닌 따로 Repository 파일을 만들어 DB에 접근하는 로직을 작성하려고 한다.

일단 먼저 Entity 파일과 DTO 파일을 만들어 보자

### boards.entity.ts, boards.dto.ts

```bash
Entity

import { Entity, Column, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';

@Entity({ name: 'boards' })
export class BoardEntity {
  @PrimaryGeneratedColumn()
  boardId: number;

  @Column()
  title: string;

  @Column()
  description: string;

  @Column()
  createAt: Date;
}
```

Board 모듈에서 DB에 저장될 컬럼들의 목록을 먼저 정의해준다.
id같은 경우는 물론 자동으로 생성되게끔 `PrimaryGenerateColumn` 데코레이터를 사용한다.

> PrimaryColumn을 사용시 id 컬럼을 자동으로 생성해 주지 않아 "Field 'id' doesn't have a default value" 라는 Error가 발생한다.

```bash
DTO

export class BoardDto {
  title: string;
  description: string;
  createAt: Date;
}

```

DTO 작성까지 완료 했으니 이제 Repository를 만들어보자

### boards.repository.ts

```bash
import { HttpException, HttpStatus, Injectable } from '@nestjs/common';
import { BoardEntity } from 'src/entity/boards/board.entity';
import { DataSource, Repository } from 'typeorm';
import { BoardDto } from '../dto/board.dto';
import { UsersRepository } from 'src/domain/users/repository/users.repository';

@Injectable()
export class BoardsRepository extends Repository<BoardEntity> {
  constructor(
    private dataSource: DataSource,
    private userRepository: UsersRepository,
  ) {
    super(BoardEntity, dataSource.createEntityManager());
  }

  async findAllBoard() {
    const boards = await this.find();
    return boards;
  }

  async createBoard(id: number, boardDto: BoardDto) {
    const user = await this.userRepository.findOneBy({ id });
    if (!user)
      throw new HttpException(
        `User Not Found. Cannot Create Post.`,
        HttpStatus.BAD_REQUEST,
      );

    const newPost = this.create({ ...boardDto, createAt: new Date(), user });
    return this.save(newPost);
  }

  async updateBoard(boardId: number, boardDto: BoardDto) {
    return await this.update({ boardId }, { ...boardDto });
  }

  async deleteBoard(boardId: number) {
    return await this.delete(boardId);
  }
}
```

이전에 작성했던 UsersRepository와 조금 다른점이 있다면, 게시글을 생성하는 과정에서 작성한 유저의 정보가 필요하기에 BoardsRepository에서 UserRepository를 사용해야 한다.
따라서, `BoardsRepository` 클래스의 생성자 부분에 UsersRepository를 넣어서 사용할 수 있게 만들어 준다.
(그냥`id`는 유저 아이디를 의미하고, `boardId`는 게시글 아이디를 의미한다.)
DB에 접근하는 로직을 작성했으니 이제 Service를 작성해보자

### boards.service.ts

```bash
import { Injectable } from '@nestjs/common';
import { BoardsRepository } from './repository/boards.repository';
import { BoardDto } from './dto/board.dto';

@Injectable()
export class BoardsService {
  constructor(private boardRepository: BoardsRepository) {}

  async findAllBoard() {
    return this.boardRepository.findAllBoard();
  }

  createBoard(userId: number, boardDto: BoardDto) {
    return this.boardRepository.createBoard(userId, boardDto);
  }

  async updateBoard(boardId: number, boardDto: BoardDto) {
    return await this.boardRepository.updateBoard(boardId, boardDto);
  }

  async deleteBoard(boardId: number) {
    return this.boardRepository.deleteBoard(boardId);
  }
}
```

Repository에서 작성한 로직을 그대로 가져다 쓰는것 외에는 특별한 점이 없다. 다음은 Controller이다.

### boards.controller.ts

```bash
import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  ParseIntPipe,
  Post,
  Put,
} from '@nestjs/common';
import { BoardsService } from './boards.service';
import { BoardDto } from './dto/board.dto';

@Controller('boards')
export class BoardsController {
  constructor(private boardService: BoardsService) {}

  @Get()
  async findAllBoard() {
    return await this.boardService.findAllBoard();
  }

  @Post(':id/post')
  createBoard(
    @Param(`id`, ParseIntPipe) userId: number,
    @Body() boardDto: BoardDto,
  ) {
    return this.boardService.createBoard(userId, boardDto);
  }

  @Put(':id')
  async updateBoard(
    @Param('id', ParseIntPipe) boardId: number,
    @Body() boardDto: BoardDto,
  ) {
    return await this.boardService.updateBoard(boardId, boardDto);
  }

  @Delete(':id')
  async deleteBoard(@Param('id', ParseIntPipe) boardId: number) {
    return this.boardService.deleteBoard(boardId);
  }
}
```

Controller에서 유의할 점은 id나 포스팅 내용, 수정내용을 어떻게 전달받을것인지인데, 나는 id값은 url parameter로, 내용은 Body로 받아오기로 하였다.

> ParseIntPipe는 메서드에서 받는 매개변수가 숫자인지 체크하는 파이프이다. 숫자가 아닐경우.
> {
> "statusCode": 400,
> "message": "Validation failed (numeric string is expected)",
> "error": "Bad Request"
> }
> 의 에러문구를 발생시킨다.

이제 Controller까지 작성을 완료했으니 Module에 등록해보자

### boards.module.ts / app.module.ts

```bash
boards

import { Module } from '@nestjs/common';
import { BoardsController } from './boards.controller';
import { BoardsService } from './boards.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { BoardEntity } from 'src/entity/boards/board.entity';
import { UserEntity } from 'src/entity/users/user.entity';
import { BoardsRepository } from './repository/boards.repository';
import { UsersRepository } from '../users/repository/users.repository';

@Module({
  imports: [TypeOrmModule.forFeature([BoardEntity])],
  controllers: [BoardsController],
  providers: [BoardsService, BoardsRepository, UsersRepository],
})
export class BoardsModule {}
```

```bash
app

import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersModule } from './domain/users/users.module';
import { UserEntity } from './entity/users/user.entity';
import { ProfileEntity } from './entity/users/profile.entity';
import { PostEntity } from './entity/users/post.entity';
import { BoardEntity } from './entity/boards/board.entity';
import { BoardsModule } from './domain/boards/boards.module';

@Module({
  imports: [
    UsersModule,
    BoardsModule,
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'localhost',
      port: 3306,
      username: 'template',
      password: 'template',
      database: 'nest_template',
      entities: [UserEntity, ProfileEntity, PostEntity, BoardEntity],
      synchronize: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

```

이제 실행해보면
`Object literal may only specify known properties, and 'user' does not exist in type 'DeepPartial<BoardEntity>'.`라는 에러가 발생한다.
쉽게 말하면 BoardEntity에 user가 없다는 말인데, 지금껏 우리가 위에서 작성한 코드에는 User Module과 연결하는 부분이 없다.
그 부분을 Entity에서 수정할 수 있는데, 다음과 같이 수정하자.

### boards.entity.ts 수정

```bash
import { Entity, Column, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { UserEntity } from '../users/user.entity';

@Entity({ name: 'boards' })
export class BoardEntity {
  // PrimaryColumn을 사용시 id 컬럼을 자동으로 생성해 주지 않아 "Field 'id' doesn't have a default value" 라는 Error가 발생한다.
  @PrimaryGeneratedColumn()
  boardId: number;

  @Column()
  title: string;

  @Column()
  description: string;

  @Column()
  createAt: Date;

  @ManyToOne(() => UserEntity, (user) => user.board)
  user: UserEntity;
}
```

추가된 부분은 최하단의 `@ManytoOne`부분이다. 여러개의 게시물이 유저 하나에 의해서 작성될 수 있으므로, 해당 데코레이터를 사용하여 `User`, `Board` 두 모델의 관계를 설정하는 부분이다.

`Board` 모델에서 작성했으니 이제 `User` 모델에서도 관계를 설정해줘야 한다.

### users.entity.ts 수정

```bash
import {
  Column,
  Entity,
  JoinColumn,
  OneToMany,
  OneToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { ProfileEntity } from './profile.entity';
import { BoardEntity } from '../boards/board.entity';

@Entity({ name: 'users' })
export class UserEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  username: string;

  @Column()
  password: string;

  @OneToOne(() => ProfileEntity)
  @JoinColumn()
  profile: ProfileEntity;

  @OneToMany(() => BoardEntity, (board) => board.user)
  board: BoardEntity[];
}
```

`Board` 모델과 반대로 한명의 유저가 여러개의 게시물을 작성할 수 있으므로, `@OnetoMany` 데코레이터를 이용해준다.
그리고 `Board` 모델에서 `UserEntity`를 사용하므로 모듈에도 등록해줘야 한다.

### boards.module.ts 수정

```bash
import { Module } from '@nestjs/common';
import { BoardsController } from './boards.controller';
import { BoardsService } from './boards.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { BoardEntity } from 'src/entity/boards/board.entity';
import { UserEntity } from 'src/entity/users/user.entity';
import { BoardsRepository } from './repository/boards.repository';
import { UsersRepository } from '../users/repository/users.repository';

@Module({
  imports: [TypeOrmModule.forFeature([BoardEntity, UserEntity])],
  controllers: [BoardsController],
  providers: [BoardsService, BoardsRepository, UsersRepository],
})
export class BoardsModule {}

```

실행시, 에러없이 잘 작동하는 것을 볼 수 있다.

---

**reference**
[Nest js 공식 문서](https://docs.nestjs.com/techniques/database)
[Type Orm 공식 문서](https://typeorm.io/)
