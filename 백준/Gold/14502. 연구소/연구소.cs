using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static int ROWS = 0;
        static int COLS = 0;
        static int maxSafeArea = 0;
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            ROWS = input[0];
            COLS = input[1];
            int[,] graph = new int[ROWS, COLS];
            for(int i=0; i<ROWS; i++)
            {
                input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
                for(int j=0; j<COLS; j++)
                {
                    graph[i, j] = input[j];
                }
            }
            MakeWall(graph, 0);
            Console.WriteLine(maxSafeArea);

        }
        static void MakeWall(int[,] graph, int count)
        {
            if(count == 3)
            {
                int[,] copy = new int[ROWS, COLS];
                Array.Copy(graph, copy, graph.Length);
                BFS(copy);
                return;
            }
            for (int r = 0; r < ROWS; r++)
            {
                for (int c = 0; c < COLS; c++)
                {
                    if(graph[r, c] == 0)
                    {
                        graph[r, c] = 1;
                        MakeWall(graph, count+1);
                        graph[r, c] = 0;
                    }
                }
            }
        }
        static void BFS(int[,] graph)
        {
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            Queue<(int r, int c)> q = new Queue<(int r, int c)>();
            for(int r = 0;r < ROWS; r++)
            {
                for(int c  = 0; c < COLS; c++)
                {
                    if(graph[r, c] == 2)
                    {
                        q.Enqueue((r, c));
                        graph[r, c] = 2;
                        while (q.Count > 0)
                        {
                            (int curR, int curC) = q.Dequeue();
                            for (int i = 0; i < dr.Length; i++)
                            {
                                int nextR = curR + dr[i];
                                int nextC = curC + dc[i];
                                if (nextR < 0 || nextC < 0 || nextR >= ROWS || nextC >= COLS || graph[nextR, nextC] != 0)
                                    continue;
                                q.Enqueue((nextR, nextC));
                                graph[nextR, nextC] = 2;
                            }
                        }
                    }
                }
            }
            int count = 0;
            for(int r = 0; r < ROWS; r++)
            {
                for(int c = 0;c < COLS; c++)
                {
                    if(graph[r, c] == 0)
                        count++;
                }
            }
            maxSafeArea = Math.Max(count, maxSafeArea);
        }
    }
}
