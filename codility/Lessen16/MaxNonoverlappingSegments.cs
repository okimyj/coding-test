/*
겹치지 않는 선분의 개수를 구하는 문제.
*/
using System;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int prevE = -1;
        for(int i=0; i<A.Length; i++)
        {
            if(A[i] > prevE)
            {
                answer+=1;
                prevE = B[i];
            }
        }
        return answer;
    }
}