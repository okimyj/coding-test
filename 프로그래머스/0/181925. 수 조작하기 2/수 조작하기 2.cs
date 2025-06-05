using System;

public class Solution {
    public string solution(int[] numLog) {
        string answer = "";
        int prevValue = 0;
        for(int i=1; i<numLog.Length; ++i){
            prevValue = numLog[i-1];
            int code = numLog[i] - prevValue;
            switch(code){
                case 1 :
                    answer += "w";    
                    break;
                case -1 :
                    answer += "s";
                    break;
                case 10:
                    answer += "d";
                    break;
                case -10:
                    answer += "a";
                    break;
                default :
                    break;
            }
       }
        return answer;
    }
}