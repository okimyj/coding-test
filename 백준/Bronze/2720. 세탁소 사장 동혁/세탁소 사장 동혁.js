const rl = require("readline").createInterface({ input: process.stdin });
let inputNum = undefined;
const unit = [25, 10, 5, 1];
rl.on("line", (line) => {
  if (inputNum === undefined) {
    inputNum = Number(line);
  } else {
    const result = Array(unit.length).fill(0);
    let target = Number(line);
    for (let i = 0; i < unit.length; ++i) {
      result[i] = Math.floor(target / unit[i]);
      target -= result[i] * unit[i];
      if (target === 0) break;
    }
    console.log(result.join(" "));
    --inputNum;
    if (inputNum === 0) rl.close();
  }
});
