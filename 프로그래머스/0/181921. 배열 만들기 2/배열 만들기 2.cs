using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int l, int r) {
        while(l%5 != 0)
            l++;
        List<int> answer = new List<int>();
        for(int i=l; i<=r; i+=5)
        {
            string strN = i.ToString().Replace("0", "").Replace("5", "");
            if(string.IsNullOrEmpty(strN))
                answer.Add(i);
        }
            
        /*
        string[] ignoreNumbers = Enumerable.Range(1, 9).Where(x=>x!=5).Select(x=>x.ToString()).ToArray();
        
        for(int i=l; i<=r; i++)
        {
            string strN = i.ToString();
            bool canAdd = true;
            foreach(string n in ignoreNumbers)
            {
                if(strN.Contains(n))
                {
                    canAdd = false;
                    break;
                }
            }
            if(canAdd)
                answer.Add(i);
        }
        */
        return answer.Count == 0 ? new int[]{-1} : answer.ToArray();
    }
}