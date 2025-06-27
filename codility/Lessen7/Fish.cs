/*
  이미 상류로 지나간 물고기는 하류로 가는 물고기가 잡을 수 없음.
  하류로 가는 물고기만 downStream stack에 push한다. 
  상류로 가는 물고기가 들어왔을 때 하류로 가는 물고기가 없다면 생존.
  있다면 해당 물고기보다 내가 더 큰 경우 생존.
*/
using System;
using System.Collections.Generic;
class Solution {
    public int solution(int[] A, int[] B) {
        Stack<int> downStream = new Stack<int>();
        int aliveCnt = 0;
        for(int i=0; i<A.Length; i++)
        {
            // 하류로 가는 물고기 push.
            if(B[i] == 1)
                downStream.Push(A[i]);
            else
            {
                while(downStream.Count > 0)
                {
                    if(downStream.Peek() < A[i])
                        downStream.Pop();
                    else
                        break;
                }
                if(downStream.Count <= 0)
                    aliveCnt++;
            }
        }
        return aliveCnt + downStream.Count;
    }
}
