internal class Program
{
    static void Main()
    {
        new BaekJoon_2473().Start();
    }
}
public class BaekJoon_2473
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        long[] values = Console.ReadLine().Split(' ').Select(long.Parse).ToArray().OrderBy(x => x).ToArray();
        long[] answer = new long[3];
        long curSumABS = long.MaxValue;
        for (int i = 0; i < values.Length - 2; i++)
        {
            long A = values[i];
            for (int k = i + 1; k < values.Length - 1; k++)
            {
                long B = values[k];
                int left = k + 1;
                int right = values.Length - 1;
                while(left <= right)
                {
                    int mid = (left + right) / 2;
                    long C = values[mid];
                    long sum = A + B + C;
                    if (Math.Abs(sum) < curSumABS)
                    {
                        curSumABS = Math.Abs(sum);
                        answer[0] = A;
                        answer[1] = B;
                        answer[2] = C;
                    }
                    if(sum < 0)
                    {
                        left = mid + 1;
                    }
                    else
                    {
                        right = mid -1;
                    }
                }
            }
        }
        Console.WriteLine(string.Join(" ", answer));
    }
}