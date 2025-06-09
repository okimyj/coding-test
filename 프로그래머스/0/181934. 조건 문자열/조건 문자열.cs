using System;

public class Solution {
    public int solution(string ineq, string eq, int n, int m) {
        int answer = 0;
        bool result = false;
        switch(ineq){
            case ">":
                result = eq == "=" ? n >= m : n > m;
                break;
            case "<":
                result = eq == "=" ? n <= m : n < m;
                break;
        }
        return result ? 1 : 0;
    }
}