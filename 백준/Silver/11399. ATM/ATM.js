const rl = require("readline").createInterface({ input: process.stdin });
let inputNum = undefined;

rl.on("line", (line) => {
  if (inputNum === undefined) {
    inputNum = Number(line);
  } else {
    const times = line.split(" ").map(Number);
    times.sort((a, b) => a - b);

    let prevSum = times[0];
    let total = prevSum;
    for (let i = 1; i < times.length; ++i) {
      prevSum = prevSum + times[i];
      total += prevSum;
    }
    console.log(total);
    rl.close();
  }
});
