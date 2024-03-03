const rl = require("readline").createInterface({ input: process.stdin });

const unit = [500, 100, 50, 10, 5, 1];
rl.on("line", (line) => {
  let target = 1000 - Number(line);
  let totalCoin = 0;
  for (let i = 0; i < unit.length; ++i) {
    const coinNum = Math.floor(target / unit[i]);
    totalCoin += coinNum;
    target -= coinNum * unit[i];
  }

  console.log(totalCoin);
  rl.close();
});