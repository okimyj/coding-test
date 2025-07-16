using System;
using System.Linq;
namespace CodingTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int T = int.Parse(Console.ReadLine());
            for(int i=0; i<T; i++)
            {
                TestDFS();
            }
        }
        static void TestDFS()
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int COLS = input[0];
            int ROWS = input[1];
            int K = input[2];
            int[,] graph = new int[ROWS, COLS];
            for (int i = 0; i < K; i++)
            {
                input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
                graph[input[1], input[0]] = 1;
            }
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            int count = 0;
            for (int r = 0; r < ROWS; r++)
            {
                for (int c = 0; c < COLS; c++)
                {
                    if(graph[r, c] == 1)
                    {
                        count++;
                        TestDFSBody(r, c, graph, COLS, ROWS);
                    }
                }
            }
            Console.WriteLine(count);
        }
        static void TestDFSBody(int curR, int curC, int[,] graph, int COLS, int ROWS)
        {
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            graph[curR, curC] = 0;
            for(int i=0; i<dr.Length; i++)
            {
                int nextR = curR + dr[i];
                int nextC = curC + dc[i];
                if (nextR < 0 || nextC < 0 || nextR >= ROWS || nextC >= COLS || graph[nextR, nextC] == 0)
                    continue;
                graph[nextR, nextC] = 0;
                TestDFSBody(nextR, nextC, graph, COLS, ROWS);
            }
        }
        static void TestBFS()
        {
            int[] input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int COLS = input[0];
            int ROWS = input[1];
            int K = input[2];
            int[,] graph = new int[ROWS, COLS];
            for(int i=0; i<K; i++)
            {
                input = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
                graph[input[1], input[0]] = 1;
            }
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            Queue<(int r, int c)> q = new Queue<(int r, int c)>();
            int count = 0;
            for (int r = 0; r < ROWS; r++) 
            { 
                for(int c = 0; c<COLS; c++)
                {
                    if (graph[r, c] == 1)
                    {
                        count++;
                        q.Enqueue((r, c));
                        graph[r, c] = 0;
                        while(q.Count > 0)
                        {
                            (int curR, int curC) = q.Dequeue();
                            for(int i=0; i<dr.Length; i++)
                            {
                                int nextR = curR + dr[i];
                                int nextC = curC + dc[i];
                                if (nextR < 0 || nextC < 0 || nextR >= ROWS || nextC >= COLS || graph[nextR, nextC] == 0)
                                    continue;
                                q.Enqueue((nextR, nextC));
                                graph[nextR, nextC] = 0;
                            }
                        }
                    }
                }
            }
            Console.WriteLine(count);
        }
    }
}
