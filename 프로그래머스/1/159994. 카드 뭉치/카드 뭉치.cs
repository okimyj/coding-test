using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        Queue<string> cardQueue1 = new Queue<string>(cards1);
        Queue<string> cardQueue2 = new Queue<string>(cards2);
        string answer = "Yes";
        for(int i=0; i<goal.Length; ++i)
        {
            if(cardQueue1.Count > 0 && cardQueue1.Peek() == goal[i])
            {
               cardQueue1.Dequeue(); 
            }
            else if(cardQueue2.Count > 0 && cardQueue2.Peek() == goal[i])
            {
                cardQueue2.Dequeue();
            }
            else
            {
                answer = "No";
                break;
            }
        }
        
        return answer;
    }
}