/*
  정상적인 괄호인지 확인 하는 문제. 
  굳이 stack 사용할 필요 없음.
*/
using System;
class Solution {
    public int solution(string S) {
        // Implement your solution here
        int open = 0;
        for(int i=0; i<S.Length; i++)
        {
            if(S[i] == '(')
                open++;
            else
                open--;
            if(open < 0)
                break;
        }
        return open == 0 ? 1 : 0;
    }
}






