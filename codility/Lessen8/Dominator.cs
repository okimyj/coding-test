/*
  배열 A를 구성하고 있는 요소 중 요소의 개수가 가장 많으면서
  배열 A의 개수 / 2 의 개수보다 많은 수를 가진 요소의 인덱스중 하나를 반환.
*/
using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    class Data{
        public int index;
        public int count;
    }
    public int solution(int[] A) {
        Dictionary<int, Data> countMap = new Dictionary<int, Data>();
        Data maxCountData = null;
        for(int i=0; i<A.Length; i++)
        {
            if(!countMap.ContainsKey(A[i]))
                countMap[A[i]] = new Data(){index = i, count =0};
            countMap[A[i]].count++;
            if(maxCountData == null || maxCountData.count < countMap[A[i]].count)
            maxCountData = countMap[A[i]];
        }
        
        if(maxCountData == null || A.Length / 2 >= maxCountData.count)
            return -1;
        return maxCountData.index;
    }
}