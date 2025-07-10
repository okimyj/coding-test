using System;
using System.Collections.Generic;
using System.Linq;
class Program
{

  private static void Main(string[] args)
  {
    baekjoon10815();
  }
  private static void baekjoon10815()
  {
    Console.ReadLine();
    HashSet<int> hasCards = Console.ReadLine().Split(' ').Select(c => Convert.ToInt32(c)).ToHashSet();
    Console.ReadLine();
    int[] check = Console.ReadLine().Split(' ').Select(c => Convert.ToInt32(c)).ToArray();
    int[] answer = new int[check.Length];
    for (int i = 0; i < check.Length; i++)
    {
      if (hasCards.Contains(check[i]))
        answer[i] = 1;
    }
    Console.WriteLine(string.Join(" ", answer));
  }
}