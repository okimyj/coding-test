using System.Linq;
using System.Text;
internal class Program
{
  private static Dictionary<int, List<int>> graph;
  private static int N;
  private static void Main(string[] args)
  {
    int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
    N = input[0];   // 정점의 갯수.
    int M = input[1];   // 간선의 갯수.
    int S = input[2];   // 시작 점.

    // 그래프 생성. 
    graph = new Dictionary<int, List<int>>();
    for (int i = 0; i < M; i++)
    {
      input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
      if (!graph.ContainsKey(input[0]))
        graph[input[0]] = new List<int>();
      if (!graph.ContainsKey(input[1]))
        graph[input[1]] = new List<int>();

      graph[input[0]].Add(input[1]);
      graph[input[1]].Add(input[0]);
    }
    // 간선이 여러개인 경우 숫자가 작은 정점부터 방문한다. 정렬.
    foreach (var kv in graph)
    {
      kv.Value.Sort();
    }

    bool[] visited = new bool[N + 1];
    visited[S] = true;
    List<int> visitedOrder = new List<int>();
    DFS(S, visited, visitedOrder);
    Console.WriteLine(string.Join(' ', visitedOrder));
    BFS(S);
  }
  private static void DFS(int cur, bool[] visited, List<int> visitedOrder)
  {
    visitedOrder.Add(cur);
    if (graph.TryGetValue(cur, out var list))
    {
      for (int i = 0; i < list.Count; i++)
      {
        if (!visited[list[i]])
        {
          visited[list[i]] = true;
          DFS(list[i], visited, visitedOrder);
        }
      }
    }
  }

  private static void BFS(int S)
  {
    bool[] visited = new bool[N + 1];
    Queue<int> q = new Queue<int>();
    List<int> visitedOrder = new List<int>();
    q.Enqueue(S);
    visited[S] = true;
    while (q.Count > 0)
    {
      int cur = q.Dequeue();
      visitedOrder.Add(cur);
      if (graph.TryGetValue(cur, out var list))
      {
        for (int i = 0; i < list.Count; i++)
        {
          if (!visited[list[i]])
          {
            visited[list[i]] = true;
            q.Enqueue(list[i]);
          }
        }
      }
    }
    Console.WriteLine(string.Join(' ', visitedOrder));
  }
}