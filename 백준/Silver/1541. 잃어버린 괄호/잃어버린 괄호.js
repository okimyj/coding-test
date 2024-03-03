const rl = require("readline").createInterface({ input: process.stdin });
rl.on("line", (line) => {
  const array = line.split(/([(\+)(\-)])/);
  // const newArray = [];
  let isOpen = false;
  let sum = 0;
  while (array.length) {
    if (array[0] === "-") {
      if (isOpen) {
        isOpen = false;
        // newArray.push(")");
      }
      isOpen = true;
      array.shift();
      // newArray.push(array.shift());
      // newArray.push("(");
    } else if (array[0] === "+") {
      array.shift();
      // newArray.push(array.shift());
    } else {
      const num = Number(array.shift());
      if (isOpen) sum -= num;
      else sum += num;
      // newArray.push(num);
    }
  }
  // if (isOpen) newArray.push(")");
  // console.log(newArray.join(""), " = ", sum);
  console.log(sum);
  rl.close();
});
