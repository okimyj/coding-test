const rl = require("readline").createInterface({ input: process.stdin });
let inputNum = 0;
rl.on("line", (line) => {
  const [canUseDay, period, holidays] = line.split(" ").map(Number);
  if (line === "0 0 0") {
    rl.close();
    return;
  }
  ++inputNum;
  const fullUseDaysNum = Math.floor(holidays / period);
  let totalDays = fullUseDaysNum * canUseDay;
  let remainDays = holidays - fullUseDaysNum * period;
  totalDays += remainDays < canUseDay ? remainDays : canUseDay;

  console.log(`Case ${inputNum}: ${totalDays}`);
});
