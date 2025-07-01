/*
카데인 알고리즘 적용. 
이전 인덱스가 가질 수 있는 최대 부분합에 현재 인덱스의 값을 더하면 
현재 인덱스가 가질 수 있는 최대 부분합을 알 수 있다.
-> 이전 인덱스가 갖고 있는 최대 부분합을 연장할지, 값을 현재 값으로 초기화 할지 고른다.
*/
using System;
class Solution {
    public int solution(int[] A) {
        int slicing = A[0];
        int max = A[0];
        for(int i=1; i<A.Length; i++)
        {
            slicing = Math.Max(slicing+A[i], A[i]);
            max = Math.Max(max, slicing);
        }
        return max;
    }
}