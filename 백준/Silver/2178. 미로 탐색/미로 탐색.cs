using System.ComponentModel;

internal class Program
{
  private static void Main(string[] args)
  {
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    int N = input[0];
    int M = input[1];
    int[,] graph = new int[N, M];
    for (int i = 0; i < N; i++)
    {
      string line = Console.ReadLine();
      for (int j = 0; j < line.Length; j++)
      {
        graph[i, j] = Convert.ToInt32(line[j]) - '0';
      }
    }
    int[,] visited = new int[N, M];
    Queue<KeyValuePair<int, int>> q = new Queue<KeyValuePair<int, int>>();
    q.Enqueue(new KeyValuePair<int, int>(0, 0));
    visited[0, 0] = 1;
    // U D L R.
    int[] dx = { 0, 0, -1, 1 };
    int[] dy = { -1, 1, 0, 0 };
    while (q.Count > 0)
    {
      var curPos = q.Dequeue();
      if (curPos.Key == N-1 && curPos.Value == M-1)
        break;
      for (int i = 0; i < dx.Length; i++)
      {
        int nextY = curPos.Key + dy[i];
        int nextX = curPos.Value + dx[i];
        if (nextX < 0 || nextY < 0 || M <= nextX || N <= nextY)
          continue;
        if (visited[nextY, nextX] > 0 || graph[nextY, nextX] == 0)
          continue;
        visited[nextY, nextX] = visited[curPos.Key, curPos.Value] +1;
        q.Enqueue(new KeyValuePair<int, int>(nextY, nextX));
      }
    }
    Console.WriteLine(visited[N-1,M-1]);
  }
  
}