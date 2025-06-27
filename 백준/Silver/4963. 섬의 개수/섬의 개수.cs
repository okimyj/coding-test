using System.ComponentModel;

internal class Program
{
  // U D L R, UL, UR, DL, DR
  static int[] dx = { 0, 0, -1, 1, -1, 1, -1, 1};
  static int[] dy = { -1, 1, 0, 0, -1, -1, 1, 1};
  private static void Main(string[] args)
  {
    while (true)
    {
      int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
      if (input[0] == input[1] && input[0] == 0)
        break;
      int W = input[0];
      int H = input[1];
      int[,] map = new int[H, W];
      for (int i = 0; i < H; i++)
      {
        input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
        for (int k = 0; k < input.Length; k++)
        {
          map[i, k] = input[k];
        }
      }
      Console.WriteLine(BFS(map));

    }
  }
  private static int BFS(int[,] map)
  {
    int H = map.GetLength(0);
    int W = map.GetLength(1);
    bool[,] visited = new bool[H, W];
    Queue<KeyValuePair<int, int>> q = new Queue<KeyValuePair<int, int>>();
    
    //Console.WriteLine($"BFS H : {H}, W : {W}");
    
    int num = 0;
    for (int y = 0; y < H; y++)
    {
      for (int x = 0; x < W; x++)
      {
        if (!visited[y, x] && map[y, x] == 1)
        {
          q.Enqueue(new KeyValuePair<int, int>(y, x));
          visited[y, x] = true;
          num++;
          while (q.Count > 0)
          {
            var curPos = q.Dequeue();
            for (int i = 0; i < dx.Length; i++)
            {
              int nextY = curPos.Key + dy[i];
              int nextX = curPos.Value + dx[i];
              if (nextY < 0 || nextX < 0 || nextY >= H || nextX >= W)
                continue;
              if (visited[nextY, nextX] || map[nextY, nextX] == 0)
                continue;
              visited[nextY, nextX] = true;
              q.Enqueue(new KeyValuePair<int, int>(nextY, nextX));
            }
          }
        }
      }
    }
    return num;
  }
}