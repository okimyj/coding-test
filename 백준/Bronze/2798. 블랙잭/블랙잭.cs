using System.Linq;
using System.Text;
internal class Program
{
  private static void Main(string[] args)
  {
    int[] inputs = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int N = inputs[0];
    int M = inputs[1];
    int[] cards = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int max = 0;
    for (int i = 0; i < N - 2; i++)
    {
      for (int j = i+1; j < N - 1; j++)
      {
        for (int k = j+1; k < N; k++)
        {
           
          int sum = cards[i] + cards[j] + cards[k];
          if (sum <= M && max < sum)
            max = sum;
        }
      }
    }
    Console.WriteLine(max);
  }
}