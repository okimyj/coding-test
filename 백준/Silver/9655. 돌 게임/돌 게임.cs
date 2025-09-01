internal class Program
{
    static void Main()
    {
        new BaekJoon_9655().Start();
    }
}
public class BaekJoon_9655
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        Console.WriteLine(N % 2 == 0 ? "CY" : "SK");
    }
}