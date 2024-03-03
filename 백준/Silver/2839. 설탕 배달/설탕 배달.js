const readline = require("readline");
const rl = readline.createInterface({
  input:process.stdin,
  output:process.stdout
});
rl.on("line", (line)=>{
  let input = Number(line);
  let result = 0;

  while( input > 0){
    if(input%5===0){
      result += input/5;
      break;
    }
    input -=3;
    ++result;
    if(input < 0)
    {
      result = -1;
      break;
    }
  }
  console.log(result);
  rl.close();
});