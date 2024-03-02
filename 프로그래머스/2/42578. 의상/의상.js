function solution(clothes) {
    const map = new Map();
    for(let i =0; i<clothes.length; ++i){
        const [name, kind] = clothes[i];
        map.set(kind, ([...map.get(kind)||[], name]));
    }
    
    const result = [...map.values()].reduce((acc, v)=>{
        acc *= (v.length+1)
        return acc;
    },1)
    
    return result-1;
}