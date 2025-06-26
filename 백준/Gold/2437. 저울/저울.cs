using System.Linq;
internal class Program
{
  // 입력 받은 무게를 오름차순으로 정렬.
  // 순서대로 무게를 누적하면서 targetWeight보다 큰 무게가 들어오는 경우 break. (해당 무게는 잴 수 없는 무게이므로)
  private static void Main(string[] args)
  {
    Console.ReadLine();
    int[] weights = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).OrderBy(x => x).ToArray();
    int targetWeight = 1;
    for (int i = 0; i < weights.Length; i++)
    {
      if (targetWeight < weights[i])
        break;
      targetWeight += weights[i];
    }
    Console.WriteLine(targetWeight);
  }
}