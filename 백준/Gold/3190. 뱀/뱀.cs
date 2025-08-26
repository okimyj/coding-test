internal class Program
{
    static void Main(string[] args)
    {
        new BaekJoon_3190().Start();
    }
}
public class BaekJoon_3190
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        int K = int.Parse(Console.ReadLine());
        int[,] board = new int[N+1, N+1];
        
        for(int i=0; i<K; i++)
        {
            int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            board[input[0], input[1]] = 1;
        }
        
        int L = int.Parse(Console.ReadLine());
        Queue<(int t, int dir)> command = new Queue<(int t, int dir)>();
        for(int i=0; i<L; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            command.Enqueue((int.Parse(input[0]), input[1] == "D" ? 1 : -1));
        }
        
        List<(int r, int c)> snake = new List<(int r, int c)>();
        snake.Add((1, 1));
        board[1, 1] = 2;
        int time = 0;
        // right, down, left, up.
        int[] dc = { 1, 0, -1, 0 };
        int[] dr = { 0, 1, 0, -1 };
        int curDir = 0;
        while(true)
        {
            ++time;
            // 이동 처리. 
            (int headR, int headC) = snake[0];
            int nextR = headR + dr[curDir];
            int nextC = headC + dc[curDir];
            // 벽 체크. 
            if (nextR < 1 || nextC < 1 || nextR > N || nextC > N)
                break;
            // 뱀 체크.
            if (board[nextR, nextC] == 2)
                break;
            if (board[nextR, nextC] == 0)
            {
                (int tailR, int tailC) = snake[snake.Count - 1];
                board[tailR, tailC] = 0;
                snake.RemoveAt(snake.Count - 1);
            }
            
            board[nextR, nextC] = 2;
            snake.Insert(0, (nextR, nextC));

            // 방향 회전 처리. 
            if (command.Count > 0 && command.Peek().t == time)
            {
                (int t, int dir) = command.Dequeue();
                curDir = (4 + curDir + dir) % 4;
                
            }

        }
        Console.WriteLine(time);
    }
    
}