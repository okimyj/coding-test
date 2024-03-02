function solution(s) {
    var answer = '';
    const strArr = s.split(' ');
    for(let i=0; i<strArr.length; ++i){
        strArr[i] = strArr[i].toLowerCase();
        const firstChar = strArr[i].charAt(0).toUpperCase();
        strArr[i] = firstChar + strArr[i].slice(1);
    }
    return strArr.join(' ');
}