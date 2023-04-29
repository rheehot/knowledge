<a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="200" alt="Nest Logo" /></a>

## DTO?

- Data Transfer Object의 약자로 계층간 데이터 교환을 위한 객체이다

- 쉽게 말해서 DB에서 데이터를 얻어 Controller나 Service로 보낼때 사용되는 객체를 얘기한다.

> 한마디로 데이터가 네트워크를 통해 전송되는 방법을 정의하는 객체이다

- 주로 `interface` 또는 `class`를 통하여 정의된다 (Nest 공식문서에는 class 사용 권장)

### 사용이유

- 데이터 유효성을 체크하는데 효율적이다.
  데이터 유효성 체크란 사용자로 부터 값을 입력받을 때 정확한 값을 입력받는지 확인하는 것을 말한다.

### 예제

Nest js에서 게시물 생성에 사용되는 DTO 예제를 들어보자
[Nest js 예제](https://github.com/augusstt06/tutorial_nest)

우선 dto를 사용하기 위해 폴더를 생성해보자

```bash
src/
│
├── /boards
│  │
│  └── /dto
│  │   └── create-board.dto.ts
│  │
│  ├ board.controller.ts
│  ├ board.model.ts
│  ├ board.module.ts
│  └ board.service.ts
│
├── app.module.ts
│
│
└── main.ts

```

현재 내 프로젝트의 폴더구조이다.
게시물 생성에 사용되는 dto를 만들것이기 때문에 `/board`아래에 dto폴더를 생성하였다.

dto 파일을 생성할때 class 또는 interface를 사용할 수 있지만, class는 interface와 다르게 런타임에서 작동하기 때문에 파이프 같은 기능을 이용할 때 더 유용하다.
따라서 class로 작성하도록 하겠다.

```bash
src/boards/dto/craete-board.dto.ts

export class createBoardDto {
  title: string;
  description: string;
}
```

요렇게 생성한 dto를 이제 Controller와 Service에 적용해야 한다.

- src/boards/boards.service.ts

```bash
* 변경 전
createBoard(title: string, description: string){
    const board: Board = {
      id: uuid(),
      title,
      description,
      status: BoardStatus.PUBLIC,
    };
    this.boards.push(board);
    return board;
  }
}
```

```bash
* 변경 후
  createBoard(createBoardDto: CreateBoardDto) {
    // 생성한 dto 사용
    const { title, description } = createBoardDto;

    const board: Board = {
      id: uuid(),
      title,
      description,
      status: BoardStatus.PUBLIC,
    };
    this.boards.push(board);
    return board;
  }
}

```

이전에 만들었던 createBoard 함수에서 사용되던 title, description 파라미터는 생성한 dto에 있으므로 두 파라미터를 dto를 사용하여 변경한다.

Service를 수정하였으니 이제 Controller를 변경해보자

- src/boards/boards.controller.ts

```bash
* 변경 전
@Post()
  createBoard(
    @Body('title') title: string,
    @Body('description') description: string,
  ): Board {
    return this.boardsService.createBoard(title, description);
```

```bash
@Post()
  createBoard(@Body() createBoardDto: CreateBoardDto): Board {
    return this.boardsService.createBoard(createBoardDto);
  }
```

마찬가지로 전에 파라미터로 사용되던 title과 description를 생성한 dto로 변경하였다.
