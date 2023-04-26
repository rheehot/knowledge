![](https://velog.velcdn.com/images/cnffjd95/post/1b706898-1c38-4141-b8fc-0ef71cb511d5/image.png)

## 1. I/O

Input/Output으로 입/출력을 의미한다.
I/O에서 발생하는 시간은 CPU를 사용하지 못하고 대기하는 시간이다.
**따라서, 입출력이 완료될때까지 CPU는 대기하고, 어플리케이션 실행속도 또한 느려지게 되는 비효율적인 현상이 생긴다.**

> 이때, 입출력이 완료되기 전 CPU가 대기하는 상태를 `blocking`상태라고 한다.

## 2. Blocking I/O

서론에서 얘기한 입출력이 완료되기 전까지 CPU가 대기하는 방식을 `bloking I/O`라고 한다.

![블로킹](https://velog.velcdn.com/images/cnffjd95/post/9e23a16c-3ce6-4d6b-af7f-6a56d3be136e/image.png)

위 사진에서 보는 것처럼, 어플리케이션에서 입출력 요청을 보낸뒤 완료된 데이터를 수신 할 때까지 대기한다.
즉, 입출력 작업 완료 전까지 어플리케이션은 다른 작업을 실행하지 못한다는 것이다.

## 3. Non-Blocking I/O

Blocking I/O 모델에서 하나의 입출력 작업 완료 전까지 다른 작업을 못한다는 것은 어플리케이션의 성능에 큰 영향을 미친다.
이것을 blocking 하지 않는 형태의 입출력방식을 통해 해결하는데 바로 `Non-blocking I/O`이다.

![논블로킹](https://velog.velcdn.com/images/cnffjd95/post/b8a8e3f8-a7b0-4724-b44f-456a827066c8/image.png)

Non-blocking I/O는 어플리케이션에서 입출력 요청을 보내는 순간 결과 메시지를 반환한다.(입력 데이터가 없다면 에러 메시지 반환)
또한, 제어권을 넘겨주지 않기 때문에 결과 메시지를 받은 어플리케이션은 즉시 작업을 이어서 실시 할수 있다.
최종적으로 입력 데이터가 발생하면, 유저에게 결과 데이터를 리턴하게 된다.

앞선 Blocking I/O와 비교해 보면 확실히 blocking 시간을 줄일수 있다는 점에서 효율적이다.

**하지만 Blocking I/O 보다 시스템 호출이 반복적으로 이루어지기 때문에 자원낭비가 발생한다.**
