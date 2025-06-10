using System;

public class Solution {
    public int solution(int[,] sizes) {
        int answer = 0;
        int maxW = 0;
        int maxH = 0;
        for(int i=0; i<sizes.GetLength(0); ++i)
        {
            if(sizes[i,0] > sizes[i,1])
            {
                maxW = Math.Max(maxW, sizes[i,0]);
                maxH = Math.Max(maxH, sizes[i,1]);
            }
            else
            {
                maxW = Math.Max(maxW, sizes[i,1]);
                maxH = Math.Max(maxH, sizes[i,0]);
            }
        }
        return maxW * maxH;
    }
}