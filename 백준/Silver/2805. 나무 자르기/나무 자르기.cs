using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int M = input[1];
            int[] heights = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int start = 0;
            int end = heights.Max();
            int answer = 0;
            while(start <= end)
            {
                long sum = 0;
                int mid = (start + end) / 2;
                for(int i=0; i<heights.Length; i++)
                {
                    sum += Math.Max(0, heights[i] - mid);
                }
                if(sum >= M)
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
