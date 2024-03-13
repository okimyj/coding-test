function solution(t, p) {
    let count = 0;
    for(let i=0; i<=t.length-p.length; ++i){
        const value = t.slice(i, p.length + i);
        if(+value <= +p)
            ++count;
    }
    return count;
}
