function solution(numbers, target) {
    var answer = 0;
    const calc = (sum, i)=>{
        if(i === numbers.length-1){
            if(sum === target)
                ++answer;
            return;
        }
        ++i;
        calc(sum+numbers[i], i);
        calc(sum+numbers[i]*-1, i);
    };
    calc(numbers[0], 0)
    calc(numbers[0]*-1, 0)
    return answer;
}