// catch 문 연결
async function test3() {
  console.log("test3 start");
  throw new Error("New Error in function test3");
}

function do_test3() {
  console.log("main start");
  test3().catch((err) => {
    console.error("catch from main");
    console.error(err);
    return console.log("main end in catch");
  });
  return console.log("main end");
}

do_test3();
