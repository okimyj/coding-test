internal class Program
{
    static void Main()
    {
        new BaekJoon_1253().Start();
    }
}
public class BaekJoon_1253
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).OrderByDescending(x => x).ToArray();
        int answer = 0;
        for(int i=0; i< numbers.Length; i++)
        {
            int left = 0;
            int right = numbers.Length - 1;
            while(left < right)
            {
                if(left == i)
                {
                    left++;
                }
                if(right == i)
                {
                    right--;
                }
                if (left == right)
                    break;
                int sum = numbers[left] + numbers[right];
                
                if (sum == numbers[i])
                {
                    answer++;
                    break;
                }
                
                if (sum > numbers[i])
                {
                    left++;
                }
                else
                {
                    right--;
                }
            }
        }
        Console.WriteLine(answer);
    }
}