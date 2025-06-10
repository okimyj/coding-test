using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] solution(int[] answers) {
        List<int> answer = new List<int>() {0,0,0};
        int[] pattern1 = new int[]{1,2,3,4,5};
        int[] pattern2 = new int[]{2,1,2,3,2,4,2,5};
        int[] pattern3 = new int[]{3,3,1,1,2,2,4,4,5,5};
        for(int i=0; i<answers.Length; ++i)
        {
            if(answers[i] == pattern1[i%pattern1.Length]) ++answer[0];
            if(answers[i] == pattern2[i%pattern2.Length]) ++answer[1];
            if(answers[i] == pattern3[i%pattern3.Length]) ++answer[2];
        }
        int max = answer.Max();
        return answer.Select((v, i)=> new {v, i}).Where(x=>x.v == max).Select(x=>x.i+1).ToArray();
    }
}