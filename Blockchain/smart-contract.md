![](https://velog.velcdn.com/images/cnffjd95/post/83e08167-9989-4d6e-b3b7-232d522a5d2a/image.png)

최근 집 계약 건으로 부동산을 몇번 방문 할 일이 있었다.
항상 부동산을 갈때마다 생각하는 부분이 "굳이 부동산 중개업자를 통해서 집거래를 해야하는건가...그냥 세입자/차입자끼리 만나서 거래하면 훨씬 간단하고 편하지 않나?" 였다.

오늘 포스팅할 주제가 바로 이것을 해결한 스마트 컨트랙트이다.

### 스마트 컨트랙트란?

디지털 자산(데이터)의 특성 중 하나가 **복제가 쉽다는 것**이다.
따라서, 아무나 함부로 조작할수 없도록 신뢰할수 있는 기관을 거쳐 거래를 이행하도록 한다. 자연스럽게 이 자산(데이터)를 거래하는데 있어서 거래 당사자들이 아닌 제 3자(또는 기관)에게 보안과 무결성을 의존할수밖에 없고 비용 또한 부담해야 한다.

스마트 컨트랙트는 위와 같은 단점을 해결하고자 개발되었다.

> **계약의 내용과 실행 조건을 사전에 설정한 후, 조건이 충족되었을때 자동으로 거래를 이행해 주는 시스템**.

특정 조건이 충족되지 않으면 실행되지 않기에, 거래를 하는 당사자들이 서로가 어떤 사람인지, 신뢰성이 높은 사람인지 등을 고려할 필요가 없다. 따라서 거래 중개인도 필요가 없다.
여기서 고려해야 할 점이 있다.
![](https://velog.velcdn.com/images/cnffjd95/post/832cbaa4-aac8-4a24-89e4-c87079b9e806/image.png)

위에서 특정한 조건을 기준으로 계약을 이행한다고 했다.
그렇다면 이 조건은 모든 계약 당사자들이 신뢰할수 있고 개방적인 데이터베이스를 기반으로 할것이다. 이 조건에 정말 딱 알맞는 환경이 바로 블록체인이다.

스마트 컨트랙트로써 거래가 이행되면 해당 거래내역이 블록체인에 저장된 분산원장의 모든 노드에 공유된다.
따라서 모든 참여자가 해당 거래 내역을 확인 할 수 있고, **데이터 위변조가 불가능**하므로 스마트 컨트랙트의 거래 결과 또한 **신뢰도가 매우 높다.**

스마트 컨트랙트는 다음과 같은 특징을 가진다.

- 관측가능성
  서로의 계약 이행 가능성을 관찰하거나 성과입증이 가능해야한다.

- 검증가능성
  계약을 이행하거나 위반할 경우, 계약 당사자들이 알 수 있어야 한다.

- 프라이버시
  계약 내용은 당사자들만이 알 수 있어야 한다.

- 강제가능성
  계약이 이뤄질 수 있도록 구속력이 있어야 한다.

이제 스마트 컨트랙트의 장단점에 대해 알아보자

### 장점

- 보안/신뢰성
  계약은 블록체인 네트워크에서 실행되고 거래 내역은 공유원장에 저장되기 때문에 안전한 계약을 이행할수 있다..(위변조시 모든 블록의 데이터를 조작해야 하기 때문에 사실상 불가능하다.)

- 경제성
  거래 당사자들이외이 제 3의 중개인이 필요없기에 비용과 시간이 절감된다.

- 자율성
  거래 당사자들이 계약에 대한 권한과 통제성을 가진다.

### 단점

- 블록체인 환경에서 계약이행시 외부의 정보가 필요할때 스스로 가져오지 못한다.
  블록체인 외부 데이터를 가져올때 잘못된 데이터를 입력할수있다. 또한 데이터를 가져오기 위해 제3자에게 의존하게 된다면 신뢰도 이슈가 발생한다.

- 배포 이후 수정이 불가하다.
  스마트 컨트랙트 코드가 블록체인상에 올라간 후에는 수정이 불가능하여 새롭게 배포하고 해킹을 방지하기 위해 기존에 사용하던 스마트 컨트랙트는 사용할 수 없도록 해야 한다.
