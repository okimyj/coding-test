using System.Linq;
using System.Text;
internal class Program
{
  private static void Main(string[] args)
  {
    int target = Convert.ToInt32(Console.ReadLine());
    int answer = 0;
    while (target > 0)
    {
      if (target % 5 == 0)
      {
        answer += target / 5;
        break;
      }
      
      target -= 3;
      answer++;
      if (target < 0)
      {
        answer = -1;
        break;
      }
    }
    Console.WriteLine(answer);
  }
}