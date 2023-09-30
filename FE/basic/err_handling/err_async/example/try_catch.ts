// await를 사용하지 않은 try/catch

async function test() {
  console.log("Do Test!");
  throw new Error("New Error in function test");
}

function do_test() {
  try {
    console.log("try start");
    test();
    console.log("try end");
  } catch (err) {
    console.error("catch err in main");
    console.log(err);
    return console.log("main end in catch");
  }
  return console.log("main end");
}
do_test();
