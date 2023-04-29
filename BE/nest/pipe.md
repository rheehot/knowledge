<a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="200" alt="Nest Logo" /></a>

## 📌 Pipe?

- `@Injectable()` 데코레이터로 주석이 달린 클래스를 말한다.

- Data Transformation과 Data Validation을 위해 사용.

- 컨트롤러 경로 처리기에 의해 처리되는 인수에 대하여 작동

![파이프](https://velog.velcdn.com/images/cnffjd95/post/fc8b0a39-21e1-407a-8386-a3536e6ef96f/image.png)
메서드가 호출되기 직전, 파이프를 삽입하고, 파이프는 메서드로 향하는 인수를 수신하고 작동한다.

### Data Transformation

입력 데이터를 원하는 형식으로 변환하는 것
만약 숫자형을 원하는데 문자열로 온다면 파이프에서 자동으로 숫자형으로 바꾸어 준다.

> string "7" => Integer 7

### Data Validation

데이터 유효성 체크이다.
입력 데이터를 평가하고, 유효한 경우, 그대로 전달한다. 만약 유효하지 않다면 예외를 발생시킨다.

> 비밀번호에 대문자와 특수기호가 없다면 에러를 발생시킨다.

### 사용법

#### 1. Handler-Level

핸들러 레벨에서 `@UsePipes()` 데코레이터를 이용해서 사용한다.
모든 파라미터에 적용됨.

```bash
@Post()
@UsePipes(pipe)
createBoard(
	// 파라미터인 title과 description 모두에 대하여 적용된다.
	@Body('title') title,
    @body('description') description
){}
```

#### 2. Parameter-Level

파라미터 레벨의 파이프이다
특정한 파라미터에게만 적용된다.

```bash
@Post()
createBoard(
	// ParameterPipe가 사용된 title 파라미터에 대하여만 적용된다.
	@Body('title', ParameterPipe) title,
    @body('description') description
){}
```

#### 3. Global-Level

어플리케이션 레벨의 파이프.
클라이언트에서 들어오는 모든 요청에 적용된다. 최상위 단계인 `main.ts`에서 사용

```bash
async function bootstrap(){
	const app = await NestFactory.create(AppModule);
    app.useGlobalPipes(GlobalPipes);
    await app.listen(3000);
}
bootstrap();
```

## Pipe를 이용한 유효성 체크

### 필요 모듈

```bash
# class-validator
npm install class-validator --save
# class-transformer
npm install class-transformer --save
```

### 파이프 생성하기

src/boards/dto/create-board.dto.ts

```bash
import { IsNotEmpty } from 'class-validator';

export class CreateBoardDto {
  // 유효성 체크 추가
  @IsNotEmpty()
  title: string;

  @IsNotEmpty()
  description: string;
}

```

src/boards/boards.controller.ts

```bash
@Post()
  // 유효성 검사를 위한 핸들러 레벨 파이프
  @UsePipes(ValidationPipe)
  createBoard(@Body() createBoardDto: CreateBoardDto): Board {
    return this.boardsService.createBoard(createBoardDto);
  }
```
