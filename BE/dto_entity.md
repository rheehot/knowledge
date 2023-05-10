![차이점](https://velog.velcdn.com/images/cnffjd95/post/c1750f27-d90e-450c-95dc-c9bfa915dd1c/image.png)

앞서 Nest js를 학습하며 공부할점과 의문점들이 꽤나 많이 생겼었는데 그중 하나인 DTO와 Entity의 차이점에 대해 공부해보자

## 📌 DTO?

DTO란 Data Trnasfer Object의 약자로 계층간 데이터 교환을 위하여 사용되는 객체이다.
여기서 말하는 계층이란 View, Controller, Service등을 말한다. 뿐만 아니라 클라이언트에서 서버로 데이터를 전송할때도 사용되고, 그 데이터를 객체로 변환하는데 사용된다.

따라서, 클라이언트로부터 받은 데이터를 서버가 처리하기 전에 이 **데이터가 유효한지에 대한 데이터 유효성 검사**를 실시하는 역할을 수행한다.

Nest js에서 사용하는 방법은 아래와 같다.

```bash
creatDto.ts

import { IsNumber, IsString } from 'class-validator';

export class CreateBoardDto {

  @IsString()
  title: string;

  @IsString()
  description: string;

  @IsNumber()
  id: number;
}
```

코드와 같이 클라이언트로부터 전송받을 데이터 title, description, id의 형식을 명시한다. 이렇게 생성한 dto 파일은 controller에서 import하여 사용한다.

```bash
@Post()
create(@Body() createBoardDto: CreateBoardDto) {
    return this.boardService.create(createBoardDto);
  }
```

Post요청으로 들어오는 데이터는 `CreateBoardDto`가 명시한 형식이어야 하고, 이 데이터를 boardService에서 정의한 create라는 메서드를 통하여 가공한다.

## 📌 Entity?

[Entity 포스팅](https://velog.io/@cnffjd95/Type-Orm-Entity-Repository)

이전 포스팅에서 다루었듯이, DB 테이블과의 연결을 위하여 테이블에서 생성될 인스턴스들을 명시해둔 것이다.
이렇게 생성된 Entity는 Repository를 통하여 DB와 통신하게된다.

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

DTO와 비슷하게 생겼지만, 연결/생성할 DB 테이블의 컬럼을 미리 명시한 것이다.

## ❗️ 차이점

얼핏 보면 DTO와 다를바가 없어보이지만 통신해야하는 목적지가 다르다.
DTO는 클라이언트에서 서버, Controller에서 Service 등 계층간의 통신을 위해 사용되는 것이라면, Entity는 앱과 DB와의 통신을 위해 사용된다는 차이점이 있다.

최상위 사진을 보면 조금 더 직관적으로 사용처를 알 수 있다.

사실 이쯤되면 나는 굳이 왜 두개를 저렇게 분리해서 사용하는가에 대한 의문점이 들었다.
조금 더 알아본 결과, 몇가지 이유가 존재했다.

- DB 보안
  Entity를 사용자에게 노출하게 된다면, DB 테이블의 구조 자체를 노출하는 것이기 때문에 보안상으로 좋지 않다.

- 값 변경
  Entity의 값이 변하면 연결되어 있는 DB의 값 또한 변경되고, 그와 연결되어있는 다른 로직들에게 변화가 생길수밖에 없다. (특히나 View 레이어는 데이터의 변경이 매우 잦다.)

- **_관심사의 분리_**
  결정적으로 DTO는 Presentation 계층에 속하여 **데이터 전송**을 목적으로 하는 객체이고, Entity는 Business 계층에 속하여 **DB와 연결하는 비즈니스 로직**을 담은 비즈니스 도메인 영역의 일부이다.
