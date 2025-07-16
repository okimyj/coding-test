using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(c => Convert.ToInt32(c)).ToArray();
            int X = input[1];
            input = Console.ReadLine().Split(" ").Select(c => Convert.ToInt32(c)).ToArray();
            int left = 0;
            int max = 0;
            int sum = 0;
            List<int> visitorSum = new List<int>();
            for(int right=0; right < input.Length; right++)
            {
                if (right - left >= X)
                {
                    visitorSum.Add(sum);
                    left = left + 1;
                    sum -= input[right - X];
                }
                sum += input[right];
            }
            visitorSum.Add(sum);
            List<int> sorted = visitorSum.OrderByDescending(x => x).ToList();
            if (sorted[0] == 0)
                Console.WriteLine("SAD");
            else
            {
                Console.WriteLine(sorted[0]);
                Console.WriteLine(sorted.Count(v => v == sorted[0]));
            }
        }
    }
}
