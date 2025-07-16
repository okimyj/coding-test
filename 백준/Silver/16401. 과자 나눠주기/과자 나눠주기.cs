using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int M = input[0];
            int N = input[1];
            int[] snacks = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            long start = 1;
            long end = snacks.Max();
            long answer = 0;
            while (start <= end)
            {
                long mid = (start + end) / 2;
                long count = 0;
                for(int i=0; i<snacks.Length; i++)
                {
                    count += snacks[i] / mid;
                }
                if(count >= M)
                {
                    answer = mid;
                    start = mid + 1;
                }
                else
                {
                    end = mid - 1;
                }
            }
            Console.WriteLine(answer);
        }
    }
}
