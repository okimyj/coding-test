using System;
// 1차원 배열 회전 문제.
//   [3, 8, 9, 7, 6] , K=3
//=> [9, 7, 6, 3, 8]
class Solution {
    public int[] solution(int[] A, int K) {
        // Implement your solution here
        int[] answer = new int[A.Length];
        for(int i=0; i<A.Length; ++i)
        {
            int index = (i+K)%A.Length;
            answer[index] = A[i]; 
        }
        return answer;
    }
}
