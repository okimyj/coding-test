internal class Program
{
    
    static void Main(string[] args)
    {
        /*
        Solution s = new Solution();
        //Console.WriteLine(s.solution(new int[] { 1,3,2}, new string[] { "diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone" }));
        Console.WriteLine(s.solution_12946(4));
        */
        new BaekJoon_2644().Start();
    }
}
public class BaekJoon_2644
{
    public void Start()
    {
        int N = int.Parse(Console.ReadLine());
        int[] target = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int M = int.Parse(Console.ReadLine());
        Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
        for(int i=0; i<M; i++)
        {
            int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            if (!graph.TryGetValue(input[0], out var list1))
            {
                list1 = new List<int>();
                graph[input[0]] = list1;
            }
            if (!graph.TryGetValue(input[1], out var list2))
            {
                list2 = new List<int>();
                graph[input[1]] = list2;
            }
            list1.Add(input[1]);
            list2.Add(input[0]);
        }

        bool[] visited = new bool[N+1];
        Queue<(int, int)> q = new Queue<(int, int)>();
        q.Enqueue((target[0], 0));
        visited[target[0]] = true;
        int answer = -1;
        while (q.Count > 0) 
        {
            (int cur, int count) = q.Dequeue();
            if (cur == target[1])
            {
                answer = count;
                break;
            }
            List<int> list = graph[cur];
            if(list == null)
                continue;
            for(int i=0; i<list.Count; i++)
            {
                if (visited[list[i]])
                    continue;
                visited[list[i]] = true;
                q.Enqueue((list[i], count+1));
            }

        }
        
        Console.WriteLine(answer);
    }
}