function solution(prices) {
    const answer = Array(prices.length).fill(0);
    let lastMaxPrice = -1;
    const priceStack = [];//prices.map((price, index)=>({price:price, t:index}))
    for(let i=0; i<prices.length; ++i){
        // 가격이 떨어졌다. 
        // priceStack에서 price가 lastMaxPrice prices[i]보다 큰 값을 갖는 녀석들을 빼낸다.
        if(prices[i] < lastMaxPrice){
            lastMaxPrice = prices[i];
            while(priceStack.length){
                if(lastMaxPrice < priceStack[priceStack.length-1].price){
                    const cur = priceStack.pop();
                    answer[cur.time] = i - cur.time;
                }
                else
                    break;
            }
        }
        
        lastMaxPrice = Math.max(prices[i], lastMaxPrice);
        priceStack.push({price:prices[i], time : i})
        // console.log(i, " : priceStack : ", priceStack, "lastMaxPrice :", lastMaxPrice)
    }
    for(let i =0; i<priceStack.length; ++i){
        answer[priceStack[i].time] = prices.length - priceStack[i].time -1;
    }
    return answer;
}
/*
//효율성 x. 
function solution(prices) {
    const answer = []
    const priceStack = prices.map((price, index)=>({price:price, t:index}))
    let time = 0;
    while(priceStack.length){
        const cur = priceStack.shift();
        let time = prices.length - cur.t -1;
        for(let i =0; i<priceStack.length; ++i){
            if(priceStack[i].price < cur.price){
                time = priceStack[i].t - cur.t;
                break;
            }
        }
        answer.push(time);
    }
    
    return answer;
}*/