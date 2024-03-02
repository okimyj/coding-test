function solution(n, words) {
    var answer = [];
    const set = new Set();
    let prevChar = '';
    for(let i =0; i<words.length; ++i){
        // console.log(words[i], " prev : " , prevChar, " i : " , i)
        if(set.has(words[i]) || words[i].length <= 1 || (prevChar && words[i].charAt(0) !== prevChar)){
            return [i%n+1, Math.ceil((i+1)/n)];
        } else{
            set.add(words[i]);
            prevChar = words[i].charAt(words[i].length -1)
        }
    }

    return [0,0];
}