function solution(s) {
    var answer = '';
    const numArr = s.split(' ').map(Number);
    
    return `${Math.min(...numArr)} ${Math.max(...numArr)}`;
}