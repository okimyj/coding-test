using System;

class Solution {
    public int solution(int[] A) {
        if(A.Length <= 0)
            return 0;
        int minPrice = A[0];
        int maxProfit = 0;
        for(int i=0; i<A.Length; i++)
        {
            maxProfit = Math.Max(maxProfit, A[i] - minPrice);
            if(minPrice > A[i])
                minPrice = A[i];
        }
        return Math.Max(0, maxProfit);
    }
}






