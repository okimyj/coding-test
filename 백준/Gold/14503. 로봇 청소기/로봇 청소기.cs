    internal class Program
    {
        static void Main()
        {
            new BaekJoon_14503().Start();
        }
    }
    public class BaekJoon_14503
    {
        public void Start()
        {
            int[] mapSize = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            int[][] map = new int[mapSize[0]][];
            for(int i=0; i < mapSize[0]; i++)
            {
                map[i] = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            }
            // 북, 동, 남, 서
            int[] dr = { -1, 0, 1, 0 };
            int[] dc = { 0, 1, 0, -1 };
            bool[,] visited = new bool[mapSize[0], mapSize[1]];
            Queue<(int r, int c)> q = new Queue<(int r, int c)>();
            q.Enqueue((input[0], input[1]));
            int count = 0;
            int curDir = input[2];
            while(q.Count > 0)
            {
                (int r, int c) = q.Dequeue();
                if (map[r][c] == 0)
                {
                    count++;
                    map[r][c] = 2;
                }
                    
                bool isAllClean = true;
                for(int i=0; i<dr.Length; i++)
                {
                    int nextR = r + dr[i];
                    int nextC = c + dc[i];
                    if (nextR < 0 || nextC < 0 || nextR >= mapSize[0] || nextC >= mapSize[1])
                        continue;
                    if (map[nextR][nextC] == 0)
                    {
                        isAllClean = false;
                        break;
                    }
                }
                // 4방향 전부 다 청소되어있음. 후진.
                if(isAllClean)
                {
                    int nextR = r - dr[curDir];
                    int nextC = c - dc[curDir];
                    if (nextR < 0 || nextC < 0 || nextR >= mapSize[0] || nextC >= mapSize[1] || map[nextR][nextC] == 1)
                    {
                        // 후진하려는데 벽임. 작동 중지. 
                        break;
                    }
                    else
                    {
                        q.Enqueue((nextR, nextC));
                    }
                }
                else
                {
                    // 반시계 방향 회전.
                    for(int i=0; i<dr.Length; i++)
                    {
                        curDir = (curDir + 3) % 4;
                        
                        int nextR = r + dr[curDir];
                        int nextC = c + dc[curDir];
                        // 빈칸이면 전진. 아니면 제자리. 
                        if (nextR < 0 || nextC < 0 || nextR >= mapSize[0] || nextC >= mapSize[1] || map[nextR][nextC] != 0)
                            continue;
                        
                        q.Enqueue((nextR, nextC));
                        break;
                    }
                        
                }
            }
            Console.WriteLine(count);
        }
    }