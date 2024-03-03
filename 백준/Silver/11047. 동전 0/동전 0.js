const rl = require("readline").createInterface({ input: process.stdin });
let coinKindNum = undefined,
  target = undefined;
let coinKind = [];
rl.on("line", (line) => {
  if (coinKindNum === undefined) {
    [coinKindNum, target] = line.split(" ").map(Number);
  } else {
    --coinKindNum;
    const coinUnit = Number(line);
    if (coinUnit <= target) coinKind.push(Number(line));
    if (coinKindNum === 0) {
      let totalNeedNum = 0;
      for (let i = coinKind.length - 1; i >= 0; --i) {
        const coinNum = Math.floor(target / coinKind[i]);
        target -= coinNum * coinKind[i];
        totalNeedNum += coinNum;
        if (target === 0) break;
      }
      console.log(totalNeedNum);
      rl.close();
      return;
    }
  }
});
