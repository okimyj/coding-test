function solution(k, dungeons) {
    var answer = -1;
    let max = 0;
    const DFS = (hp, index, visited, depth) =>{
        if(hp < dungeons[index][0]){
            // console.log("cannot more - depth : ", depth, " hp : ", hp, " dungeon : ", dungeons[index])
            answer = Math.max(visited.size, answer)
            return;
        }
        visited.add(index+1);
        if(depth === 1){
            answer = Math.max(visited.size, answer)
            return;
        }
        // console.log("DFS - index : ", index+1, "hp : ", hp, " data : ", dungeons[index] , " depth : ", depth, " visited : ", visited)
        for(let i =0; i<dungeons.length; ++i){
            if(!visited.has(i+1)){
                DFS(hp - dungeons[index][1], i, visited, depth-1);
                visited.delete(i+1);
            }
        }
    }
    
    for(let i =0; i<dungeons.length; ++i){
        
        DFS(k, i, new Set(), dungeons.length);
        // const num = DFS(k, i, new Set(), dungeons.length);
        // answer = Math.max(answer, num);
    }
    return answer;
}