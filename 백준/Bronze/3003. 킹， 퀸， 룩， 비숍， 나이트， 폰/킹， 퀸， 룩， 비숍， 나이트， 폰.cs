using System.Linq;
using System.Text;
internal class Program
{
  private static void Main(string[] args)
  {
    int[] needNum = { 1, 1, 2, 2, 2, 8 };
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    for (int i = 0; i < needNum.Length; i++)
    {
      input[i] = needNum[i] - input[i];
    }
    Console.WriteLine(string.Join(' ', input));
  }

}