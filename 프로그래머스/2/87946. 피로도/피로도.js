function solution(k, dungeons) {
    var answer = -1;
    let max = 0;
    const DFS = (hp, index, visited) =>{
        visited.add(index);
        answer = Math.max(answer, visited.size);
        hp -= dungeons[index][1];
        // console.log("hp : " , hp, " index: ", index, " visited : " , visited, " info : ", dungeons[index] )
        for(let i =0; i<dungeons.length; ++i){
            // console.log("inner for - index : ", index, " hp : ", hp)
            if(!visited.has(i) && hp >= dungeons[i][0]){
                DFS(hp, i, visited);
                // console.log("-- inner DFS out --")
                visited.delete(i);
            }
        }
    }
    const visited = new Set();
    for(let i =0; i<dungeons.length; ++i){
        if(k >= dungeons[i][0]){
            // console.log("- - start DFS - - start index : ", i )
            DFS(k, i, visited);
            visited.clear();
        }

    }
    return answer;
}