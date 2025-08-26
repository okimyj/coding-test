internal class Program
{
    static void Main()
    {
        new BaekJoon_1744().Start();
    }
}
public class BaekJoon_1744
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        PriorityQueue<int, int> positiveNumbers = new PriorityQueue<int, int>();
        PriorityQueue<int, int> negativeNumbers = new PriorityQueue<int, int>();

        for(int i=0; i<N; i++)
        {
            int number = int.Parse(Console.ReadLine());
            if (number > 0)
                positiveNumbers.Enqueue(number, -number);
            else
                negativeNumbers.Enqueue(number, number);
        }
        int sum = 0;
        while(positiveNumbers.Count > 0)
        {
            int A = positiveNumbers.Dequeue();
            if(positiveNumbers.Count > 0)
            {
                int B = positiveNumbers.Dequeue();
                if (A == 1 || B == 1)
                {
                    sum += A + B;
                }
                else
                {
                    sum += A * B;
                }
            }
            else
            {
                sum += A;
            }
            
                
        }
        while(negativeNumbers.Count > 0)
        {
            int A = negativeNumbers.Dequeue();
            int B = 1;
            if (negativeNumbers.Count > 0)
            {
                B = negativeNumbers.Dequeue();
            }
            sum += A * B;
        }
        Console.WriteLine(sum);
    }
}