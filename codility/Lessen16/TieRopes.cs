/*
인접한 로프를 묶어서 만들 수 있는 K보다 크거나 같은 길이의 로프 개수 반환.
*/

using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    public int solution(int K, int[] A) {
        // Implement your solution here
        int count = 0;
        int acc = 0;
        for(int i=0; i<A.Length; i++)
        {
            acc += A[i];
            if(acc >= K)
            {
                acc = 0;
                count++;

            }
        }
        return count;
    }
}
