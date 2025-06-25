using System;
using System.Linq;
/*
  1차 : 내림차순으로 정렬 후 앞에서 부터 3개의 요소를 합산한 값을 리턴한다.
*/
class Solution {
    public int solution(int[] A) {
        int answer = A.OrderByDescending(x=>x).Take(3).Aggregate((A,B)=>A*B);
        return answer;
        /*
        var maximalNumbers = A.OrderByDescending(x=>x).Take(3);
        int answer = 1;
        foreach(int n in maximalNumbers)
        {
            answer *= n;
        }
        return answer;
        */
    }
}

/*
  2차 : 내림차순으로 정렬 되어있을 때.
  1. 모두 양수라면 맨 앞의 3개의 값의 곱이 가장 큰 수.
  2. 정렬된 값에 음수가 2개 이상이 있다면, 뒤에서부터 2개의 값과 맨 앞의 값을 곱한 것이 최대 값이 됨.
*/
class Solution {
    public int solution(int[] A) {
        // 내림 차순으로 정렬.
        var sorted = A.OrderByDescending(x=>x);
        // 맨 앞에서 3개의 곱을 구함. (모두 양수 일 때는 이 녀석이 가장 큰 값.)
        int productA = sorted.Take(3).Aggregate((A,B)=>A*B);
        // 맨 앞의 값 1개와 맨 뒤의 값 2개의 곱을 구함.
        // 음 수가 있는 경우 가장 작은 음수 2개와 맨 앞의 큰 값을 곱한 값이 가장 큰 값임.
        int productB = sorted.Skip(sorted.Count()-2).Take(2).Aggregate((A,B)=>A*B) * sorted.First();
        return Math.Max(productA, productB);
    }
}
