function solution(array, commands) {
    var answer = [];
    commands.map(([start, end, index])=>{
        const sorted = array.slice(start-1,end).sort((a, b)=>a-b);
        answer.push(sorted[index-1]);
    });
    
    
    return answer;
}