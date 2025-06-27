using System.ComponentModel;

internal class Program
{
  // 비가 아예 오지 않을 수도 있고, 비는 입력된 map의 최대값 만큼도 올 수 있다고 가정.
  // 안전 영역의 최대 값을 구하는 것.
  static int[,] map;
  // U D L R.
  static int[] dx = { 0, 0, -1, 1 };
  static int[] dy = { -1, 1, 0, 0};
  private static void Main(string[] args)
  {
    int N = Convert.ToInt32(Console.ReadLine());
    int limit = 0;
    map = new int[N, N];
    for (int i = 0; i < N; i++)
    {
      string[] input = Console.ReadLine().Split(' ').ToArray();
      for (int k = 0; k < input.Length; k++)
      {
        map[i, k] = Convert.ToInt32(input[k]);
        limit = Math.Max(limit, map[i, k]);
      }
    }
    Queue<KeyValuePair<int, int>> q = new Queue<KeyValuePair<int, int>>();
    int maxSafeArea = 0;
    for (int height = 0; height < limit; height++)
    {
      int safeArea = 0;
      bool[,] visited = new bool[N, N];
      for (int y = 0; y < N; y++)
      {
        for (int x = 0; x < N; x++)
        {
          if (!visited[y, x] && map[y, x] > height)
          {
            q.Enqueue(new KeyValuePair<int, int>(y, x));
            visited[y, x] = true;
            ++safeArea;
            while (q.Count > 0)
            {
              var curPos = q.Dequeue();
              for (int i = 0; i < dx.Length; i++)
              {
                int nextY = curPos.Key + dy[i];
                int nextX = curPos.Value + dx[i];
                // 영역체크.
                if (nextY < 0 || nextX < 0 || nextY >= N || nextX >= N)
                  continue;
                if (visited[nextY, nextX])
                  continue;
                visited[nextY, nextX] = true;
                if (map[nextY, nextX] > height)
                  q.Enqueue(new KeyValuePair<int, int>(nextY, nextX));
              }
            }
          }
        }
      }
      maxSafeArea = Math.Max(safeArea, maxSafeArea);
    }
    Console.WriteLine(maxSafeArea);
  }
}