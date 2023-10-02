import test from "./test_module";
import "./index.css";
// import cat from "./cat.png";

// console.log(test);

window.addEventListener("DOMContentLoaded", () => {
  const el = document.querySelector("#app");
  el.innerHTML = `
    <h1>${test}</h1>
    `;
});
