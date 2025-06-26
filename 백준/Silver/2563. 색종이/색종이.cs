using System.Linq;
using System.Text;
internal class Program
{
  private static void Main(string[] args)
  {
    const int SIZE = 10;
    int N = Convert.ToInt32(Console.ReadLine());
    int[,] canvas = new int[100,100];
    
    for (int i = 0; i < N; i++)
    {
      int[] coord = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)-1).ToArray();
      for (int x = coord[0]; x < coord[0] + SIZE; x++)
      {
        for (int y = coord[1]; y < coord[1] + SIZE; y++)
        {
          canvas[x, y] = 1;
        }
      }
    }
    
    Console.WriteLine(canvas.Cast<int>().ToArray().Count(x => x == 1));
  }
}