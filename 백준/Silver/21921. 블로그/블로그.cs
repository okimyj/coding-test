using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(c => Convert.ToInt32(c)).ToArray();
            int N = input[0];
            int X = input[1];
            input = Console.ReadLine().Split(" ").Select(c => Convert.ToInt32(c)).ToArray();
                        
            int sum = 0;
            for(int i=0; i<X; i++)
            {
                sum += input[i];
            }
            int max = sum;
            int count = 1;
            for (int right=X; right < N; right++)
            {
                sum += input[right] - input[right-X];
                if (max == sum)
                {
                    ++count;
                }
                else if (max < sum)
                {
                    max = sum;
                    count = 1;
                }
            }

            if (max == 0)
                Console.WriteLine("SAD");
            else
            {
                Console.WriteLine(max);
                Console.WriteLine(count);
            }
        }
    }
}
