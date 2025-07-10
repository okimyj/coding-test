using System;
using System.Linq;
class Program
{

  private static void Main(string[] args)
  {
    baekjoon2470();
  }
  private static void baekjoon2470()
  {
    int N = Convert.ToInt32(Console.ReadLine());
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int[] sorted = input.OrderBy(x => x).ToArray();
    int best = Int32.MaxValue;
    int left = 0;
    int right = sorted.Length - 1;
    int[] answer = new int[2];
    while (left < right)
    {
      int sum = sorted[left] + sorted[right];
      if (Math.Abs(sum) < best)
      {
        best = Math.Abs(sum);
        answer[0] = sorted[left];
        answer[1] = sorted[right];
      }
      if (sum > 0)
        right--;
      else
        left++;
    }
    Console.WriteLine(string.Join(' ', answer));
  }
}