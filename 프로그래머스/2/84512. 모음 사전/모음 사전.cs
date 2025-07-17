using System;
using System.Collections.Generic;
public class Solution {
    char[] alphavets = new char[]{'A', 'E', 'I', 'O', 'U'};
    List<string> dict = new List<string>();
    public int solution(string word) {
        MakeDict("");
        return dict.IndexOf(word);
    }
    public void MakeDict(string str)
    {
        dict.Add(str);
        if(str.Length == 5)
        {
            return;
        }
        for(int i=0; i<alphavets.Length; i++)
        {
            MakeDict(str+alphavets[i]);
        }
    }
}