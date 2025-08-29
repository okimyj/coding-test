internal class Program
{
    static void Main()
    {
        new BaekJoon_7576().Start();
    }
}
public class BaekJoon_7576
{
    public void Start()
    {
        int[] dr = new int[] { 0, 1, 0, -1};
        int[] dc = new int[] { 1, 0, -1, 0 };
        // 가로, 세로.
        int[] size = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int[][] tomatoBox = new int[size[1]][];
        int tomatoNum = 0;         // 안익은 토마토 개수. 
        int answer = -1;
        Queue<(int r, int c, int day)> q = new Queue<(int r, int c, int day)>();
        for (int r=0; r < size[1]; r++)
        {
            int[] tomatos = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            for(int c=0; c<tomatos.Length; c++)
            {
                if (tomatos[c] == 0)
                    tomatoNum++;
                else if (tomatos[c] == 1)
                {
                    q.Enqueue((r, c, 0));
                }
            }
            tomatoBox[r] = tomatos;
        }
        // 토마토가 이미 모두 익어있는 상태.
        if (tomatoNum == 0)
        {
            Console.WriteLine(0);
            return;
        }
            
        // 모두 빈 상자.
        if(q.Count == 0)
        {
            Console.WriteLine(-1);
            return;
        }

        while (q.Count > 0)
        {
            (int r, int c, int day) = q.Dequeue();
            answer = day;
            for (int i=0; i<dr.Length; i++)
            {
                int nextR = r + dr[i];
                int nextC = c + dc[i];
                if (nextR < 0 || nextC < 0 || nextR >= size[1] || nextC >= size[0] || tomatoBox[nextR][nextC] != 0)
                    continue;
                tomatoNum--;
                tomatoBox[nextR][nextC] = 1;
                q.Enqueue((nextR, nextC, day + 1));
            }
        }

        if(tomatoNum == 0)
        {
            Console.WriteLine(answer);
        }
        else
        {
            Console.WriteLine(-1);
        }
    }
}