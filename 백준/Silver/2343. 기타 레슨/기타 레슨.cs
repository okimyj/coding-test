using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int N = input[0];
            int M = input[1];
            input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int start = input.Max();
            int end = input.Sum();
            int answer = 0;
            while(start <= end)
            {
                int mid = (start + end) / 2;
                int count = 1;
                int sum = input[0];
                for (int i=1; i<input.Length; i++)
                {
                    if(sum + input[i] <= mid)
                    {
                        sum += input[i];
                    }
                    else
                    {
                        count++;
                        sum = input[i];
                    }
                }
                if(M < count)
                {
                    start = mid + 1;
                }
                else
                {
                    answer = mid;
                    end = mid - 1;
                }
            }
            Console.WriteLine(answer);
        }
    }
}
