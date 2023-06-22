## 📌 NoSql

Not Only SQL의 약자로, 관계형데이터베이스가 아닌 형태의 데이터 저장기술이다.

기존의 관계형 데이터베이스의 단점인 대량의 비정형 데이터를 저장/관리 하는데 부적합하다는것과 여러 컴퓨터가 연결되어 하나의 시스템을 구성하는 클러스터 환경에서 비효율적이라는것을 해결하고자 고안되었다.

간단한 특징과 장단점을 먼저 살펴보자

### 특징

- 데이터간의 관계를 정의하지 않음.

- 관계형 데이터베이스에 비하여 많은 양의 데이터를 저장 가능.

- 분산형 구조.

- 테이블들의 스키마가 유동적이다.

이 있다.

### 장점

- 가변적인 구조로 데이터 저장 가능

- 데이터 모델의 유동적 변화 가능

- 관계형 데이터 베이스보다 저렴한 비용으로 데이터 분산/병렬 처리 가능

### 단점

- 데이터 일관성이 보장되지 않음.

- 충분한 메모리가 필요하다.

## NoSQL의 종류

데이터를 저장하는 방식에 따라 NoSql은 여러가지 종류로 나뉜다.

### key - value DB

![](https://velog.velcdn.com/images/cnffjd95/post/bcbb7c2b-f26b-45bd-a8be-f9f8fde516fe/image.png)

가장 기본적인 패턴으로, key 값과 value 값을 하나의 쌍으로 저장한다.
구조 자체가 단순하기에 속도가 빠르며, 데이터 분산 저장시 유용하다.
특징으로는,

- key 값은 고유한 값이어야 한다.

- 테이블간 관계정의가 없으므로 RDB의 foreign key가 필요없다

- value에는 모든 데이터 타입을 허용한다.

`Redis` 가 이 타입에 해당한다.

### Wide - Column DB

![](https://velog.velcdn.com/images/cnffjd95/post/2adcee61-ad13-4954-b667-326d2f36e17e/image.png)

위의 key-value에서 조금더 확장된 방식이다. 각각의 행마다 다른 스키마 값과 수를 가질 수 있다.
또한, key에 할당된 value 안에 위 사진처럼 Column과 value가 조합된 필드가 오는데 이것을 `Column Family` 라고 한다.
위 사진처럼 key값인 유저의 이름마다 가지는 스키마의 값과 수가 각각 다른것을 확인 할 수 있다.

### Document DB

![](https://velog.velcdn.com/images/cnffjd95/post/79a19bb3-9612-4391-82a0-0a6ca40be140/image.png)
데이터를 저장할때 key-value의 형태의 JSON, XML 등의 document타입으로 저장된다.

- 값 저장 전에는 스키마를 별도로 지정하지 않으며, document가 스키마가 된다.

- 각각의 document 별로 다른 필드를 가질 수 있으므로, 데이터관리시 주의필요

대표적으로 `Mongo DB` 가 이 유형에 속한다.

### Graph DB

![](https://velog.velcdn.com/images/cnffjd95/post/5c00c7ec-20e5-477b-9379-91a4ae95315c/image.png)

데이터를 노드로 표현하고, 노드 사이의 관계를 엣지(화살표)로 표현한다.
그림처럼 간단하고 직관적인 데이터 모델을 가진다.
