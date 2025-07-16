using System;

public class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int level = 0;
        long remainSec = 0;
        int left = 1;
        int right = 100001;
        while(left < right)
        {
            level = (left+right)/2;
            if(CanSolve(level, diffs, times, limit))
            {
                right = level;
            }
            else
                left = level+1;
        }
        return left;
    }
    public bool CanSolve(int level, int[] diffs, int[] times, long limit)
    {
        for(int i=0; i<diffs.Length; i++)
        {
            if(diffs[i] <= level)
            {
                limit -= times[i];
            }
            else
            {
                limit -= (times[i] + times[i-1]) * (diffs[i]-level) + times[i];
            }
            if(limit < 0)
                break;
        }
        if(limit >= 0)
        {
            return true;
        }
        return false;
    }
}