using System;
using System.Linq;
/*
  문제 해석을 잘 못함 . P, Q, R, N 이 각 원소의 값인 줄 알았으나 index를 의미.
*/
class Solution {
    public int solution(int[] A) {
        //N is an integer within the range [0..100,000];
        // each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
        // 0 <= P < Q < R < N => 음수, 100,000이상 제거 후 오름차순 정렬.
        var positiveNumbers = A.Where(x=> x >= 0 && x < 100000).OrderBy(x=>x).ToList();
        // P + Q > R
        // Q + R > P
        // R + P > Q
        // => 3개의 값 중 2개의 값을 더 한 값이 항상 나머지 하나의 값보다 크다.
        for(int iP=0; iP<positiveNumbers.Count-2; iP++)
        {
            int P = positiveNumbers[iP];
            for(int iQ = iP+1; iQ<positiveNumbers.Count-1; iQ++)
            {
                int Q = positiveNumbers[iQ];
                for(int iR=iQ+1; iR<positiveNumbers.Count; iR++)
                {
                    int R = positiveNumbers[iR];
                    if(P+Q>R && Q+R>P && R+P > Q)
                        return 1;
                }
            }
        }
        return 0;
    }
}


// 최종 코드.
using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    public int solution(int[] A) {
        // 0 ≤ P < Q < R < N
        // index가 인접해있다.
        List<int> sorted = A.OrderBy(x=>x).ToList();
        for(int i=0;i<sorted.Count-2; i++)
        {
            // int overflow 발생. 조건을 반대로 바꾼다.
            if(sorted[i+2] - sorted[i] < sorted[i+1])
                return 1;
            //if(sorted[i] + sorted[i+1] > sorted[i+2])
            //    return 1;
        }
        return 0;
    }
}
