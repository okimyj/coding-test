function solution(participant, completion) {
    const map = new Map();
    for(let i=0; i<completion.length; ++i){
        map.set(completion[i], (map.get(completion[i])|| 0) +1);
    }
    for(let i=0; i<participant.length; ++i){
        const getNum = map.has(participant[i]) ? map.get(participant[i]) : 0;
        if(getNum > 0){
            map.set(participant[i], getNum-1);
        }
        else
            return participant[i];
    }
}