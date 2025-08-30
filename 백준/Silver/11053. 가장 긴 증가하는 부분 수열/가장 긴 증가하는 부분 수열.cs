internal class Program
{
    static void Main()
    {
        new BaekJoon_11053().Start();
    }
}
public class BaekJoon_11053
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        int[] A = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int[] dp = new int[N];
        Array.Fill(dp, 1);
        for (int i=0; i<N; i++)
        {
            for(int j=0; j<i; j++)
            {
                if (A[j] < A[i])
                {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
            
        }
        Console.WriteLine(dp.Max());
    }
}