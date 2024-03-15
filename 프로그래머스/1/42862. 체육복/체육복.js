function solution(n, lost, reserve) {
    const filteredLost = lost.filter((number)=>!reserve.includes(number))
    const filteredReserve = reserve.filter((number)=>!lost.includes(number))
    filteredLost.sort()
    
    var answer = n - filteredLost.length;
    const borrowUniform = (number)=>{
        const idx = filteredReserve.indexOf(number);
        if(idx != -1){
            filteredReserve.splice(idx,1);
            return true;
        }
        return false;
    }
    filteredLost.forEach((number)=>{
        if(borrowUniform(number-1) || borrowUniform(number+1))
            ++answer;
    })
    return answer;
}