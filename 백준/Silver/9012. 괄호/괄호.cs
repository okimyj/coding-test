namespace OKIMYJ
{
	internal class Program
	{
		static void Main(string[] args)
		{
			int lineNum = int.Parse(Console.ReadLine());
			for (int i = 0; i < lineNum; ++i)
			{
				string brackets = Console.ReadLine();
				Stack<char> check = new Stack<char>();
				foreach (char c in brackets)
				{
					if (c == '(')
						check.Push(c);
					else
					{
						if (check.Count() > 0 && check.Last() == '(')
						{
							check.Pop();
						}
						else
						{
							check.Push(c);
							break;
						}

					}
				}

				Console.WriteLine(check.Count() > 0 ? "NO" : "YES");
			}

		}
	}
}