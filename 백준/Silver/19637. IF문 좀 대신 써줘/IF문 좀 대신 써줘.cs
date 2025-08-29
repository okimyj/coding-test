using System.Text;

internal class Program
{
    static void Main()
    {
        new BaekJoon_19637().Start();
    }
}
public class BaekJoon_19637
{
    public void Start()
    {
        int[] inputSize = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        List<(string title, int power)> titles = new List<(string title, int power)>();
        for(int i=0; i < inputSize[0]; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            titles.Add((input[0], int.Parse(input[1])));
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i < inputSize[1]; i++)
        {
            int power = int.Parse(Console.ReadLine());
            int left = 0;
            int right = inputSize[0]-1;
            int mid = (left + right) / 2;
            
            while (left <= right)
            {
                if(power > titles[mid].power)
                {
                    left = mid+1;
                }
                else
                {
                    right = mid - 1;
                }
                mid = (left + right) / 2;
            }
            sb.Append(titles[left].title).Append("\n");
            
            
        }
        Console.WriteLine(sb.ToString());
    }
}