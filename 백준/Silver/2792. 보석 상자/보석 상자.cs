internal class Program
{
    static void Main()
    {
        new BaekJoon_2792().Start();
    }
}
public class BaekJoon_2792
{
    public void Start()
    {
        int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int N = input[0];       // 학생 수.
        int M = input[1];       // 보석 색상 수. 
        int[] quantities = new int[M];
        for(int i=0; i<M; i++)
        {
            quantities[i] = int.Parse(Console.ReadLine());
        }
        int max = quantities.Max();
        int min = 1;
        int answer = 0;
        while(min <= max)
        {
            int mid = (min + max) / 2;
            int count = 0;      // 보석을 받을 학생 수.
            for(int i=0; i<quantities.Length; i++)
            {
                count += (quantities[i] / mid) + (quantities[i] % mid == 0 ? 0 : 1);
            }
            if(count > N)
            {
                min = mid + 1;
            }
            else if(count <= N)
            {
                answer = mid;
                max = mid - 1;
            }
        }
        Console.WriteLine(answer);
    }
}