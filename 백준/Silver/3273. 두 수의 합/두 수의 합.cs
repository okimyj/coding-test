using System;
class Program
{

  private static void Main(string[] args)
  {
    baekjoon3273();
  }
  private static void baekjoon3273()
  {
    Console.ReadLine();
    int[] numbers = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).OrderBy(x => x).ToArray();
    int X = Convert.ToInt32(Console.ReadLine());

    int left = 0;
    int right = numbers.Length - 1;

    int count = 0;
    while (left < right)
    {
      int sum = numbers[left] + numbers[right];
      if (sum > X)
        right--;
      else if (sum < X)
        left++;
      else
      {
        count++;
        left++;
      }
    }
    Console.WriteLine(count);
  }
}