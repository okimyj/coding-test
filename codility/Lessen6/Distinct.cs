using System;
using System.Linq;
/*
  배열 A의 고유한 값들의 개수를 반환한다.
*/
class Solution {
    public int solution(int[] A) {
        
        return A.GroupBy(x=>x).Count();
    }
}
