const rl = require("readline").createInterface({ input: process.stdin });
let inputNum = undefined;

rl.on("line", (line) => {
  if (inputNum === undefined) {
    inputNum = Number(line);
  } else {
    const arr = line.split("");
    if (arr[0] === ")") console.log("NO");
    else {
      const check = [];
      for (let i = 0; i < arr.length; ++i) {
        if (arr[i] === "(") {
          check.push(arr[i]);
        } else {
          if (check[check.length - 1] === "(") check.pop();
          else {
            check.push(arr[i]);
            break;
          }
        }
      }
      console.log(check.length > 0 ? "NO" : "YES");
    }
    --inputNum;
    if (inputNum === 0) rl.close();
  }
});
