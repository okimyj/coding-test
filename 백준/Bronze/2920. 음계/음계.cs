using System;
namespace OKIMYJ
{
  internal class Program
  {
    enum ORDER_TYPE {
      ASCENDING = 0,
      DESCENDING,
      MIXED
    }
    static void Main(string[] args)
    {
      int[] input = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
      
      ORDER_TYPE orderType = input[0] == 1 ? ORDER_TYPE.ASCENDING : input[0] == 8 ? ORDER_TYPE.DESCENDING : ORDER_TYPE.MIXED;

      if (orderType != ORDER_TYPE.MIXED)
      {
        for(int i=1; i<input.Length; ++i)
        {
          if((orderType == ORDER_TYPE.ASCENDING && input[i] != i+1) || (orderType == ORDER_TYPE.DESCENDING && input[i] != 8-i))
          {
            orderType = ORDER_TYPE.MIXED;
            break;
          }
        }
      }
      Console.WriteLine(orderType.ToString().ToLower());
    }
  }
}
