function solution(s){
    // s = s.toLowerCase().split('')
    // const pCount = s.filter((c) => c === 'p').length
    // const yCount = s.filter((c) => c === 'y').length
    s = s.toLowerCase();
    let pCount = 0;
    let yCount = 0;
    for(let i =0; i<s.length; ++i){
        if(s[i] === 'p')
            ++pCount;
        if(s[i] === 'y')
            ++yCount;
    }
    return pCount === yCount;
}