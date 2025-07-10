using System;
using System.Linq;
using System.Collections.Generic;
class Program
{
  
  private static void Main(string[] args)
  {
    baekjoon1931();
  }
  private static void baekjoon1931()
  {
    int N = Convert.ToInt32(Console.ReadLine());
    // 끝나는 시간이 가장 빠른 녀석부터 차례로 처리.
    PriorityQueue<(int s, int e), (int e, int s)> pq = new PriorityQueue<(int s, int e), (int e, int s)>();
    for (int i = 0; i < N; i++)
    {
      int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
      pq.Enqueue((input[0], input[1]), (input[1], input[0]));
    }
    int lastEndTime = -1;
    int answer = 0;
    while (pq.Count > 0)
    {
      var (s, e) = pq.Dequeue();
      if (lastEndTime <= s)
      {
        answer++;
        lastEndTime = e;
      }
        
    }
    Console.WriteLine(answer);
  }
}