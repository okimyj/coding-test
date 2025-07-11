using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<int> answer = new List<int>();
        /*List<int> workDays = new List<int>();
        for(int i=0; i<progresses.Length; ++i)
        {
            workDays.Add((int)Math.Ceiling((100f - progresses[i]) / speeds[i]));
        }
        */
        List<int> workDays = progresses.Select((value, i)=>(int)Math.Ceiling((100f- value)/speeds[i])).ToList();
        
        int prevMaxDeployDay = workDays[0];
        int deployNumOfDay = 0;
        for(int i=0; i<workDays.Count; ++i)
        {
            if(prevMaxDeployDay >= workDays[i])
            {
                ++deployNumOfDay;
            }
            else
            {
                answer.Add(deployNumOfDay);
                deployNumOfDay = 1;
                prevMaxDeployDay = workDays[i];
            }
        }
        answer.Add(deployNumOfDay);
        return answer.ToArray();
    }
}