import sys
input = sys.stdin.readline
input()
sInput = list(map(int, input().rstrip().split()))
for _ in range(int(input())) :
  gender, number = input().rstrip().split()
  number = int(number)
  if gender == '1' :
    for i in range(number, len(sInput)+1, number) :
      sInput[i-1] = not sInput[i-1]
  else :
    number -= 1
    sInput[number] = not sInput[number]
    for i in range(1, len(sInput)//2+1) :
      if number-i < 0 or len(sInput) <= number+i :
        break
      if sInput[number+i] == sInput[number-i] :
        sInput[number+i] = not sInput[number+i]
        sInput[number-i] = not sInput[number-i]
      else:
        break


if len(sInput) // 20 > 0 :

  for i in range(len(sInput)) :
    if i % 20 == 19 or i == len(sInput) -1 :
      print(int(sInput[i]))
    else :
      print(int(sInput[i]), end=' ')

else:
  print(*map(int, sInput))