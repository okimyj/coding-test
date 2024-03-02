function solution(progresses, speeds) {
    var answer = [];
    const workDays = progresses.map((el,i)=>Math.ceil((100-el) / speeds[i]));
    console.log("workDays : ", workDays);
    let prevMaxDay = workDays[0];
    let deployNum = 0;
    for(let i=0; i<workDays.length; ++i){
        console.log("deployNum : ", deployNum, " prevMaxDay : " , prevMaxDay, " workDays[i] : " , workDays[i])
        if(prevMaxDay >= workDays[i]){
            ++deployNum;
        }else{
            console.log("anwerPush!! deployNum : ", deployNum);
            answer.push(deployNum);
            deployNum = 1;
            prevMaxDay = workDays[i];
        }
    }
    answer.push(deployNum);
    
    return answer;
}