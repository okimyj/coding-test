/*
  1. 같은 높이의 벽은 stack에 추가하지 않음. 
  2. stack에 추가되어있는 벽 중 나보다 높은 벽 제거. 
  3. stack이 비어있거나 stack에 나보다 작은 벽만 있는 경우 count증가, push.
  
*/

using System;
using System.Collections.Generic;
class Solution {
    public int solution(int[] H) {
        // Implement your solution here
        Stack<int> stack = new Stack<int>();
        int count = 0;
        for(int i=0; i<H.Length; i++)
        {
            while(stack.Count > 0 && stack.Peek() > H[i])
            {
                stack.Pop();
            }
            if(stack.Count <= 0 || stack.Peek() < H[i])
            {
                count++;
                stack.Push(H[i]);
            }
        }
        return count;
    }
}
