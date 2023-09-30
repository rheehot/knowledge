// await 이용 처리

async function test2() {
  console.log("test2 start");
  throw new Error("New Error in function test");
}

async function do_test2() {
  try {
    console.log("try start");
    await test2();
    console.log("try end");
  } catch (err) {
    console.error("catch from main");
    console.error(err);
    return console.log("main end in catch");
  }
  return console.log("main end");
}

do_test2();
