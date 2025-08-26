internal class Program
{
    static void Main(string[] args)
    {
        new BaekJoon_10773().Start();
    }
}
public class BaekJoon_10773
{
    public void Start()
    {
        int K = int.Parse(Console.ReadLine());
        Stack<int> s = new Stack<int>();
        for (int i = 0; i < K; i++)
        {
            int input = int.Parse(Console.ReadLine());
            if(input == 0 && s.Count > 0)
            {
                s.Pop();
            }
            else
            {
                s.Push(input);
            }
            
        }
        Console.WriteLine(s.Sum());
    }
    
}