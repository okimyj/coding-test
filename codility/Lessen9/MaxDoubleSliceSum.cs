using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int[] A) {
        int[] leftSum = new int[A.Length];
        int[] rightSum = new int[A.Length];
        // X, 맨 처음 인덱스는 포함하지 않음.
        for(int y=1; y<A.Length; y++)
        {
            leftSum[y] = Math.Max(leftSum[y-1] + A[y], 0);
        }
        //rightSum[A.Length-1] = A[A.Length-1];
        for(int y=A.Length-2; y>0; y--)
        {
            rightSum[y] = Math.Max(0, rightSum[y+1] + A[y]);
        }
        //Console.WriteLine($"left : {string.Join(", ", leftSum)}");
        //Console.WriteLine($"right : {string.Join(", ", rightSum)}");
        
        int max = 0;
        for(int y=1; y<leftSum.Length-1; y++)
        {
            int sum = leftSum[y-1]+rightSum[y+1];
            if(max < sum)
            {
                max = sum;
                //Console.WriteLine($"y : {y}, sum : {sum}");
            }

        }
        return max;
    }
}