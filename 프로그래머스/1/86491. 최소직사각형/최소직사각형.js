function solution(sizes) {
    let maxW = 0;
    let maxH = 0;
    var answer = 0;
    sizes.forEach(([w,h])=>{
        // 둘 중 하나가 maxSize 보다 크다면,
        if(w < h){
            const temp = h;
            h = w;
            w = temp;
        }
        maxW = Math.max(maxW, w);
        maxH = Math.max(maxH, h);
        
    });
    
    return maxW * maxH;
}