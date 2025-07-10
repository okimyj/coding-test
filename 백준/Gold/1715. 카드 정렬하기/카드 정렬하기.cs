using System;
using System.Collections.Generic;
class Program
{
  
  private static void Main(string[] args)
  {
    baekjoon1715();
  }
  private static void baekjoon1715()
  {
    int N = Convert.ToInt32(Console.ReadLine());
    PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
    for (int i = 0; i < N; i++)
    {
      int C = Convert.ToInt32(Console.ReadLine());
      pq.Enqueue(C, C);
    }
    int answer = 0;
    while (pq.Count > 1)
    {
      int sum = pq.Dequeue() + pq.Dequeue();
      answer += sum;
      pq.Enqueue(sum, sum);
    }
    
    Console.WriteLine(answer);
  }
}