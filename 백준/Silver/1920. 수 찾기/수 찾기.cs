using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            Console.ReadLine();
            //HashSet<string> numbers = Console.ReadLine().Split(" ").ToHashSet();
            string[] numbers = Console.ReadLine().Split(" ").ToArray();
            Console.ReadLine();
            string[] targetNumbers = Console.ReadLine().Split(" ").ToArray();
            
            for(int i=0; i<targetNumbers.Length; i++)
            {
                Console.WriteLine(numbers.Contains(targetNumbers[i]) ? 1 : 0);
            }
            */
            Console.ReadLine();
            int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            Array.Sort(numbers);
            Console.ReadLine();
            int[] targetNumbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            List<int> result = new List<int>();
            for (int i = 0; i < targetNumbers.Length; i++)
            {
                int left = 0;
                int right = numbers.Length-1;
                bool isFind = false;
                while(left <= right)
                {
                    int mid = (left + right) / 2;
                    if (numbers[mid] == targetNumbers[i])
                    {
                        isFind = true;
                        break;
                    }
                    if(numbers[mid] < targetNumbers[i])
                    {
                        left = mid+1;
                    }
                    else
                    {
                        right = mid - 1;
                    }
                }
                result.Add(isFind ? 1 : 0);
            }
            Console.WriteLine(string.Join("\n", result));
        }
    }
}
