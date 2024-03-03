function solution(bridge_length, weight, truck_weights) {
    var time = 0;
    const passing_q = [];      // 다리 위에 있는 트럭 q. [weight, remain_weight]
    let remain_w = weight;
    
    // 지나가고 있는 트럭 q가 빌 때 까지.
    while(passing_q.length || truck_weights.length){
        // console.log("time : ", time, "passing_q : ", passing_q)
        
        if(truck_weights[0] <= remain_w){
            remain_w-=truck_weights[0];
            passing_q.push({weight:truck_weights.shift(), pushTime:time})
        }
        ++time;
        // 경과 시간 - 다리에 올라간 시간이 bridge_length보다 크면 빠져나온다.
        if((time - passing_q[0].pushTime) >= bridge_length){
            remain_w += passing_q[0].weight;
            passing_q.shift();
        }
    }
    ++time;
    return time;
}