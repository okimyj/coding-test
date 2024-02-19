// function solution(nums) {
//     const canHasNum = nums.length/2;
//     const set = new Set();
//     for(let i=0; i<nums.length; ++i){
//         if(!set.has(nums[i])){
//             set.add(nums[i]);
//             if(set.size >= canHasNum)
//                 break;
//         }
//     }
    
//     return set.size;
// }
function solution(nums) {
    const set = new Set([...nums]);
    return Math.min(set.size, nums.length/2);
}