/*
  입력값 N을 2진수로 변환했을 때 
  1과 1사이에 있는 0의 개수의 최대 값을 구하는 문제.
*/
using System;
using System.Linq;

class Solution {
    public int solution(int N) {
        // Implement your solution here
        string binaryN = Convert.ToString(N, 2);
        int maxGap = 0;
        int startIndex = 0;
        for(int i=0; i<binaryN.Length; i++)
        {
            if(binaryN[i] == '1')
            {
                maxGap = Math.Max(maxGap, i - startIndex -1);
                startIndex = i;
            }
        }
        return maxGap;
    }
}
