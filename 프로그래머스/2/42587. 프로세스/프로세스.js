function solution(priorities, location) {
    let maxPriority = Math.max(...priorities);
    const prioritiesWithKey = priorities.map((el, index)=>({p:el, key:index}));
    // console.log("maxPriority : ", maxPriority, "prioritiesWithKey : ", prioritiesWithKey);
    let order = 1;
    
    while(prioritiesWithKey.length){
        const process = prioritiesWithKey.shift();
        const isBigPriority = prioritiesWithKey.some(el => el.p > process.p);
        if(isBigPriority){
            prioritiesWithKey.push(process);
        }
        else
        {
            priorities.splice(process.key);
            maxPriority=Math.max(...priorities)
            if(process.key === location)
                return order;
            ++order;
        }
        
    }
    
    // prioritiesWithKey.sort((a, b) => b.p - a.p);
    // console.log("prioritiesWithKey : ", prioritiesWithKey);
    // var answer = prioritiesWithKey.findIndex((el)=>el.key === location) +1;
    return answer;
}