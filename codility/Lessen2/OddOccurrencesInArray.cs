using System;
using System.Collections.Generic;
using System.Linq;
// Linq만으로 좀 괴랄하게 풀어본것.
// 시간 복잡도 failed.
class Solution {
    public int solution(int[] A) {
        return A.GroupBy(x=>x)
        .Select(g=>new KeyValuePair<int,int>(g.Key, g.Count()%2))
        .Where(kv=>kv.Value == 1).First().Key;
    }
}


using System;
using System.Collections.Generic;
using System.Linq;
// 정렬 후 stack에 push/pop 해가면서 마지막으로 남은 요소를 반환.
class Solution {
    public int solution(int[] A) {
        List<int> sorted = A.OrderBy(x=>x).ToList();
        Stack<int> stack = new Stack<int>();
        for(int i=0; i<sorted.Count; i++)
        {
            if(stack.TryPeek(out int peek) && peek == sorted[i])
                stack.Pop();
            else
                stack.Push(sorted[i]);
        }
        return stack.Pop();
    }
}
