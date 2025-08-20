using System;
using System.Linq;

public class Solution {
    public int solution(int[] picks, string[] minerals)
    {
        int answer = 0;
        // 캘 수 있는 광물의 개수.
        int pickableNum = Math.Min(minerals.Length, picks.Sum(x => x)*5);

        // 광물 5개 마다의 피로도 합산 구하기.
        int sectionNum = (int)Math.Ceiling(pickableNum / 5f);
        int[][] pickLevels = new int[sectionNum][];
        
        // 캘 수 있는 광물 개수 만큼만 계산. 
        for (int i = 0; i < pickableNum; i++)
        {
            if (pickLevels[i / 5] == null)
                pickLevels[i / 5] = new int[3];

            switch (minerals[i])
            {
                case "diamond":
                    pickLevels[i / 5][0] += 1;      // 다이아 - 다이아 곡괭이
                    pickLevels[i / 5][1] += 5;      // 다이아 - 철 곡괭이
                    pickLevels[i / 5][2] += 25;     // 다이아 - 돌 곡괭이
                    break;
                case "iron":
                    pickLevels[i / 5][0] += 1;
                    pickLevels[i / 5][1] += 1;
                    pickLevels[i / 5][2] += 5;
                    break;
                case "stone":
                    pickLevels[i / 5][0] += 1;
                    pickLevels[i / 5][1] += 1;
                    pickLevels[i / 5][2] += 1;
                    break;
            }
        }
        // 돌로 캘 때의 피로도가 가장 높은 순으로 정렬 후 피로도가 가장 낮게 들어가는 다이아로 캔다.
        Array.Sort(pickLevels, (A, B) => B[2] - A[2]);

        for(int i=0; i< sectionNum; i++)
        {
            if (picks[0] > 0)
            {
                answer += pickLevels[i][0];
                --picks[0];
            }
            else if (picks[1] > 0)
            {
                answer += pickLevels[i][1];
                --picks[1];
            }
            else if (picks[2] > 0)
            {
                answer += pickLevels[i][2];
                --picks[2];
            }
        }

        return answer;
    }
}