using System;
using System.Collections.Generic;

class Program
{
    private const int INF = int.MaxValue;

    static void Main()
    {
        string[] ve = Console.ReadLine().Split();
        int V = int.Parse(ve[0]);
        int E = int.Parse(ve[1]);
        int K = int.Parse(Console.ReadLine());

        List<(int to, int weight)>[] graph = new List<(int, int)>[V + 1];
        for (int i = 0; i <= V; i++)
            graph[i] = new List<(int, int)>();

        for (int i = 0; i < E; i++)
        {
            string[] edge = Console.ReadLine().Split();
            int u = int.Parse(edge[0]);
            int v = int.Parse(edge[1]);
            int w = int.Parse(edge[2]);
            graph[u].Add((v, w));
        }

        int[] dist = new int[V + 1];
        for (int i = 1; i <= V; i++)
            dist[i] = INF;
        dist[K] = 0;

        PriorityQueue<(int node, int cost), int> pq = new PriorityQueue<(int, int), int>();
        pq.Enqueue((K, 0), 0);

        while (pq.Count > 0)
        {
            var (curNode, curCost) = pq.Dequeue();

            if (curCost > dist[curNode])
                continue;

            foreach (var (nextNode, weight) in graph[curNode])
            {
                int newCost = dist[curNode] + weight;
                if (newCost < dist[nextNode])
                {
                    dist[nextNode] = newCost;
                    pq.Enqueue((nextNode, newCost), newCost);
                }
            }
        }

        for (int i = 1; i <= V; i++)
        {
            Console.WriteLine(dist[i] == INF ? "INF" : dist[i]);
        }
    }
}
