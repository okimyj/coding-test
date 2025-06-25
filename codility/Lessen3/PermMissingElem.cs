/*
N개의 서로다른 정수로 구성된 배열 A가 주어지고
A는 [1,... (N+1)]의 범위로 구성되어있다. 
여기서 누락된 요소를 찾아 리턴.
A를 오름차순으로 정렬해서 1부터 순서대로 있는지 체크.
*/
using System;
using System.Linq;
class Solution {
    public int solution(int[] A) {
        // A가 비어있다. 1이 없는 것.
        if(A.Length <= 0)
            return 1;
        int[] sortedArray = A.OrderBy(x=>x).ToArray();
        for(int i=0; i<sortedArray.Length; i++)
        {
            if(i+1 != sortedArray[i])
                return i+1;
        }
        return 0;
    }
}
