const rl = require("readline").createInterface({ input: process.stdin });
rl.on("line", (line) => {
  const numbers = line.split(" ").map(Number);

  const countMap = numbers.reduce((count, num) => {
    count.set(num, (count.get(num) || 0) + 1);
    return count;
  }, new Map());
  
  const maxCount = [...countMap.entries()].reduce((a, b) => (a[1] > b[1] ? a : b));
  let prize = 0;
  if (maxCount[1] === 3) {
    prize = 10000 + maxCount[0] * 1000;
  } else if (maxCount[1] === 2) {
    prize = 1000 + maxCount[0] * 100;
  } else if (maxCount[1] === 1) {
    prize = Math.max(...numbers) * 100;
  }
  console.log(prize);
  rl.close();
  process.exit();
});
