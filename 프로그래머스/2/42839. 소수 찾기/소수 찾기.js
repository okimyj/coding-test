// 소수 : 1과 자신만을 약수로 가지는 수.
const isPrime = (n)=>{
    if(n <= 1)
        return false;
    for(let i=2; i<=Math.sqrt(n); ++i){
        if(i != n && n%i === 0)
            return false;
    }
    return true;
};

function solution(numbers) {
    numbers = numbers.split('').map(Number);
    // numbers = [1,2,3,4];
    const checked = new Set();
    const madeNumbers = new Set();
    let answer = 0;
    const makeNumberDFS = (index, prefix, depth)=>{
        prefix = prefix + numbers[index];
        madeNumbers.add(Number(prefix));
        // console.log("index : ", index, "prefix : " , prefix, " depth : ", depth)
        // depth가 1일 때 현재 numbers의 index 에 있는 숫자 push. 
        if(depth === 1){
            return;
        }
        
        for(let i =0; i<numbers.length; ++i){
            if(!checked.has(i)){
                checked.add(i);
                makeNumberDFS(i, prefix, depth-1);
                checked.delete(i);
            }
        }
    };
    // checked.add(0);
    // makeNumberDFS(0, '', numbers.length)
    for(let i =0; i<numbers.length; ++i){
        // 한번 체크한 숫자 index 저장. 
        checked.add(i);
        makeNumberDFS(i, '', numbers.length);
        checked.clear();
        // newNumbers.filter((el)=>isPrime(el));
    }
    madeNumbers.forEach((num)=>{
        if(isPrime(num)){
            ++answer;
            console.log("isPrime ! ", num);
        }
    });
    // console.log("madeNumbers : ", madeNumbers);
    
    return answer;
}