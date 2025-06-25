using System.Linq;
internal class Program
{
  private static void Main(string[] args)
  {
    int[] input = Console.ReadLine().Split(' ').Select(c => Convert.ToInt32(c)).ToArray();
    int N = input[0];
    int M = input[1];
    int[] basket = Enumerable.Range(1, N).ToArray();
    for (int i = 0; i < M; i++)
    {
      input = Console.ReadLine().Split(' ').Select(c => Convert.ToInt32(c)-1).ToArray();
      int temp = basket[input[0]];
      basket[input[0]] = basket[input[1]];
      basket[input[1]] = temp;
    }
    Console.WriteLine(string.Join(' ', basket));
  }
}