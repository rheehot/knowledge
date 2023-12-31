> 프론트엔드분야를 공부하며 생길수 있는 의문점과 가져야할 지식에 대하여 공부하는 바를 적은 글입니다.

## 1. 비동기 처리의 단점

- 비동기 처리는 하나의 태스크가 완료되지 않아도 다른 태스크를 실행할 수 있다는 점에서 효율적이지만, 콜백지옥에 빠질수 있다는 단점이 있다.
  > 함수의 매개변수로 넘어가는 콜백함수가 반복되는 현상을 일컫는다.

```
async(1, function() {
	async(2, function(){
		async(3, function(){
        	async(4, function(){
            	console.log("콜백지옥");
                })
             })
          })
        })
```

- 위의 코드처럼 함수의 매개변수로 함수가 계속해서 반복되면 가독성도 좋지 않을 뿐더러, 코드를 수정하기도 힘들다.

- 비동기 처리에서 이것을 극복하기 위해 **Promise**라는 개념을 도입하였다.

## 2. Promise

- promise는 자바스크립트의 비동기 처리에 사용되는 객체이다.

- 총 3가지의 상태를 가지는데,
  - 대기 (Pending)
    - 비동기 처리가 아직 수행되지 않은 상태
  - 완료 (Fulfilled)
    - 비동기 처리가 성공한 상태
      - 이 경우, `resolve` 함수를 호출하여 fulfilled 상태로 변경된다.
  - 실패 (Rejected)
    - 비동기 처리가 실패한 상태
      - 이 경우, `reject` 함수를 호출하여 rejected 상태로 변경된다.

```
const example = () => new Promise((resolve, reject) => {
	let a = "promise";
    if(a=="promise"){
    	resolve("Success!")
    } else{
	    reject("reject")
    }
})

promise().then((message) => {
	console.log(`then에서는 ${message}`)
}) .catch((message) => {
	console.log(`catch에서는 ${message}`)
})
```

- 코드에서 볼수 있듯이, 비동기 처리가 성공적으로 완료되면 then으로 넘어가 resolve를 실행하고, 실패하면 catch로 넘어가 reject를 실행한다.
  > then, catch는 promise의 후속처리 메서드로, 둘다 promise를 반환한다.
