using System.Linq;
internal class Program
{
  private static void Main(string[] args)
  {
    int[] coins = new int[] { 500, 100, 50, 10, 5, 1 };
    int price = Convert.ToInt32(Console.ReadLine());
    int answer = 0;
    int N = 1000 - price;
    for (int i = 0; i < coins.Length; i++)
    {
      answer += N / coins[i];
      N %= coins[i];
    }
    Console.WriteLine(answer);
  }
}