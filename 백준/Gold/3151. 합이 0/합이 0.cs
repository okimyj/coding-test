internal class Program
{
    static void Main()
    {
        new BaekJoon_3151().Start();
    }
}
public class BaekJoon_3151
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        int[] levels = Console.ReadLine().Split(' ').Select(int.Parse).OrderByDescending(x => x).ToArray();
        Dictionary<int, int> levelCount = new Dictionary<int, int>();
        for(int i=0; i<levels.Length; i++)
        {
            levelCount[levels[i]] = levelCount.GetValueOrDefault(levels[i], 0) + 1;
        }
        long answer = 0;
        for(int i=0; i<levels.Length; i++)
        {
            int A = levels[i];
            for (int j=i+1; j<levels.Length; j++)
            {
                int B = levels[j];
                int sum = A + B;
                if(levelCount.TryGetValue(-sum, out int count))
                {
                    answer += count;
                    if (-sum == levels[i])
                        answer--;
                    if (-sum == levels[j])
                        answer--;
                }
            }
        }
        Console.WriteLine(answer/3);
    }
}