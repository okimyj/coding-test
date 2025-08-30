internal class Program
{
    static void Main()
    {
        new BaekJoon_14940().Start();
    }
}
public class BaekJoon_14940
{
    public void Start()
    {
        // 세로 / 가로.
        int[] NM = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int[][] map = new int[NM[0]][];
        int[][] dist = new int[NM[0]][];
        int sr = -1, sc = -1;
        
        for (int r=0; r < NM[0]; r++)
        {
            map[r] = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            dist[r] = new int[NM[1]];
            Array.Fill(dist[r], -1);
            for(int c=0; c < NM[1]; c++)
            {
                if (map[r][c] == 0)
                    dist[r][c] = 0;
                else if (map[r][c] == 2)
                {
                    dist[r][c] = 0;
                    sr = r;
                    sc = c;
                }
            }
        }
        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };
        Queue<(int r, int c)> q = new Queue<(int r, int c)>();
        q.Enqueue((sr, sc));
        while (q.Count > 0) 
        {
            (int r, int c) = q.Dequeue();
            for(int i=0; i<dr.Length; i++)
            {
                int nextR = r + dr[i];
                int nextC = c + dc[i];
                if (nextR < 0 || nextC < 0 || nextR >= NM[0] || nextC >= NM[1] || dist[nextR][nextC] != -1)
                    continue;
                dist[nextR][nextC] = dist[r][c] + 1;
                q.Enqueue((nextR, nextC));
            }
        }
        for(int i=0; i < NM[0]; i++)
        {
            Console.WriteLine(string.Join(" ", dist[i]));
        }
    }
}