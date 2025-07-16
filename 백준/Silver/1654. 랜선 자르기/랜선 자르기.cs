using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int K = input[0];
            int N = input[1];
            int[] lines = new int[K];
            for (int i = 0; i < K; i++)
                lines[i] = int.Parse(Console.ReadLine());
            long start = 1;
            long end = (int)Math.Pow(2, 31) - 1;
            long count = 0;
            long answer = 0;
            while (start <= end) 
            {
                count = 0;
                long mid = (start + end) / 2;
                for(int i=0; i<lines.Length; i++)
                {
                    count += lines[i] / mid;
                }
                if(count >= N)
                {
                    start = mid + 1;
                    answer = mid;
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
