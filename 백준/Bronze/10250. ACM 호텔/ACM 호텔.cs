int testNum = int.Parse(Console.ReadLine());
for (int i=0; i<testNum; ++i)
{
  int[] split = Console.ReadLine().Split(' ').Select(c => int.Parse(c)).ToArray();
  int floor = split[2] % split[0];
  floor = floor == 0 ? split[0] * 100 : floor * 100;
  int roomNumber = (int)Math.Ceiling((double)split[2]/split[0]);
  Console.WriteLine(floor+roomNumber);
}