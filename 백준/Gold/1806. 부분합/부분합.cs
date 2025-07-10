using System;
using System.Linq;
class Program
{

  private static void Main(string[] args)
  {
    baekjoon1806();
  }
  private static void baekjoon1806()
  {
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int N = input[0];
    int S = input[1];
    input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int startIdx = 0;
    int endIdx = 0;
    long sum = 0;
    long best = Int32.MaxValue;
    while (true)
    {
      if (sum >= S)
      {
        best = Math.Min(best, endIdx - startIdx);
        sum -= input[startIdx];
        startIdx++;
      }
      else if (endIdx == N)
        break;
      else
      {
        sum += input[endIdx];
        endIdx++;
      }
    }
    Console.WriteLine(best.Equals(Int32.MaxValue)?0:best);
  }
}