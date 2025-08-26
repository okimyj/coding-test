namespace BaekJoon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            new BaekJoon_9012().Start();
        }
    }
    public class BaekJoon_9012
    {
        public void Start()
        {
            int N = int.Parse(Console.ReadLine());
            int count = 0;
            for(int i=0; i<N; i++)
            {
                string input = Console.ReadLine();
                for(int c = 0; c < input.Length; c++)
                {
                    if (input[c] == '(')
                    {
                        ++count;
                    }
                    else
                    {
                        --count;
                        if (count < 0)
                            break;
                    }
                }
                if (count == 0)
                    Console.WriteLine("YES");
                else
                    Console.WriteLine("NO");
                count = 0;
            }
        }
    }

}
