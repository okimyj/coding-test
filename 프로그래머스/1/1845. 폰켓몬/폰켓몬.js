function solution(nums) {
    const uniqueSet = new Set(nums);
    return Math.min(uniqueSet.size, nums.length/2)
}