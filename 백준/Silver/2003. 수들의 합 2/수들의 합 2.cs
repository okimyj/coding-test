using System;
using System.Linq;
class Program
{

  private static void Main(string[] args)
  {
    baekjoon2003();
  }
  private static void baekjoon2003()
  {
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int M = input[1];
    int[] numbers = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int answer = 0;
    int left = 0;
    int right = 0;
    int sum = 0;
    while (true)
    {
      if (sum > M)
      {
        sum -= numbers[left];
        left++;
      }
      else if (right == numbers.Length)
        break;
      else
      {
        sum += numbers[right];
        right++;
      }
      if (sum == M)
      {
        sum -= numbers[left];
        left++;
        answer++;
      }
    }
    Console.WriteLine(answer);
  }
}