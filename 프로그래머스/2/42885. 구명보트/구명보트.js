function solution(people, limit) {
    const sorted = people.sort((a, b)=> b-a);
    var answer = 0;
    for(let i=0; i<people.length; ++i){
        if(sorted.length <= i)
            break;
        const first = sorted[i];
        const remain = limit - first;
        if(remain > 0 && sorted.length && remain >= sorted[sorted.length-1]){
            sorted.pop();
        }
        ++answer;
    }
    // while(sorted.length){
    //     const first = sorted.shift();
    //     const remain = limit - first;
    //     if(remain > 0 && sorted.length && remain >= sorted[sorted.length-1]){
    //         sorted.pop();
    //     }
    //     ++answer;
    // }
    return answer;
}