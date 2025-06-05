using System;

public class Solution {
    public int solution(string number) {
        int sum = 0;
        for(int i=0; i<number.Length; ++i){
            sum += (int)number[i] - 48;
        }
        return sum % 9;
    }
}