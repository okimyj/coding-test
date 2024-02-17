function solution(t, p) {
    const pNum = Number(p);
    const pLen = p.length;
    let count = 0;
    for(let i=0; i<t.length; ++i){
        if(i > t.length - pLen)
            break;
        const value = Number(t.substring(i, i+pLen));
        console.log(value);
        if(value <= pNum)
            ++count;
    }
    return count;
}