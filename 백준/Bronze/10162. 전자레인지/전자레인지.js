const rl = require("readline").createInterface({ input: process.stdin });

const unit = [5 * 60, 1 * 60, 10];
rl.on("line", (line) => {
  let time = Number(line);
  const result = [0, 0, 0];
  for (let i = 0; i < unit.length; ++i) {
    result[i] = Math.floor(time / unit[i]);
    time -= result[i] * unit[i];
  }

  console.log(time !== 0 ? -1 : result.join(" "));
  rl.close();
});