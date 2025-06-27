/*
  1. 가장 많이 나타나는 leader요소를 찾는다. 
  2. A를 돌면서 해당 index까지 포함된 leader의 개수를 계산한다.
  3. A개수만큼 돌면서 포함되는 배열의 갯수 / 2 보다 count[index]가 커지는 경우
     나머지 뒤쪽의 갯수도 체크해서 둘 다 조건을 만족하는 경우 answer++
*/

using System;
using System.Linq;
class Solution {
    
    public int solution(int[] A) {
        int leader = A.GroupBy(x=>x).OrderByDescending(kv=>kv.Count()).First().Key;
        int[] count = new int[A.Length];
        count[0] = A[0] == leader ? 1 : 0;
        for(int i=1; i<A.Length; i++)
        {
            count[i] = count[i-1];
            if(leader == A[i])
                count[i]++;
        }
        
        int answer = 0;
        for(int i=0; i<A.Length; i++)
        {
            int S = (i+1);
            if(S/2 < count[i])
            {
                if((A.Length - S)/2 < count[A.Length-1] - count[i])
                    answer++;
            }
        }
        return answer;
    }
}
