internal class Program
{
    static void Main()
    {
        new BaekJoon_6236().Start();
    }
}
public class BaekJoon_6236
{
    public void Start()
    {
        int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int N = input[0];
        int M = input[1];
        int[] needMoney = new int[N];
        for(int i=0; i<N; i++)
        {
            needMoney[i] = int.Parse(Console.ReadLine());
        }

        int min = needMoney.Max();
        int max = needMoney.Sum();
        while (min <= max)
        {
            int mid = (min + max) / 2;
            int count = 1;
            int money = mid;
            for(int i=0; i<needMoney.Length; i++)
            {
                if (money < needMoney[i])
                {
                    count++;
                    money = mid;
                }
                money -= needMoney[i];
            }
            

            if (count <= M)
            {
                max = mid - 1;
            }
            else
            {
                min = mid + 1;
            }
            
        }
        Console.WriteLine(min);

    }
    

}