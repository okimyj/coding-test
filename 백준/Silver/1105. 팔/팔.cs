using System.Linq;
internal class Program
{
  // 두 숫자의 자릿수가 다르다 -> 10, 100, 1000, ... 같이 반드시 10 으로 떨어지는 숫자가 있으므로 8의 최소 개수는 0.
  // 첫째 자리수부터 비교. 두 개의 값이 같고 8이라면 answer++, 같기만 하다면 패스.
  // 값이 달라진다면 해당 자리와 그 이후로는 8이 아닌 다른 수가 올 수 있음. break.
  private static void Main(string[] args)
  {
    string[] input = Console.ReadLine().Split(' ').ToArray();
    int answer = 0;
    if (input[0].Length == input[1].Length)
    {
      string L = input[0];
      string R = input[1];
      for (int i = 0; i < L.Length; i++)
      {
        //L의 자릿수가 8이 아닌 경우 8은 올 수 없음.
        if (L[i] == R[i])
        {
          if (L[i] == '8')
          {
            answer++;
          }
        }
        else
          break;

      }
    }

    Console.WriteLine(answer);
  }
}