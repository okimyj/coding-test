/*
  open 형태의 괄호를 stack에 쌓고,
  close 괄호가 들어왔을 때 현재 stack에 있는 괄호와 비교해 pair한 것인지 확인.
*/
using System;
using System.Collections.Generic;

class Solution {
    public int solution(string S) {
        // Implement your solution here
        Stack<char> openStack = new Stack<char>();
        for(int i=0; i<S.Length; i++)
        {
            if(IsOpen(S[i]))
                openStack.Push(S[i]);
            else
            {               
                if(openStack.Count <= 0 || !IsPair(openStack.Peek(), S[i]))
                    return 0;
                openStack.Pop();
            }
        }
        return openStack.Count == 0 ? 1 : 0;
    }
    public bool IsPair(char open, char close)
    {
        return (open == '{' && close == '}')
            || (open == '[' && close == ']')
            || (open == '(' && close == ')');
    }
    public bool IsOpen(char c)
    {
        return c == '{' || c == '[' || c == '(';
    }
}
