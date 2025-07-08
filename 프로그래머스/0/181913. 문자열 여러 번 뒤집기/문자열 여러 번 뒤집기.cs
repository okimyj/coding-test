using System;
using System.Linq;

public class Solution {
    public string solution(string my_string, int[,] queries) {
        char[] answer = my_string.Select(c=>c).ToArray();
        for(int q=0; q<queries.GetLength(0); q++)
        {
            int s = queries[q,0];
            int e = queries[q,1];
            string tempString = string.Join("", answer);
            for(int i=s; i<=e; i++)
            {
                answer[i] = tempString[e-(i-s)];
            }
        }
        return string.Join("",answer);
    }
}